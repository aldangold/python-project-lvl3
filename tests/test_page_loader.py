from unittest import mock
import argparse
import pytest
import tempfile
import os

from page_loader import engine


@pytest.mark.parametrize(
    'url,name_file', [
        ('https://hexlet.io/courses', 'hexlet-io-courses.html'),
        ('http://hexlet.io', 'hexlet-io.html'),
    ],
)
def test_get_name(url, name_file):
    assert name_file == engine.get_name(url)


def test_load_file():
    url = 'https://hexlet.io/courses'
    with tempfile.TemporaryDirectory() as temp_dir:
        engine.load_page(temp_dir, url)
        name_file = engine.get_name(url)
        temp_path_file = os.path.join(temp_dir, name_file)
        assert os.path.exists(temp_path_file) == True


@mock.patch(
    'argparse.ArgumentParser.parse_args',
    return_value=argparse.Namespace(
        output='.',
        url='https://hexlet.io/courses',
    )
)
def test_parser(mock_args):
    args = engine.parser.parse_args()
    assert args.output == '.'
    assert args.url == 'https://hexlet.io/courses'
