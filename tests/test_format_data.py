import os
import sys
import pytest
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the project root to sys.path
sys.path.append(project_root)
from main import format_data

@pytest.fixture
def sample_items_list():
    '''Provides a constant sample items list to test formatting the data'''
    items = [
      {
        "race_raw": "White",
        "weight_max": 115,
        "poster_classification": "missing",
        "path": "/wanted/kidnap/amanda-deguio",
        "suspects": None,
        "title": "AMANDA DEGUIO",
        "eyes_raw": "Blue",
        "modified": "2024-09-07T00:03:35+00:00",
        "weight": "Approximately 115 pounds",
        "details": "\u003Cp\u003EAmanda DeGuio was reported missing by relatives on August 27, 2014, but had not been seen by her family in Upper Darby, Pennsylvania, since the first week of June of 2014, after she returned from a trip to Florida.  She left home without her cell phone, credit cards, or additional clothing.  DeGuio does not drive and it is unknown how she left home.  She is known to frequent the Upper Darby, Clifton Heights, and the Overbrook section of Philadelphia, Pennsylvania.\u003C/p\u003E",
        "height_max": 62,
        "reward_max": 0,
        "hair_raw": "Brown",
        "sex": "Female",
        "hair": "brown",
        "height_min": 62,
        "files": [
          {
            "url": "https://www.fbi.gov/wanted/kidnap/amanda-deguio/download.pdf",
            "name": "English"
          }
        ],
        "dates_of_birth_used": [
          "March 5, 1990"
        ],
        "build": "Thin",
        "scars_and_marks": "DeGuio has the following tattoos:  lips or a lipstick mark on the right cheek of her buttocks, the Italian boot shape and the word \"Tommy\" on her right torso, writing under one of her breasts, initials on the top of one of her fingers, and the letters \"MF\" on the inside of her lower lip.  She also has a diagonal surgical scar on her upper and lower abdomen.",
        "subjects": [
          "Kidnappings and Missing Persons"
        ],
        "eyes": "blue",
        "field_offices": [
          "philadelphia"
        ],
        "coordinates": [],
        "description": "Upper Darby, Pennsylvania\r\nJune of 2014",
        "@id": "https://api.fbi.gov/@wanted-person/3e523bdc92e44b4ea3efd687115563b0"
      },
      {
        "race_raw": "White",
        "suspects": None,
        "title": "ALEKSEI SERGEYEVICH MORENETS",
        "eyes_raw": "Brown",
        "modified": "2024-09-07T00:03:35+00:00",
        "status": "na",
        "occupations": [
          "Officer in the Russian Federation’s Main Intelligence Directorate of the General Staff (GRU)"
        ],
        "files": [
          {
            "url": "https://www.fbi.gov/wanted/cyber/aleksei-sergeyevich-morenets/aleksei-sergeyevich-morenets-8-5x11.pdf",
            "name": "English"
          },
          {
            "url": "https://www.fbi.gov/wanted/cyber/aleksei-sergeyevich-morenets/morenetsrussian.pdf/@@download/file/morenetsrussian.pdf",
            "name": " "
          }
        ],
        "dates_of_birth_used": [
          "July 31, 1977"
        ],
        "subjects": [
          "Cyber's Most Wanted"
        ],
        "eyes": "brown",
        "field_offices": None,
        "coordinates": [],
        "@id": "https://api.fbi.gov/@wanted-person/3d41d106985e4b558604afbf7538125d"
      }]
    return items

def test_format_data(sample_items_list):
    '''Test function to test the function to download the data and 
    write the data into a file'''

    data = format_data(sample_items_list)
    assert data is not None
    assert 'title' in sample_items_list[0]
    assert 'subjects' in sample_items_list[0]
    assert 'field_offices' in sample_items_list[0]
