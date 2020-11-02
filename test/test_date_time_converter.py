import pytest
from src.date_time_converter import date_time

@pytest.mark.parametrize("input, expected, note",
    [("01.01.2000 00:00", "1 January 2000 year 0 hours 0 minutes", "Somebody was born") ])
def test_date_time_converter(input, expected, note):
    assert date_time(input) == expected, note
