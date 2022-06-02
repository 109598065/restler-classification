import re


def compound_word_processing(word):
    snake_case_words = re.sub(r'(?<!^)(?=[A-Z])', '_', word).lower()
    split_words = snake_case_words.split('_')
    split_words.append(snake_case_words)
    return split_words
