# Jack C. Cook
# 5/12/20

import pandas as pd


def merge_files(to_merge_read):
    """
    Merge the files into one file, all with sorted headers
    :param to_merge_read: the dictionary created by the function read_in_files
    :return: a dictionary of the merged file contents
    """
    keys = list(to_merge_read.keys())
    merged = {key: None for key in keys}

    for i in range(len(keys)):
        numbers = {}
        words = {}
        for j in range(len(to_merge_read[keys[i]])):
            nested_keys = list(to_merge_read[keys[i]][j].keys())
            for k in range(len(nested_keys)):
                if type(nested_keys[k]) is int or type(nested_keys[k]) is float:
                    numbers[str(nested_keys[k])] = to_merge_read[keys[i]][j][nested_keys[k]]
                elif nested_keys[k].isnumeric():
                    numbers[nested_keys[k]] = to_merge_read[keys[i]][j][nested_keys[k]]
                else:
                    words[nested_keys[k]] = to_merge_read[keys[i]][j][nested_keys[k]]
        numbers_keys_sorted = sorted(list(numbers.keys()), key=float)
        sorted_numbers = {key: numbers[key] for key in numbers_keys_sorted}
        words_keys_sorted = sorted(list(words.keys()), key=str.lower)
        sorted_words = {key: words[key] for key in words_keys_sorted}
        merged_dict = {**sorted_words, **sorted_numbers}
        merged[keys[i]] = merged_dict

    return merged


def read_in_files(to_merge_dict):
    """
    Read the files in using pandas, consider dataframes as dictionaries
    :param to_merge_dict: the dictionary to merge
    :return: the to merged as read dictionaries
    """
    keys = list(to_merge_dict.keys())
    to_merge_read = {key: [] for key in keys}

    for i in range(len(keys)):
        for j in range(len(to_merge_dict[keys[i]])):
            df = pd.read_excel(to_merge_dict[keys[i]][j] + '/' + keys[i])
            dnary = df.to_dict('list')
            to_merge_read[keys[i]].append(dnary)
    return to_merge_read


def combine_merge_dict(to_merge_dict):
    to_merge_read = read_in_files(to_merge_dict)
    merged = merge_files(to_merge_read)
    return merged