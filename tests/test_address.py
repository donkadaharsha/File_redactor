from project1 import main
import spacy
from spacy.tokens import Doc
import pytest

@pytest.fixture
def nlp_model():
    nlp = spacy.load("en_core_web_sm")
    return nlp

# Define the test function
def test_address(nlp_model):
    input_text = "My house is located in New York."
    
    # Call the address() function with the input text
    doc, redacted_address = main.address(input_text)
    
    # Assertions
    assert isinstance(doc, str)
    assert isinstance(redacted_address, list)
    assert len(redacted_address) > 0
    assert 'New York' in redacted_address
