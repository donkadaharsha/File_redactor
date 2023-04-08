import re
import pytest
from project1 import main

# Define the test function
def test_phones():
    input_text = "My phone number is +1 123-456-7890. Call me at (975) 654-5213"
    
    # Call the phones() function with the input text
    doc, redacted_phoneNums = main.phones(input_text)
    
    # Assertions
    assert isinstance(doc, str)
    assert isinstance(redacted_phoneNums, list)
    assert '(975) 654-5213' in redacted_phoneNums
    assert '123-456-7890' in redacted_phoneNums
