import os
import sys
import pytest
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the project root to sys.path
sys.path.append(project_root)
from main import fetch_data

@pytest.fixture
def sample_page_no():
    '''Provides a constant sample page number to test downloading the data'''
    return 12
def test_fetch_data_from_url(sample_page_no):
    '''Test function to test the function to download the data and 
    write the data into a file'''

    data = fetch_data(sample_page_no)
    assert data is not None
    assert data.get('page', 0) == sample_page_no

