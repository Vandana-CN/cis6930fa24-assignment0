import os
import sys
import pytest
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the project root to sys.path
sys.path.append(project_root)
from main import fetch_data_from_file

@pytest.fixture
def sample_file_path():
    '''Provides a constant sample file path to test downloading the data'''
    return 'test.json'
def test_fetch_data_from_file(sample_file_path):
    '''Test function to test the function to download the data and 
    write the data into a file'''

    data = fetch_data_from_file(sample_file_path)
    assert data is not None

