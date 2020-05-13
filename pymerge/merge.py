# Jack C. Cook
# 5/12/20

import os
from . import combine
from . import output_merged


def to_merge(inputfolders, file_names):
    """
    Get the information for what needs to be merged
    :param inputfolders: the list of the input folders
    :param file_names: the file names created by the function collect_files
    :return: a dictionary containing the files that will be merged
    """

    to_merge_dict = {}

    for i in range(len(file_names)):
        for j in range(len(file_names[i])):
            keys = list(to_merge_dict.keys())  # get all the files to merge
            if file_names[i][j] not in keys:
                to_merge_dict[file_names[i][j]] = []
            to_merge_dict[file_names[i][j]].append(inputfolders[i])
    return to_merge_dict


def collect_files(inputfolders):
    """
    Collect all of the relevant files, for now only considering xlsx
    :param inputfolders: the path to all of the input folders
    :return: all of the files that are in the input folders
    """

    file_names = []
    for i in range(len(inputfolders)):
        tmp_file_list = []
        for file in os.listdir(inputfolders[i]):
            split_file = file.split('.')
            if split_file[-1] != 'xlsx':
                continue
            tmp_file_list.append(file)
        file_names.append(tmp_file_list)
    return file_names


def merge_folders(inputfolders, outputfolder):
    file_names = collect_files(inputfolders)
    to_merge_dict = to_merge(inputfolders, file_names)
    merged = combine.combine_merge_dict(to_merge_dict)
    output_merged.save_files(outputfolder, merged)
