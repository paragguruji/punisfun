from pywsd.lesk import simple_lesk
import gensim 
import numpy as np
import scipy.spatial as spatial
from nltk.corpus import stopwords
<<<<<<< HEAD
import os
import json
import codecs
from nltk.corpus import cmudict
import sys
reload(sys)  

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

=======
from pywsd.lesk import simple_lesk
import os
import json
#from punisfun.src.pronunciation import getPunPartners as func

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

>>>>>>> 78665b5efcc15b87b06d83a9efe622ec1b3340c6

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
    
def avg_feature_vector(words, model, num_features):
        #function to average all words vectors in a given paragraph
        featureVec = np.zeros((num_features,), dtype="float32")
        nwords = 0
        #list containing names of words in the vocabulary
        index2word_set = set(model.index2word)
        for word in words:
            if word in index2word_set:
                nwords = nwords+1
                featureVec = np.add(featureVec, model[word])
        if(nwords>0):
            featureVec = np.divide(featureVec, nwords)
        return featureVec
word2vec_model = gensim.models.Word2Vec.load_word2vec_format('C:\Users\lenovo\Downloads\glove.6B\glove.6B.50d.txt', binary=False, encoding='utf8')
#-----------------------------------------------
<<<<<<< HEAD
fobj = codecs.open('C:\Users\lenovo\Desktop\NLT Project\punisfun\src\Data.txt', 'r', encoding='utf-8', errors='ignore')
fwriter = codecs.open('C:\Users\lenovo\Desktop\NLT Project\punisfun\src\Output.txt', 'w', encoding='utf-8',errors='ignore')
fview = codecs.open('C:\Users\lenovo\Desktop\NLT Project\punisfun\src\Data_View.txt', 'w', encoding='utf-8',errors='ignore')
for  line in fobj:
    Data_holder = line.split('~' , 2)
    Original_Sentence = Data_holder[0]
    
    PunWord = Data_holder[1]

    Original_Sentence_Vector = avg_feature_vector(Original_Sentence.split(), model=word2vec_model, num_features=50)
    candidates = getPunPartners(PunWord)
#    print candidates
    length= len(candidates)
    list1=[]
    if length > 1:
#        print("\nThe original sentence is: ") + Original_Sentence
        
        fwriter.write(Original_Sentence)
        fwriter.write("\t")
        
        fwriter.write(PunWord)
        fwriter.write("\t")
        
        fview.write(Original_Sentence)
        fview.write("\n")
        
        fview.write(PunWord)
        fview.write("\n")
        
#        print("\nI am getting homophonic words for the word: ") + PunWord
#        print("\nThe words are: ")
#        print(candidates)
        fwriter.write(str(candidates))
        fwriter.write("\t")
        
        fview.write(str(candidates))
        fview.write("\n")
        
        for i in candidates: 
            Context_From_PYWSD = simple_lesk(Original_Sentence, i, pos='n')
            if not Context_From_PYWSD:
#                print ("Null");
                Contextual_Sentence = i
#                print Contextual_Sentence
            else:
                Contextual_Sentence = Context_From_PYWSD.definition().encode()
            #stop words removal
            stop = set(stopwords.words('english'))
            catcher1 = [i for i in Contextual_Sentence.lower().split() if i not in stop]
            Contextual_Sentence = ""
            for word in catcher1:
                Contextual_Sentence = Contextual_Sentence + " " + word
                
=======

fobj = open('Main_dataset.txt', 'r')
for  line in fobj.readlines():
    Data_holder = line.split('~' , 2)
    #print Data_holder[0]#sentence
    #print Data_holder[1]#pun
    Original_Sentence = Data_holder[0]
    
    PunWord = Data_holder[1]
    Original_Sentence_Vector = avg_feature_vector(Original_Sentence.split(), model=word2vec_model, num_features=50)
    #----------------------------------------------------
    candidates = getPunPartners(PunWord)
    length= len(candidates)
    list1=[]
    if length > 1:
        print("\nThe original sentence is: ") + Original_Sentence
        print("\nI am getting homophonic words for the word: ") + PunWord
        print("\nThe words are: ")
        print(candidates)
        for i in candidates: 
            Context_From_PYWSD = simple_lesk(Original_Sentence, i, pos='n')
            if not Context_From_PYWSD:
                print ("Null");
                Contextual_Sentence = i
                print Contextual_Sentence
            else:
                Contextual_Sentence = Context_From_PYWSD.definition()
            #stop words removal
            stop = set(stopwords.words('english'))
            catcher1 = [i for i in Contextual_Sentence.lower().split() if i not in stop]
            #print catcher1
            Contextual_Sentence = ""
            for word in catcher1:
                Contextual_Sentence = Contextual_Sentence + " " + word
>>>>>>> 78665b5efcc15b87b06d83a9efe622ec1b3340c6
            #print Contextual_Sentence
            Vector_of_Words = avg_feature_vector(Contextual_Sentence.split(), model=word2vec_model, num_features=50)
            Similarity =  1 - spatial.distance.cosine(Original_Sentence_Vector,Vector_of_Words)
            list1.append(Similarity)
            #print "Maximum two similarities: " + holder
    if list1:
<<<<<<< HEAD
#        print list1
        
        fwriter.write(str(list1))
        fwriter.write("\t")
        
        fview.write(str(list1))
        fview.write("\n")
        
        list2=[]
        list2=sorted(list1)
        list3=list2[-2:]
        difference_of_max2= list2[1] - list2[0]
#        print("\nMaximum two values are: ")
#        print list3
        
        fwriter.write(str(list3))
        fwriter.write("\t")
        
        fview.write(str(list3))
        fview.write("\n")
        
#        print("\nTheir Difference is: ")
#        print difference_of_max2
        
        fwriter.write(str(difference_of_max2))
        fwriter.write("\n")
        
        fview.write(str(difference_of_max2))
        fview.write("\n\n\n")
print "Done!"
fobj.close(); 
fwriter.close();
=======
        print list1
        list2=[]
        list2=sorted(list1)
        list3=list2[-2:]
        difference= list2[1] - list2[0]
        print("\nMaximum two values are: ")
        print list3
        print("\nTheir Difference is: ")
        print difference      
fobj.close(); 
>>>>>>> 78665b5efcc15b87b06d83a9efe622ec1b3340c6
