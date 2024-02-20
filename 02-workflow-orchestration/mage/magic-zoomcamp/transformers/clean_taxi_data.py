if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    # Remove rows where the passenger count is equal to 0 or the trip distance is equal to zero.
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]


    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date.
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # Rename columns in Camel Case to Snake Case, e.g. VendorID to vendor_id.
    data = data.rename(columns = {'VendorID': 'vendor_id', 'RatecodeID': 'rate_code_id', 'PULocationID': 'pu_location_id', 'DOLocationID': 'do_location_id'})

    print(data['vendor_id'].unique())
    return data


@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'

@test
def test_column_renamed(output, *args) -> None:
    assert 'vendor_id' in output.columns, 'VendorID columns was not renamed'

@test
def test_rides_with_zero_passengers(output, *args) -> None:
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'

@test
def test_rides_with_zero_distance(output, *args) -> None:
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero distance'

