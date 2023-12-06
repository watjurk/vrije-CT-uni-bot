from enum import Enum
from typing import Tuple

import inquiry  # imports the
from format import bot_format


class FirstOpenQuestionResponse(Enum):  # define a class which represents the user's response to first question
    Studying = 0
    Sports = 1
    Activities = 2

    def __str__(self):
        match self.value:
            case 0:
                return "Studying"
            case 1:
                return "Sports"
            case 2:
                return "Social Activities"


def first_open_question() -> Tuple[FirstOpenQuestionResponse, str]:
    print(bot_format("What can I help you with?"))

    similarity_ratios, user_response = inquiry.keywords([keywords_for_studying, keywords_for_sports, keywords_for_activities])
    print(similarity_ratios) # TODO: Remove this print
    max_similarity_ratio = max(similarity_ratios)

    firstQuestionResponse: FirstOpenQuestionResponse | None = None
    if max_similarity_ratio < 20:
        print(bot_format("Sorry I was unable to determine what should I help you with."))
        print(bot_format("Please choose what are you interested in:"))
        option_index = inquiry.checkbox(["studying", "sport", "social Activities"])
        firstQuestionResponse = FirstOpenQuestionResponse(option_index)
    else:
        similarity_ratios_index = similarity_ratios.index(max(similarity_ratios))
        firstQuestionResponse = FirstOpenQuestionResponse(similarity_ratios_index)
        print(bot_format(f"It seems like you are interested in {firstQuestionResponse}, is that correct?"))
        if inquiry.confirm():
            return firstQuestionResponse, user_response
        else:
            return first_open_question()

    return firstQuestionResponse, user_response


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
