from typing import List

from thefuzz import fuzz


def average_similarity_ratio(target_string: str, keywords: List[str]) -> float:
    ratio = 0

    for keyword in keywords:
        ratio += fuzz.token_sort_ratio(target_string, keyword)

    return ratio / len(keywords)


def max_similarity_ratio(target_string: str, keywords: List[str]) -> float:
    ratio = 0

    for keyword in keywords:
        ratio = max(fuzz.token_sort_ratio(target_string, keyword), ratio)

    return ratio


def contains_negation_word(input: str) -> bool:
    negation_words = ["not"]
    return contains_exact(input, negation_words)


def contains_exact(input: str, keywords: List[str]) -> bool:
    for keyword in keywords:
        if keyword in input:
            return True
    return False
