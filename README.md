Name: Vandana Cendrollu Nagesh

# Project Description
1. FEATURES
This python package takes a page url (from the FBI wanted website) or path of a file as the input and does the following actions - 
1 - Fetches the FBI wanted data using urlib.requests library in python and loads the data in json format.
2 - Parses the data in the json to extract the title, subjects and field offices from each record.
3 - Prints each record in thron seperated format.

2. PROJECT STRUCTURE
The project is structured to have a main file that is triggered initially, which then internally utilizes three different functions, namely - fetch_data_from_url, fetch_data_from_file and format_data to perform the above described actions. All these files are in the main.py which lies in the root directory.

3. TESTING
This project can be classified into 3 parts - data download, data extraction, and printing the data. Three test files are designed to test each phase. test_data_from_url.py file tests the data extraction phase from the REST API, test_data_from_file.py file tests the data download phase, test_format_data.py tests the lines of code written to extract each information from the raw data record.

# How to install
pipenv install

## How to run
pipenv run python3 main.py --page <url>
or 
pipenv run python3 main.py --file <file_path>

[![Watch the video](https://img.youtube.com/vi/775e0nLt4gs/0.jpg)](https://youtu.be/4YBYvgKLAaM)

## How to test
pipenv run python3 -m pytest <test_file>

## Functions
#### main.py \
main() - This functions takes page number or file path as the parameter. This function downloads data, extracts FBI wanted information from the raw data, converts each record into desirable thorn seperated format and prints the formatted lines to the console.

fetch_data_from_url() - This function takes url as the parameter. This function takes the url and gets the binary data from the url, converts the data in JSON format and returns the data.

fetch_data_from_file() - This function takes file path as the parameter. This function takes the file and reads the binary data form the file into JSON and returns the data

format_data() - This function takes a list of items as the parameter. This function extracts the each item from the list and processes the data to return the information in the relevant thorn seperated format list where each item in the list is a thorn seperated string


print_items() - This function takes a list as parameter and prints each string in the list to the console

## Bugs and Assumptions
1. the items list must have the following keys - 'title', 'subjects', 'field_offices'
