from typing import List, Tuple     
import compare
from format import USER_PREFIX, bot_format

def keywords(keywords_per_topic: List[List[str]]) -> Tuple[List[int], str]:
    response = input(USER_PREFIX) # Asking the user for input and storing the response
    similarity_ratios = []                                                #stores the responses similarity ratio

    # Iterating through each set of keywords in the given list of topics
    for keywords in keywords_per_topic:   
        # Calculating the combined average similarity ratio for the response against the current set of keywords
        similarity_ratio = (compare.average_similarity_ratio(response, keywords) + compare.max_similarity_ratio(response, keywords)) / 2
        # Adding the calculated similarity ratio to the list
        similarity_ratios.append(similarity_ratio)
    
    # Returning the list of similarity ratios and the user's response
    return (similarity_ratios, response)

def checkbox(options: List[str]) -> int:
    # Converting all options to lowercase for consistent comparison
    options = list(map(lambda x: x.lower(), options))

    # Continuous loop until a valid response is received
    while True:
        # Displaying each option with an index for the user to choose from
        for i, option in enumerate(options):
            print(f"    {i+1}) {option}")

        # Getting the user's choice/response and converting it to lowercase
        response = input(USER_PREFIX).lower()

        for i, option in enumerate(options):               # Checking if the response matches any of the options (by text or index)
            if response == option or response == str(i + 1):
                return i                                   # Returning the index of the chosen option
        print(bot_format("Please select a correct option")) #  Asking the user to select a correct option if the input is invalid

def confirm() -> bool: #
    while True:       # Continuous loop until a valid 'Yes' or 'No' response is received
        confirm_response = input(USER_PREFIX + "(Yes/No): ").lower().strip() #Asking the user for a confirmation response

        if confirm_response == "yes" or confirm_response == "y":  # Checking for positive response
            return True   #Returning True if found
        if confirm_response == "no" or confirm_response == "n":   # Checking for negative responses 
            return False  #Returning False if found

        print(bot_format("Please respond with Yes or No"))         # Asking the user to respond correctly if the input is invalid
