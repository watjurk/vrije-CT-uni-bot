from typing import List, Tuple

import compare
from format import USER_PREFIX, bot_format


def keywords(keywords_per_topic: List[List[str]]) -> Tuple[List[int], str]:
    response = input(USER_PREFIX)
    similarity_ratios = []
    for keywords in keywords_per_topic:
        print(compare.average_similarity_ratio(response, keywords), compare.max_similarity_ratio(response, keywords))
        similarity_ratio = (compare.average_similarity_ratio(response, keywords) + compare.max_similarity_ratio(response, keywords)) / 2
        similarity_ratios.append(similarity_ratio)
    return (similarity_ratios, response)


def checkbox(options: List[str]) -> int:
    options = list(map(lambda x: x.lower(), options))
    while True:
        for i, option in enumerate(options):
            print(f"    {i+1}) {option}")

        response = input(USER_PREFIX).lower()
        for i, option in enumerate(options):
            if response == option or response == str(i + 1):
                return i

        print(bot_format("Pease select a correct option."))


def confirm() -> bool:
    while True:
        confirm_response = input(USER_PREFIX + "(Yes/No): ").lower().strip()
        if confirm_response == "yes" or confirm_response == "y":
            return True
        if confirm_response == "no" or confirm_response == "n":
            return False

        print(bot_format("Pease respond with Yes or No."))
