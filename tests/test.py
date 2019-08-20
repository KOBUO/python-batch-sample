import pytest
from pandas import DataFrame, Series


@pytest.fixture(scope="module")
def calculate_pandas_create_at():
    import calculate_pandas
    return calculate_pandas


def test_sample(calculate_pandas_create_at):
    df = DataFrame({'machine_id': ["BD0084", "BD0084", "BD0084"],
                    'date': ["2018-10-04", "2018-10-05", "2018-10-06"],
                    'angle': [0.0, 20.0, 40.0]})
    actual = calculate_pandas_create_at.create_at(df)
    assert df.equals(actual[['machine_id', 'date', 'angle']])
    expected: Series = Series([0.0, 20.0, 20.0])
    assert expected.equals(actual['angle_diff'])


@pytest.mark.parametrize(
    "x, y", [
        ("aaa", "aaa"),
        ("bbb", "bbb")
    ]
)
def test_1(x, y):
    assert x == y
