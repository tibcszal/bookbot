
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


def sort_on(dictionary):
    return dictionary['count']


def build_sorted_list(char_dict):
    result_list = []
    for entry in char_dict.keys():
        into_list = {
            "char": entry,
            "count": char_dict[entry]
        }
        result_list.append(into_list)
    result_list.sort(reverse=True, key=sort_on)
    return result_list