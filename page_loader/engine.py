"""The loader core logic module."""

import os
import re
import argparse
import requests
from urllib import parse

PATTERN = r'[^A-Za-z0-9]'
SUB = '-'


def load_page(directory: str, url: str):
    """Loads the page to the set directory.

    Args:
        directory (str): String value of set directory.
        url (str): String value of URL.

    """
    content = get_page(url)
    name_of_file = get_name(url)
    path_for_save = os.path.join(directory, name_of_file)
    with open(os.path.abspath(path_for_save), 'wb') as file:
        file.write(content)


def get_page(url: str):
    response = requests.get(url)
    return response.content


def get_name(url: str):
    """Transforms URL to target format.

    Args:
        url (str): String value of URL.

    Returns:
        name_for_save (str): String value of name for file with extension html.
    """
    parsed_url = parse.urlparse(url)
    name = parsed_url.netloc + parsed_url.path
    name_for_save = '{}.html'.format(re.sub(PATTERN, SUB, name))
    return name_for_save


"""Parse arguments.

Automatically generate help and usage messages.

Returns:
    arguments (str): Gets from the command line,
    convert to the appropriate type.
"""
parser = argparse.ArgumentParser(description='Page loader')
parser.add_argument('url', type=str, help='URL for load')
parser.add_argument(
    '-o', '--output',
    default='',
    help='set directory for save')
