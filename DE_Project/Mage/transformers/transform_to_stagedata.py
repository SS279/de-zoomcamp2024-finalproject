if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    data.columns = (data.columns
                    .str.lower()
                    .str.replace('majortext','crime_category')
                    .str.replace('minortext','crime_type')
                    .str.replace('lookup_boroughname','london_boroughname')
                )

    return data
