# Jack C. Cook
# 5/12/20

import pandas as pd


def save_files(outputfolder, merged):
    """

    :param outputfolder: The folder where all of the merged files will be saved
    :param merged: The merged dictionaries
    :return: None
    """

    keys = list(merged.keys())

    for i in range(len(keys)):
        df = pd.DataFrame(merged[keys[i]])
        df = df.loc[:, ~df.columns.str.match('Unnamed')]
        path = outputfolder + '/' + keys[i]
        df.to_excel(path)
