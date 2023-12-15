from typing import List

from thefuzz import fuzz  # Importing fuzz from thefuzz library for string matching.


def average_similarity_ratio(
    target_string: str, keywords: List[str]
) -> float:  # Function to calculate the average similarity ratio between a target string and a list of keywords.
    ratio = 0  # Initialize the ratio variable to accumulate similarity scores.

    # Iterating through each keyword in the list.
    for keyword in keywords:
        ratio += fuzz.token_sort_ratio(
            target_string, keyword
        )  # Increasing the ratio by the similarity score of the target string and the current keyword.

    return ratio / len(keywords)  # Returning the average ratio by dividing the accumulated ratio by the number of keywords.


def max_similarity_ratio(
    target_string: str, keywords: List[str]
) -> float:  # Function to find the maximum similarity ratio between a target string and a list of keywords.
    ratio = 0  # Initialize the ratio variable to track the highest similarity score.

    # Iterating through each keyword in the list.
    for keyword in keywords:
        ratio = max(
            fuzz.token_sort_ratio(target_string, keyword), ratio
        )  # Updating the ratio with the maximum value between the current ratio and the new similarity score.

    return ratio  # Returning the highest ratio found.


def contains_negation_word(input: str) -> bool:  # Function to check if the input contains any negation word.
    negation_words = ["not"]  # List of negation words to check against.
    return contains_exact(input, negation_words)  # Calling a function to check if the input contains any of the negation words.


def contains_exact(input: str, keywords: List[str]) -> bool:  # Function to check if the input string contains any of the defined keywords exactly
    # Iterating through each keyword in the list.
    for keyword in keywords:
        if keyword in input:  # Checks if the keyword is found in the input--> return True.
            return True
        else:  # If none of the keywords are found, return False.
            return False
