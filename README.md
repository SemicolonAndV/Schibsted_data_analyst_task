# Campaign analysis

The analysis can be found in the `campaign_analysis` directory. All the steps are explained inside Jupyter Notebook.

# Currency converter

This script allows to read the data from CSV file and convert campaign budget (by default given in EUR currency) to local currency of a given campaign. Column with this information is added to the data and displayed in the generated output file.

# Instructions

1) Prepare CSV file in the same directory as the script `convert_currency.py`. Make sure the file has two columns: `budget_{currency}` and `local_currency`. In case there is a column missing, the script will inform the user about required adjustments.
2) Prepare `config.py` file which contains API_KEY from the website `https://www.exchangerate-api.com/`.
2) Run the script `convert_currency.py`. For purpose of the basic task it takes no additional arguments required to run it, however it can be used with other currencies too.

NOTE: if API has no access to the currency given in any field of `local_currency` column, it will return `NaN` in the row with this currency.

## Script usage

usage: `convert_currency.py [-h] [-c CURRENCY] [-i INPUT_FILE] [-u OUTPUT_FILE]`

options:  
  -h, --help  
show this help message and exit  

  -c CURRENCY, --currency CURRENCY  
    Currency expressed as ISO 4217 code, defaults to `EUR`. find out more at https://www.exchangerate-api.com/docs/supported-currencies  

  -i INPUT_FILE, --input_file INPUT_FILE  
    Path to CSV file with input data, defaults to `sales_report_input.csv` inside directory with this script  

  -u OUTPUT_FILE, --output_file OUTPUT_FILE  
    Path to save output data, defaults to `sales_report_output.csv` inside directory with this script

## Task results

The resulting file can be found under `sales_report_output_local_currency.csv` file in this repository.
