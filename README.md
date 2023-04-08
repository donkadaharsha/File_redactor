## CS5293sp23 – Project1

## Name: Harsha Vardhan

## PROJECT DESCRIPTION:
This project aims to redact sensitive information from a text file which has contents from http://www.enron-mail.com/. All the sensitive information such as names, address, gender, dates and phone numbers are redacted when a file is passed as an argument to run this program. A unicode character is used to replace and hide the sensitive information. After redaction, statistics of redacted data is stored in stats file and can be seen in the output. 

## How to install

Installation of Spacy:  pipenv install Spacy
Installation of en_core_web_sm: pipenv run python -m spacy download en_core_web_sm
Installation of pytest: pipenv install pytest

## How to run
Run the program:
pipenv run python redactor.py --input '*.txt' --names --dates --phones --genders --address --output 'files/' --stats stderr
# Pass stdout or file instead of stderr for output in console/file respectively.

Run the pytests: 
pipenv run python -m pytest

# Video

https://user-images.githubusercontent.com/114453047/230698915-5bf21b54-6f1b-4aa2-863b-2ec12188012e.mp4

## FUNCTIONS

names(doc)
This function takes the data input and matches if the data belongs to 'PERSON' or 'ORG' or 'NORP'. If found, it will store those words in redacted_names list and returns the document and list.

dates(doc)
This function takes the data input and matches if the data belongs to 'DATE'. If found, it will store those words in redacted_dates list and returns the document and list.

phones(doc)
This function takes the data input and matches against the given regex pattern. If found, it will store those words in redacted_phoneNums list and returns the document and list.

genders(doc)
This function takes the data input and matches against the given regex pattern and adds those to GENDER matcher. If found, it will store those words in redacted_gender list and returns the document and list.

address(doc)
This function takes the data input and matches if the data belongs to 'GPE' or 'LOC'. If found, it will store those words in redacted_address list and returns the document and list.

textToUnicode(result,doc)
This function is used to convert all the words found from the above functions to its corresponding unicode full-block characters. 

statistics(result)
This function shows the statistics, i.e, the count of the redacted words from each category - names, genders, address, phone, dates. 

In redactor.py, it reads the arguments using parser and calls all the functions from main.py based on the arguments provided. It also creates the directory for the output files to be stored.  

# Pytest Functions

test_names.py
This file is used to test the names(doc) function from main.py. It verifies the functionality of this method by extracting names and asserting to check if it belongs to person or org or norp.

test_dates.py
This file is used to test the dates(doc) function from main.py. It verifies the functionality of this method by extracting dates and asserting to check if it belongs to DATE category.

test_genders.py
This file is used to test the genders(doc) function from main.py. It verifies the functionality of this method by extracting genders and storing in a list. After that, it asserts the genders to check if it belongs to the gender category which is defined by the regex pattern in gender(doc) function.


test_address.py
This file is used to test the address(doc) function from main.py. It verifies the functionality of this method by extracting addresses and asserting to check if it belongs to GPE or LOC.


test_phones.py
This file is used to test the phones(doc) function from main.py. It verifies the functionality of this method by extracting phone numbers and storing in a list. After that, it asserts the phone numbers to check if it belongs to the phone number category which is defined by the regex pattern in phones(doc) function.

## Bugs

- I have used Spacy model to redact all the sensitive information which in few cases might not redact accurately. As this model doesnot have high accuracy.
- Some parts of the text `which isn't an address is considered as an address because it is matching with GPE category.
- Sometimes, the spacy model is identifying Cc or Bcc as 'Names' and redacting it. 

## Assumptions

- Assuming that gender will only be among {He, His, Him ,Man, Male, Men, brother, Mr, Uncle, Father, She, Women, Her/Hers, Woman, Sister, Female, Aunt, Mrs, Mother, Ms, Wife, Husband, Daughter, Son, Grandmother, Grandfather, Granddaughter, Grandson, Nephew, Neice}
