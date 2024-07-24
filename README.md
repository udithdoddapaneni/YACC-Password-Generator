# Password Generator



## Overview:

A simple application that generates password for the user. 


## Actions:

The application will generate password based on some rules.

The rules are:-
The length of the password must be between 12 and 18 (inclusive)
There should be at least one uppercase character, one lowercase character, one symbol and one digit in the password

The length of the password and how many uppercase, lowercase, symbols, digits and their positions must be determined randomly. 

Inbuilt random number generators should not be used in the final version

## Output:

A password which is hard to guess


## Technologies used:

Just basic python is enough to make the generator. For the user interface we used streamlit.

## Important tasks:

1) Making a pseudo-random number generator that’s as close as to a real random number generator. For example we know that the more number of times we toss a coin in real life the more the probability of getting a head appears to converge to 0.5. 
	
	More information of how this works here:
	https://www.freecodecamp.org/news/random-number-generator/
	https://www.math.arizona.edu/~tgk/mc/book_chap3.pdf


2) The user interface


## How to run
### Prerequisites
The necessary packages for running the scripts are mentioned in the requirements.txt file.
```
pip install -r requirements.txt
```
Custom packages are present inside _CustomRandom_ folder

### Run the application
To run the following command in terminal to open the interface 
```
streamlit run Interface.py
```
