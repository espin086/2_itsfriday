import pandas as pd
import pytest
import pull_indeed


def test_dataframe_not_empty():
    df = pd.DataFrame()
    # df = pull_indeed.scrape_indeed('Los Angeles','Data Scientist')
    assert df.empty is False, 'dataframe is empty'


test_dataframe_not_empty()
