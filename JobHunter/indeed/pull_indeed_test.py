"""
Testing that pull_indeed function worked properly
"""

import pull_indeed

DF = pull_indeed.scrape_indeed('Los Angeles', 'Data Scientist')


def test_dataframe_not_empty():
    """
    Data frame must not be all null or missing values
    """
    assert DF.empty is False, 'dataframe is empty'


def test_each_column_has_data():
    """
    Each column in the dataframe must have data
    """
    for column in DF.columns:
        assert DF[column].empty is False,\
            'column {0} in data is empty'.format(column)


if __name__ == "__main__":
    test_dataframe_not_empty()
    test_each_column_has_data()
