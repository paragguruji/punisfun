# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 23:30:42 2016

@author: Parag
"""

import os
import json
from nltk.corpus import cmudict


def mapPronounciationToWords():
    """Returns a dict with each unique pronounciation in the CMUdict as a key
        and list of words coressponding to it as the coressponding value
    """
    wordToPronounciationMap = cmudict.dict()
    pronounciationToWordmap = {}
    for w in wordToPronounciationMap:
        for p in wordToPronounciationMap[w]:
            s = " ".join(p)
            if s not in pronounciationToWordmap:
                pronounciationToWordmap[s] = []
            pronounciationToWordmap[s].append(w)
    return pronounciationToWordmap


def dumpToJsonFile(obj, filename):
    """Dumps given object 'obj' to a json file named as the string 'filename'
        and stored in the 'data' folder of this project.

        Warning: Assumption for this function to work correctly is that the
        current working directory is the root directory of the repository.
    """
    data_dir = os.path.join(os.getcwd(), 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    path = os.path.join(data_dir, filename)
    with open(path, "w") as f:
        json.dump(obj, f)
