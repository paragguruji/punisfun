# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 23:30:42 2016

@author: Parag
"""

import os
import json
from nltk.corpus import cmudict


def mapWordToPronunciations(stress=False):
    """Returns a dict with each unique word in the CMUdict as a key
        and list of its pronunciations as the coressponding value

        :arg: stress: bool Flag if the pronunciation stress to be ignored
                      :default: False
    """
    original = cmudict.dict()
    return dict(
        [(w,
          list(set([
              " ".join(p) if stress else
              " ".join(p).replace('0', '').replace('1', '').replace('2', '')
              for p in original[w]])))
         for w in original])


def mapPronunciationToWords(stress=False):
    """Returns a dict with each unique pronunciation in the CMUdict as a key
        and list of words coressponding to it as the coressponding value

        :arg: stress: :bool: Flag if the pronunciation stress to be ignored
                      :default: False
    """
    wordToPronunciationMap = mapWordToPronunciations(stress=stress)
    pronunciationToWordmap = {}
    for w in wordToPronunciationMap:
        for p in wordToPronunciationMap[w]:
            if p not in pronunciationToWordmap:
                pronunciationToWordmap[p] = []
            pronunciationToWordmap[p].append(w)
    return pronunciationToWordmap


def dumpToJsonFile(obj, filename):
    """Dumps given object 'obj' to a json file named as the string 'filename'
        and stored in the 'data' folder of this project.

        Warning: Assumption for this function to work correctly is that the
        current working directory is the parent directory of the root directory
        of this repository.
    """
    data_dir = os.path.join(os.getcwd(), 'punisfun', 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    path = os.path.join(data_dir, filename)
    with open(path, "w") as f:
        json.dump(obj, f)


def readFromJsonFile(filename):
    """Reads the json fie from data dir if exists and returns the dict
        Returns None on failure.

        Warning: Assumption for this function to work correctly is that the
        current working directory is the parent directory of the root directory
        of this repository.
    """
    path = os.path.join(os.path.join(os.getcwd(),
                                     'punisfun',
                                     'data'), filename)
    if os.path.exists(path):
        return json.load(open(path))
    else:
        return None


def getPunPartners(word, w2p=None, p2w=None):
    """Returns a list of such words which can substitute given word to produce
        a homophonic pun

        :arg: word: target word
        :arg: w2p: word-to-pronunciations-map (default: generate on fly)
        :arg: p2w: pronunciation-to-words-map (default: generate on fly)
    """
    word = word.strip().lower()
    if not w2p:
        w2p = readFromJsonFile('w2p.dict')
        if not w2p:
            w2p = mapWordToPronunciations()
    if not p2w:
        p2w = readFromJsonFile('p2w.dict')
        if not p2w:
            p2w = mapPronunciationToWords()
    out = []
    if word in w2p:
        for p in w2p[word]:
            out.extend(p2w[p])
    return sorted(list(set(out)))
