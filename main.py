# -*- coding: utf-8 -*-
# Example main.py
import argparse
import sys
import urllib
import urllib.request
import json


def fetch_data(page):
    url = (f"https://api.fbi.gov/wanted/v1/list?page={page}")
    headers = {}


    # Random user agent
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          
    # headers['page'] = page
    # formatted_url = urllib.request.Request(url, headers=headers)
    # data = urllib.request.urlopen().read(formatted_url)

    data = urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    data = json.loads(data.decode('utf-8'))
    return data
def fetch_data_from_file(file):
    with open(file, 'r') as f:
        data = f.read()
    data = json.loads(data)
    return data
def format_data(items):
    printable_list = []
    for item in items:
        title = item.get('title', '')
        subjects = item.get('subjects', [])
        field_offices = item.get('field_offices', [])
        # print(f'type of field offices - {type(field_offices)}')
        # print(f'{title}þ{subjects}þ{field_offices}')
        subjects_str = ''
        if subjects:
            for i in range(len(subjects)):
                if i==len(subjects)-1:
                    subjects_str = subjects_str + subjects[i]
                else:
                    subjects_str = subjects_str + subjects[i] + ', '
        field_offices_str = ''
        if field_offices:
            for i in range(len(field_offices)):
                if i==len(field_offices)-1:
                    field_offices_str = field_offices_str + field_offices[i]
                else:
                    field_offices_str = field_offices_str + field_offices[i] + ', '

        printable_list.append(f'{title}þ{subjects_str}þ{field_offices_str}')
    return printable_list
def print_items(printable_list):
    for item in printable_list:
        print(item)
def main(page=None, file=None):
    # Download data
    if page is not None:
        data = fetch_data(page)
    elif file is not None:
        data = fetch_data_from_file(file)	
    # # TODO call formating data function
    items = data.get('items', [])
    printable_list = format_data(items)
    print_items(printable_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=False, help="An Example API file.")
    parser.add_argument("--page", type=int, required=False, help="An Example API file.")
     
    args = parser.parse_args()
    if args.page:
        main(page=args.page)
    elif args.file:
        main(file=args.file)
    else:
        parser.print_help(sys.stderr)