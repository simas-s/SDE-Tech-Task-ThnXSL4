from etl_pipeline.api import get_daily_weather


def example_test_func():
    """
    This is a placeholder function to demonstrate unit test structure. The actual functions for this ETL pipeline are
    all based on interacting with the OpenWeather and GCP APIs. To separate testable logic from API calls we can either
    separate them into separate functions or Mock the API calls, in this case there is almost no transformation logic
    to test hence this funtion serves as an example of what tests should look like.
    """
    input_data = []
    expected_output = []
    actual_output = get_daily_weather(input_data)
    assert expected_output == actual_output
