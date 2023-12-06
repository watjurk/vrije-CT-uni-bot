import compare
import inquiry
import unilife
# imports the first question from the defined code of questions
from first_question import FirstOpenQuestionResponse, first_open_question
from format import USER_PREFIX, bot_format


def main():
    print(bot_format("Hello I am your university bot assistant."))  # presents the user with the first message from the Bot
    subject_chosen, user_response = first_open_question()  # presents the user with the first question to ask
    match subject_chosen:
        case FirstOpenQuestionResponse.Studying:
            studying_path(user_response)
        case FirstOpenQuestionResponse.Sports:
            sports_path(user_response)
        case FirstOpenQuestionResponse.Activities:
            activities_path(user_response)


def studying_path(user_response_to_first_question: str):
    is_struggling = False

    # Skip this detection if there's a negation word. Then we cannot be sure.
    if not compare.contains_negation_word(user_response_to_first_question):
        struggling_keywords = ["struggling", "struggle"]  # TODO: More keywords!
        if compare.contains_exact(user_response_to_first_question, struggling_keywords):
            is_struggling = True

    if is_struggling == True:
        print(bot_format("It seems like you are struggling with something"))
    else:
        print(bot_format("Are you struggling with something?"))
        is_struggling = inquiry.confirm()

    if is_struggling:
        studying_struggling_path(user_response_to_first_question)
    else:
        studying_not_struggling_path()


def studying_struggling_path(user_response_to_first_question: str):
    wants_to_share = False

    # Skip this detection if there's a negation word. Then we cannot be sure.
    if not compare.contains_negation_word(user_response_to_first_question):
        share_keywords = ["share"]  # TODO: More keywords!
        if compare.contains_exact(user_response_to_first_question, share_keywords):
            wants_to_share = True

    if wants_to_share == True:
        print(bot_format("It seems like you would like to share you struggles with other students."))
    else:
        print(bot_format("Would you like to share you struggles with other students?"))
        wants_to_share = inquiry.confirm()

    if wants_to_share:
        print(bot_format("I will suggest seeking out a study group."))
    else:
        print(bot_format("I will suggest seeking out the student advisor."))


def studying_not_struggling_path():
    print(bot_format("From what I can tell you are not struggling with anything."))
    print(bot_format("If you need any further assistance you can contact the Student Desk at: studentdesk@vu.nl"))
    print(bot_format("Be sure to include your student number!"))


def sports_path(user_response_to_first_question: str):
    print(bot_format("Do you have a specific sport in mind or you are looking for something new?"))
    user_choice = inquiry.checkbox(["Specific sport", "Something new"])
    if user_choice == 0:
        sports_specific_path(user_response_to_first_question)
    else:
        sports_something_new_path(user_response_to_first_question)


def sports_specific_path(user_response_to_first_question: str):
    def print_sport_available_message():
        print(bot_format("Great this specific sport is available at the university."))
        print(bot_format("You can sign-up on the University Sports Centre website: sportcentrumvu.nl"))

    if not compare.contains_negation_word(user_response_to_first_question):
        if compare.contains_exact(user_response_to_first_question, unilife.unilife_sports):
            print_sport_available_message()

    print(bot_format("Which specific sport you have in mind?"))
    user_response = input(USER_PREFIX).lower().strip()
    if user_response in unilife.unilife_sports:
        print_sport_available_message()
    else:
        print(bot_format("Unfortunately this specific sport is not available at the university, sorry."))


def sports_something_new_path(user_response_to_first_question: str):
    # TODO: Make this when they create the follow-up question(s)
    pass


def activities_path(user_response_to_first_question: str):
    interested_in_upcoming = False
    wants_to_join_association = False
    if not compare.contains_negation_word(user_response_to_first_question):
        upcoming_keywords = ["upcoming"]
        if compare.contains_exact(user_response_to_first_question, upcoming_keywords):
            interested_in_upcoming = True

        join_association_keywords = ["join", "association"]
        if compare.contains_exact(user_response_to_first_question, join_association_keywords):
            wants_to_join_association = True

    if (wants_to_join_association and interested_in_upcoming) or (not wants_to_join_association and not interested_in_upcoming):
        print(bot_format("Are you interested in upcoming events or do you want to join an association?"))
        user_choice = inquiry.checkbox(["Upcoming events", "Joining an association"])
        if user_choice == 0:
            interested_in_upcoming = True
            wants_to_join_association = False
        else:
            interested_in_upcoming = False
            wants_to_join_association = True

    if interested_in_upcoming:
        activities_upcoming_path()

    if wants_to_join_association:
        activities_join_association()


def activities_upcoming_path():
    events = []
    for event in unilife.unilife_events:
        events.append((event, unilife.time_to_event(event)))
    events = sorted(events, key=lambda e: e[1])

    print(bot_format("There are some upcoming events."))
    for i in range(3):
        print(bot_format(events[i][0]))

    print(bot_format("I am sure you will enjoy all of them!"))


def activities_join_association():
    # TODO: Make this when they create the follow-up question(s)
    pass


main()


# I need to study
# I need help with studying
# I need to study football
# I need to play football
# I am having problems concentrating
# I need to go to an event
# what’s happening in amsterdam this weekend? - activities
# are there any sports event this week? - sport
# can you help me find a study spot? - study
# I'm studying the history of soccer for my class project - study
# I’m researching different team-building activities for my work - study
# want to improve my python coding and also join a volleyball league - ???
# I need advice on balancing my studies with my badminton training - study
