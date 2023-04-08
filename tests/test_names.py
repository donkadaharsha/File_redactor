import spacy
from project1 import main
from spacy.tokens import Doc
import pytest

@pytest.fixture
def nlp_model():
    nlp = spacy.load("en_core_web_sm")
    return nlp

# Define the test function
def test_names():
    input_text = "Joseph works in Apple Corp."
    
    # Call the names() function with the input text
    doc, redacted_names = main.names(input_text)
    
    # Assertions
    assert isinstance(doc, Doc)
    assert isinstance(redacted_names, list)
    assert len(redacted_names) > 0
    assert 'Joseph' in redacted_names
    assert 'Apple Corp.' in redacted_names
    assert 'PERSON' in [ent.label_ for ent in doc.ents]
    assert 'ORG' in [ent.label_ for ent in doc.ents]
