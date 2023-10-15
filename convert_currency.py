import requests
import pandas as pd
import argparse
from config import API_KEY


def read_data(input_path: str) -> pd.DataFrame:
    print(f"Loading data from {input_path}")
    try:
        return pd.read_csv(input_path)
    except FileNotFoundError:
        print("File not found, check input data")


def convert_to_currency(dataset: pd.DataFrame, rates: dict, currency: str) -> None:
    print(f"Converting local currencies to {currency}...")
    dataset["budget_local_currency"] = dataset[f"budget_{currency}"] * dataset[
        "local_currency"
    ].apply(lambda row: rates.get(row))


def save_to_csv(dataset: pd.DataFrame, filename: str) -> None:
    print(f"Saving converted dataset to {filename}")
    output_name = filename.split(".")[0] + "_local_currency.csv"
    dataset.to_csv(output_name)


def get_exchange_rates(currency: str) -> dict:
    rates_content = (
        requests.get(
            f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{currency.upper()}"
        )
        .json()
        .get("conversion_rates")
    )
    if rates_content:
        return rates_content
    raise Exception(f"Invalid currency: {currency}")


def check_mandatory_columns(currency: str, dataset: pd.DataFrame) -> None:
    mandatory_cols = ["local_currency", f"budget_{currency}"]
    for col in mandatory_cols:
        if col not in dataset.columns:
            raise Exception(
                f"Dataset is missing one or more mandatory columns ({mandatory_cols}). Please check input data."
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--currency",
        default="EUR",
        help="Currency expressed as ISO 4217 code, find out more about available options at https://www.exchangerate-api.com/docs/supported-currencies",
    )
    parser.add_argument(
        "-i",
        "--input_file",
        default="sales_report_input.csv",
        help="Path to CSV file with sales data, defaults to 'sales_report_input.csv' inside directory with this script",
    )
    parser.add_argument(
        "-u",
        "--output_file",
        default="sales_report_output.csv",
        help="Path to save output data, defaults to 'sales_report_output.csv' inside directory with this script",
    )
    args = parser.parse_args()

    data = read_data(args.input_file)
    rates = get_exchange_rates(args.currency)
    check_mandatory_columns(args.currency, data)
    convert_to_currency(data, rates, args.currency)
    save_to_csv(data, args.output_file)
