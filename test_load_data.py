import pandas as pd
import os
from choose_museum import read_data, PATH

def test_data_exists():

    assert os.path.exists(PATH)


def test_load_data():
    df = read_data()
    assert not df.empty
    assert "latitude" in df.columns
