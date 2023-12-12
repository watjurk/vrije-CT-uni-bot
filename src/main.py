import compare
import inquiry
import unilife

# Importing necessary modules and functions.
from first_question import FirstOpenQuestionResponse, first_open_question
from format import USER_PREFIX, bot_format


def main():  # Start of the main function
    print(bot_format("Hello I am your university bot assistant."))  # the bot initializes with a greeting from the bot.
    subject_chosen, user_response = first_open_question()  # Collects user response to the first open question.
    # Directing to different paths based on the user's choice.
    match subject_chosen:
        case FirstOpenQuestionResponse.Studying:  # if the user's response is recognized as studying criteria
            studying_path(user_response)  # redirects to the first studying section question
        case FirstOpenQuestionResponse.Sports:  # if the user's response is recognized as sports criteria
            sports_path(user_response)  # redirects to the first sports section question
        case FirstOpenQuestionResponse.Activities:  # if the user's response is recognized as activities criteria
            activities_path(user_response)  # redirects to the first activities section question


def studying_path(user_response_to_first_question: str):  # the path for users interested in studying related queries.
    is_struggling = False  # defining the struggling function false
    if not compare.contains_negation_word(user_response_to_first_question):  # the negative words are taken as the opposite intended meaning
        struggling_keywords = ["struggling", "struggle"]  # defining the struggling keywords
        if compare.contains_exact(user_response_to_first_question, struggling_keywords):  # if sturggling keywords is found then it stated as true
            is_struggling = True

    # Responds based on the detected struggle status.(T/F)
    if is_struggling:  # if the user's response was struggling related then prints the following message
        print(bot_format("It seems like you are struggling with something"))
    else:  # if the user's response didnt have struggling keywords then asks for confirmation as inquiry
        print(bot_format("Are you struggling with something?"))
        is_struggling = inquiry.confirm()

    # Decides next steps based on whether the user is struggling or not.
    if is_struggling:
        studying_struggling_path(user_response_to_first_question)
    else:
        studying_not_struggling_path(user_response_to_first_question)


def studying_struggling_path(user_response_to_first_question: str):  # Path for users who are struggling with studying.
    wants_to_share = False  # pre-defining the wants to share function as false
    # Checks if the user wants to share their struggles.
    if not compare.contains_negation_word(user_response_to_first_question):  # the negative words are taken as the opposite intended meaning
        share_keywords = ["share"]  # checks for defined truggle keywords
        if compare.contains_exact(user_response_to_first_question, share_keywords):  # if sturggling keywords is found then it stated as true
            wants_to_share = True

    # Responds based on whether the user wants to share their struggles.
    if wants_to_share:  # if the user wnats to share was true then the folloing message gets printed
        print(bot_format("It seems like you would like to share your struggles with other students."))
    else:  # if the user wants to share was flase then a confirmation message gets printed
        print(bot_format("Would you like to share your struggles with other students?"))
        wants_to_share = inquiry.confirm()

    # Suggests different solutions based on user's willingness to share.
    if wants_to_share:
        print(bot_format("I will suggest seeking out a study group."))
    else:
        print(bot_format("I will suggest seeking out the student advisor."))


def studying_not_struggling_path(user_response_to_first_question):  # Path for users who are not struggling with studying.
    interested_practical_information = False
    if not compare.contains_negation_word(user_response_to_first_question):
        interested_practical_information_keywords = ["practical", "information"]
        if compare.contains_exact(user_response_to_first_question, interested_practical_information_keywords):
            interested_practical_information = True

    if interested_practical_information:
        print(bot_format("It seems like you are interested in practical information."))
    else:
        print(bot_format("Are you interested in practical information?"))
        interested_practical_information = inquiry.confirm()

    if interested_practical_information:
        print(bot_format("From what I can tell you are not struggling with anything."))
        print(bot_format("If you need any further assistance you can contact the Student Desk at: studentdesk@vu.nl"))
        print(bot_format("Be sure to include your student number!"))
    else:
        print(bot_format("Thanks for using unibot!"))


def sports_path(user_response_to_first_question: str):  # Path for users interested in sports related queries.
    print(
        bot_format("Do you have a specific sport in mind or you are looking for something new?")
    )  # asks user about specific sports path or exploring new sports
    user_choice = inquiry.checkbox(
        ["Specific sport", "Something new"]
    )  # Redirects to specific sports path or exploring new sports based on user choice.
    if user_choice == 0:
        sports_specific_path(user_response_to_first_question)  # If yes the code calls the function of the path for a specific sport.
    else:
        sports_something_new_path(user_response_to_first_question)  # If not the code calls the function for exploring new sports.


def sports_specific_path(user_response_to_first_question: str):  # Path for users who have a specific sport in mind.
    def print_sport_available_message():
        print(
            bot_format("Great this specific sport is available at the university.")
        )  # if the user's mentioned sport is available in the defined list
        print(
            bot_format("You can sign-up on the University Sports Centre website: sportcentrumvu.nl")
        )  # suggests user to go to the university website

    # Checks if the user's mentioned sport is available.
    if not compare.contains_negation_word(user_response_to_first_question):
        if compare.contains_exact(user_response_to_first_question, unilife.unilife_sports):
            print_sport_available_message()
            return

    print(bot_format("Which specific sport you have in mind?"))  # Asks the user for the specific sport they have in mind.
    user_response = input(USER_PREFIX).lower().strip()  # Responds based on whether the mentioned sport is available or not.
    if user_response in unilife.unilife_sports:  # if the user's sport is available in the database then prints the pre-defined message
        print_sport_available_message()
    else:  # if the user''s sport is not available in the database then prints the error message
        print(bot_format("Unfortunately this specific sport is not available at the university, sorry."))


def sports_something_new_path(user_response_to_first_question: str):
    print(bot_format("What type of sport are you interested in?"))
    print(bot_format("Are you looking for team & individual sports or something focused on fitness?"))
    user_choice = inquiry.checkbox(["sports in teams or individual", "sports focused on fitness"])

    def print_sign_up_message():
        print(bot_format("You can sign-up on the University Sports Centre website: sportcentrumvu.nl."))

    if user_choice == 0:
        print(bot_format("Are you interested in individual sports or team sports?"))
        next_user_choice = inquiry.checkbox(["individual sports", "team sports"])
        if next_user_choice == 0:
            print(bot_format("Great! We offer sports like Swimming, Tennis."))
            print(bot_format("These sports are excellent for individual sports and building up endurance."))
            print_sign_up_message()

        else:
            print(bot_format("Good to know! We also provide options like Basketball, Football & Waterpolo."))
            print(bot_format("These activities enhance your leadership skills and teamwork."))
            print_sign_up_message()
    else:
        print(bot_format("Are you interested in fitness activities that you can do individually"))
        print(bot_format("or would you prefer group fitness activities for a more group environment?"))
        next_user_choice = inquiry.checkbox(["individually", "group environment"])
        if next_user_choice == 0:
            print(bot_format("Great! For individual fitness, your options include  aikido, and Karate."))
            print(bot_format("These activities are perfect for you."))
            print_sign_up_message()
        else:
            print(bot_format("Great choice! For group fitness, we offer Zumba and Yoga."))
            print_sign_up_message()


def activities_path(user_response_to_first_question: str):  # Path for users interested in activities.
    interested_in_upcoming = False  # pre-defining the student interested in upcoming events as false
    wants_to_join_association = False  # predefining the student wants to join association function as false
    # Checks if the user is interested in upcoming events or joining an association.
    if not compare.contains_negation_word(user_response_to_first_question):  # checks if the user's response does not have any negative word
        upcoming_keywords = ["upcoming"]  # defined checklist for upcoming word
        if compare.contains_exact(
            user_response_to_first_question, upcoming_keywords
        ):  # if there is an exact match of the keywrod defined then it returns as true
            interested_in_upcoming = True

        join_association_keywords = ["join", "association"]  # defined keywords for joining an association
        if compare.contains_exact(user_response_to_first_question, join_association_keywords):  # checks the response and defined keywords
            wants_to_join_association = True  # if a word is found then it is stated as true

    # Determines the path based on user interest.
    if (wants_to_join_association and interested_in_upcoming) or (not wants_to_join_association and not interested_in_upcoming):
        print(
            bot_format("Are you interested in upcoming events or do you want to join an association?")
        )  # asks user about interest in upcoming events and association joining
        user_choice = inquiry.checkbox(
            ["Upcoming events", "Joining an association"]
        )  # defined keywords for the uqestion about upcoming events/association joining
        if user_choice == 0:  # if there was a match then
            interested_in_upcoming = True  # the user is interested in coming to upcoming events
            wants_to_join_association = False  # the user is not interested in joining an association
        else:
            interested_in_upcoming = False  # the user is not interested in coming to upcoming events
            wants_to_join_association = True  # the user is interested in joining an association

    # Directs to respective paths based on the user's interest.
    if interested_in_upcoming:  # redirects user if he is interested to an upcoming event
        activities_upcoming_path()
    if wants_to_join_association:  # redirects user if he is interested in joining an association
        activities_join_association()


def activities_upcoming_path():  # Path for users interested in upcoming events.
    events = []  # defining an empty set for events
    # Collects and sorts upcoming events.
    for event in unilife.unilife_events:
        events.append((event, unilife.time_to_event(event)))  # adds the events to the set from the defined list of events
    events = sorted(events, key=lambda e: e[1])  # sorts them accordingly for search

    # Displays upcoming events to the user.
    print(bot_format("There are some upcoming events."))
    for i in range(3):
        print(bot_format(events[i][0]))

    print(bot_format("I am sure you will enjoy all of them!"))


def activities_join_association():
    def recommend_association(association_name: str):
        print(bot_format(f"We would recommend: {association_name}"))

    print(bot_format("Would you like to join an association dedicated to sciences/nature or arts/actuality?"))
    user_choice = inquiry.checkbox(["sciences/nature", "arts/actuality"])
    if user_choice == 0:
        print(bot_format("Would you say you're more inclined to scientific debate or are you more interested in adventures and animals? "))
        next_user_choice = inquiry.checkbox(["scientific debate", "adventures and animals"])
        if next_user_choice == 0:
            recommend_association("Students for Sustainability, Science Society.")
        else:
            recommend_association("Animal Shelter Volunteers, Bunch of Backpackers")
    else:
        print(bot_format("Do you look forward to learning something new and engaging in creative activities"))
        print(bot_format("or are you more interested in news and debates?"))
        next_user_choice = inquiry.checkbox(["creative activities", "news and debates"])
        if next_user_choice == 0:
            recommend_association("Poetry Pals / Painting and Pottery, Language Club")
        else:
            recommend_association("International Students Society, Debate Club")


main()  # Initiates the program.
