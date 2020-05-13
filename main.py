# Jack C. Cook
# Tuesday, May 12, 2020

import sys, getopt
import pymerge.merge as pym


def main(argv):
    inputfolders = []
    outputfolder = ''
    try:
        input_folders = False
        output_folder = False
        for i in range(len(argv)):
            if argv[i] == '-i':  # reading the input folders
                input_folders = True
                continue
            if argv[i] == '-o':
                input_folders = False
                output_folder = True
                continue

            if input_folders is True:
                inputfolders.append(argv[i])
            elif output_folder is True:
                outputfolder = argv[i]

            if input_folders is False and output_folder is True:  # we only want one output folder
                break
    except:
        print('main.py -i <input_folder_1> <input_folder_2 ...> -o <output_folder>')

    pym.merge_folders(inputfolders, outputfolder)


if __name__ == '__main__':
    main(sys.argv[1:])
