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

	IMPLEMENTATION OF MERSENNE TWISTER
	
	- Initialization: The MersenneTwister class is initialized with a seed (default is 5489). The seed determines the starting point for the random number sequence.It initializes internal state variables, including an array MT of length n (624), to store the state of the generator. Various constants and masks are also set.
	- Twisting: The twist method updates the internal state array MT to generate the next n values in the sequence. This involves a series of bitwise operations and shifts, mixing the current state to produce new values.
	- Extracting Numbers: The extract_number method retrieves a tempered value from the MT array, ensuring the generator produces different numbers over time. It applies additional bitwise transformations to the state.
	- Random Integer Generation: The selfimplemented randint method generates a random integer within a specified range [a, b] using the extracted numbers.
	- Seeding with Current Time: The generator is seeded with the current timestamp, making it unpredictable for each run.


2) The user interface


## How to Run
### Download Repository
- Click on code
- Download as zip
- Extract the zip file
  
### Install Dependencies
The necessary packages for running the scripts are mentioned in the requirements.txt file.
```
pip install -r requirements.txt
```
Custom packages are present inside _CustomRandom_ folder

### Run the Application
To run the following command in terminal to open the interface 
```
streamlit run Interface.py
```
