import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://data.london.gov.uk/download/recorded_crime_summary/268c37c6-9022-4130-8e43-7bb41ee89f2d/MPS%20Borough%20Level%20Crime%20%28most%20recent%2024%20months%29.csv'

    london_crimes_dtypes = {
        'MajorText':str,
        'MinorText':str,
        'LookUp_BoroughName':str,
        '202202': pd.Int64Dtype(),
        '202203': pd.Int64Dtype(),
        '202204': pd.Int64Dtype(),
        '202205': pd.Int64Dtype(),
        '202206': pd.Int64Dtype(),
        '202207': pd.Int64Dtype(),
        '202208': pd.Int64Dtype(),
        '202209': pd.Int64Dtype(),
        '202210': pd.Int64Dtype(),
        '202211': pd.Int64Dtype(),
        '202212': pd.Int64Dtype(),
        '202301': pd.Int64Dtype(),
        '202302': pd.Int64Dtype(),
        '202303': pd.Int64Dtype(),
        '202304': pd.Int64Dtype(),
        '202305': pd.Int64Dtype(),
        '202306': pd.Int64Dtype(),
        '202307': pd.Int64Dtype(),
        '202308': pd.Int64Dtype(),
        '202309': pd.Int64Dtype(),
        '202310': pd.Int64Dtype(),
        '202311': pd.Int64Dtype(),
        '202312': pd.Int64Dtype(),
        '202401': pd.Int64Dtype()
        }

    return pd.read_csv(url,sep=",",dtype=london_crimes_dtypes)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
