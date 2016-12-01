# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 17:17:30 2016

@author: Parag
"""

from punisfun.src.pronunciation import getPunPartners
from punisfun.src.util.combinations import base10toN, decodeIndex
from nltk.tokenize import RegexpTokenizer

TOKENIZER = RegexpTokenizer(r'\w+')


def formCombinations(sentence):
    """Generates all possible combinations of a sentence based on homophones

        :Returns: a dict containing combination-id (int) as keys with each
            value being a dict containing results for resp. combination with:
            1.  key: c (str)
                value: (list) sequence of pun-option-code encoding the sentence
            2.  key: s (str)
                value: (unicode) the (tokenized) sentence of the combination

        :arg sentence: (str) space separated sequence of words stripped of all
            punctuation
    """
    tokens = TOKENIZER.tokenize(sentence)
    realm = dict([(k, getPunPartners(tokens[k])) for k in range(len(tokens))])
    radix = max([len(v) for v in realm.values()])
    true_combinations = []
    possible_sentences = []
    for n in range(radix ** len(realm)):
        c = [decodeIndex(s)
             for s in base10toN(n, radix, len(realm))]
        if not any(c[i] >= len(realm[i]) for i in range(len(c))):
            possible_sentences.append(u' '.join([realm[i][c[i]]
                                                 for i in range(len(c))]))
            true_combinations.append(c)
    patterns = dict([(k, {'c': true_combinations[k],
                          's': possible_sentences[k]})
                     for k in range(len(true_combinations))])
    return patterns
#    codes = sorted([' '.join([str(i) for i in d]) for d in true_combinations])
#    return {'sentence': sentence, 'sentences': possible_sentences,
#            'codes': codes, 'combinations': true_combinations, 'realm': realm}


def patternDiff(p1, p2):
    """Validates pair of given 2 patterns for mutual variation of exactly 1
        word and finds pun location if pair is valid

        :Returns: (dict) result containing:
            1.  key:    (str) validity
                value:  (bool) True if pair valid
            2.  key:    (str) pun_location
                value:  (int) index of pun-word in the sentence

        :arg p1: (dict) pattern 1 - of the structure as that of value in
            output of the method formCombinations
        :arg p2: (dict) pattern 2 - of the form as that of p1
    """
    result = {}
    allowed = True
    for i in range(len(p1['c'])):
        if p1['c'][i] != p2['c'][i]:
            if allowed:
                result['pun_location'] = i
                result['sentences'] = [p1['s'], p2['s']]
                result['validity'] = True
                allowed = False
            else:
                result = {'validity': False}
                break
    return result


def pairUp(patterns):
    """Finds pairs of possible sentences varying by only one word (pun word)

        :Returns: a dict with keys being pair-id (int) each value being a dict
            with contains:
                1.  key: (str) pun_location,
                    value: index (int) of pun-word in the sentence
                2.  key: (str) sentences
                    value: list of 2 sentences (unicode) of the pair

        :arg patterns: (dict) Outcome of
            punisfun.src.punlocation.formCombinations
    """
    pairs = {}
    count = 0
    for i in range(len(patterns)):
        for j in range(i+1, len(patterns)):
            result = patternDiff(patterns[i], patterns[j])
            if result.pop('validity'):
                pairs[count] = result
                count += 1
    return pairs


def worker(sentence):
    """Worker function that processes one sentence to generate pairs of
        potential pun-holder sentences along with the pun location.

        :Returns: a dict with keys being pair-id (int) each value being a dict
            with contains:
                1.  key: (str) pun_location,
                    value: index (int) of pun-word in the sentence
                2.  key: (str) sentences
                    value: list of 2 sentences (unicode) of the pair

        :arg sentence: (str) space separated sequence of words stripped of all
            punctuation
    """
    return pairUp(formCombinations(sentence))
