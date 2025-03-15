
def get_word_count(file_contents):
    return len(file_contents.split())


def get_char_count(file_contents):
    result_dict = {}
    for char in file_contents:
        lower_case_char = char.lower()
        if lower_case_char not in result_dict.keys():
            result_dict[lower_case_char] = 1
        else:
            result_dict[lower_case_char] += 1
    return result_dict