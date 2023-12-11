from enum import Enum
from typing import Tuple

import inquiry  # Importing the inquiry module for user interaction

from format import bot_format  # Importing formatting functions for consistent user interface

class FirstOpenQuestionResponse(Enum):  # Defining a class for first open question
    Studying = 0
    Sports = 1
    Activities = 2

    # String representation of the classes
    def __str__(self):
         match self.value:
            case 0:  #If the value is 0, it represents "Studying
                return "Studying"
            case 1:  #If the value is 1, it represents "Sports"
                return "Sports" 
            case 2:  #If the value is 2, it represents "Social Activities"
                return "Social Activities"

# Function to handle the first open question to the user
def first_open_question() -> Tuple[FirstOpenQuestionResponse, str]:
    print(bot_format("What can I help you with?"))                #Presents the initial question to the user

    similarity_ratios, user_response = inquiry.keywords([keywords_for_studying, keywords_for_sports, keywords_for_activities]) # Analyzing user response based on 3 different categories of predefined keywords
    print(similarity_ratios)  #TODO: #Remove later

    max_similarity_ratio = max(similarity_ratios)  #Determines the highest similarity ratio

    firstQuestionResponse: FirstOpenQuestionResponse | None = None
    if max_similarity_ratio < 20:   #if the matching % <20 then runs the following code 
        print(bot_format("Sorry, I was unable to determine what I should help you with"))  #if the similarity is less than 20 then prints the message
        print(bot_format("Please choose what you are interested in:"))    #gives the user 3 options to select from
        option_index = inquiry.checkbox(["studying", "sport", "social Activities"])
        firstQuestionResponse = FirstOpenQuestionResponse(option_index)  # Setting the response based on user's choice
    else:
        similarity_ratios_index = similarity_ratios.index(max(similarity_ratios)) #Finds the index of the highest similarity ratio
        firstQuestionResponse = FirstOpenQuestionResponse(similarity_ratios_index)  #Sets the response based on the highest similarity ratio
        # Confirming with the user if the detected interest is correct
        print(bot_format(f"It seems like you are interested in {firstQuestionResponse}, is that correct?"))
        if inquiry.confirm(): # Confirming the interest with the user
            return firstQuestionResponse, user_response
        else:                 # Re-asking the question if the user denies the detected interest
            return first_open_question()
        
    return firstQuestionResponse, user_response # Returning the determined response and the original user response

# Keywords for analyzing user response for studying related queries
keywords_for_studying = [
    "school work",
    "learn",
    "studying",
    "study",
    "practice",
    "learn",
    "exam",
    "share with",
    "student advisor",
    "practical information",
    "concentrating",
    "balancing studies"
    "my studies"
]

# Keywords for analyzing user response for sports related queries
keywords_for_sports = [
    "play",
    "athletics",
    "sport",
    "working out",
    "sport opportunities",
    "sports centre",
    "new sport",
    "gym",
    "healthy",
    "hockey",
    "football",
    "basketball",
    "Tennis",
    "Badminton",
    "padel",
    "Cricket",
    "Golf",
    "soccer",
    "rugby",
    "volleyball",
    "sport event",
    "swimming",
    "zumba",
    "karate",
    "yoga",
    "waterpolo",
    "aikido",
    "competition",
    "fitness",
    "Poetry pals",
    "debate club",
    "poetry pals",
    "painting and poetry",
    "sustainibility",
    "animal",
    "bunch of backpackers",
    "kayaking",
    "pole dance",
    "Animal shelter volunteers",
]

# Keywords for analyzing user response for social activities related queries
keywords_for_activities = [
    "social activities",
    "student association",
    "asociation",
    "event",
    "upcoming",
    "join an association",
    "student council",
    "volunteering",
    "party",
    "club",
    "arts",
    "international",
    "debate",
    "environment and sustainability",
    "animals",
    "nature",
    "languages",
    "Breakfast",
    "lunch",
    "dinner",
    "trip",
    "trips",
    "parties",
    "dance",
    "music",
]
