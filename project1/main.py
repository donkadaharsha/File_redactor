import spacy
from spacy.matcher import Matcher
import re
nlp = spacy.load("en_core_web_sm")

# Find names to be redacted
def names(doc):
    doc = nlp(doc)
    redacted_names = []
    for ent in doc.ents:
        if ent.label_ in ['PERSON', 'ORG', 'NORP']:
            redacted_names.append(ent.text)
    return doc, redacted_names

# Find dates to be redacted
def dates(doc):
    doc = nlp(doc)
    redacted_dates=[]
    for token in doc.ents:
        if token.label_ == "DATE":
            redacted_dates.append(token.text)
    return doc,redacted_dates

# Find Phones to be redacted
def phones(doc):
    redacted_phoneNums=[]
    phone_pattern=re.findall(r'(?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', doc)
    for phone in phone_pattern:
        redacted_phoneNums.append(phone)
    return doc,redacted_phoneNums

# Find genders to be redacted
def genders(doc):
    doc = nlp(doc)
    gender_pattern = [{"TEXT": {"REGEX": "^[hH]e$|^[hH]is$|^[hH]im$|^[mM]an$|^[mM]ale$|^[mM]en$|^[bB]rother$|^[mM]r$|^[uU]ncle$|^[fF]ather$|^[sS]he$|^[wW]omen$|^[hH]ers?$|^[wW]oman$|^[sS]ister$|^[fF]emale$|^[aA]unt$|^[mM]rs$|^[mM]other$|^[mM]s$|^[wW]ife$|^[hH]usband$|^[dD]aughters?$|^[sS]on$|^[Gg]randmother$|^[Gg]randfather$|^[Gg]randdaughter$|^[Gg]randson$|^[Nn]iece$|^[Nn]ephew$"}}]
    matcher = Matcher(nlp.vocab)
    matcher.add("GENDER", [gender_pattern])
    matches = matcher(doc)
    redacted_gender=[]
    for match_id, start, end in matches:
        span = doc[start:end] 
        redacted_gender.append(span.text)
    return doc,redacted_gender

# Find address to be redacted
def address(doc):
    nlp_doc = nlp(doc)
    redacted_address=[]
    for token in nlp_doc.ents:
        if token.label_ == "GPE" or token.label_ == "LOC":
            redacted_address.append(token.text)
    return doc, redacted_address

# Replaces all the found names, phones, address, dates, genders with the corresponding unicode characters
def textToUnicode(result,doc):
    unic_char = '\u2588'
    redacted_list=[]
    for key,val in result.items():
        redacted_list+=val
    for i in redacted_list:
        i= r'\b' + i + r'\b'
        doc=re.sub(i,unic_char*len(i),doc)
    return doc

# Gives the statistics of the redacted data.
def statistics(result):
    redacted=""
    for key,val in result.items():
        redacted +="{} redacted from this file are {} \n".format(key,len(val))
    return redacted