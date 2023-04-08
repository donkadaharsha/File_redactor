import spacy
from project1 import main
from spacy.tokens import Doc
from spacy.matcher import Matcher
import pytest

@pytest.fixture
def nlp_model():
    nlp = spacy.load("en_core_web_sm")
    return nlp

# Define the test function
def test_genders(nlp_model):
    input_text = "He goes for a walk. She goes for cycling."
    
    # Call the genders() function with the input text
    doc, redacted_genders = main.genders(input_text)
    
    # Assertions
    assert isinstance(doc, Doc)
    assert isinstance(redacted_genders, list)
    assert len(redacted_genders) > 0
    assert 'He' in redacted_genders
    assert 'She' in redacted_genders

