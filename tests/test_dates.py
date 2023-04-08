import pytest
from project1 import main
# Define the test function
def test_dates():
    # Input text for testing
    input_text = "My birthday is on March 20, 1996. Today's date is 2023-04-07"
    
    # Call the dates() function with the input text
    doc, redacted_dates = main.dates(input_text)
    
    # Assertions

    assert isinstance(redacted_dates, list)
    assert len(redacted_dates) == 2
    assert 'March 20, 1996' in redacted_dates
    assert '2023-04-07' not in redacted_dates
