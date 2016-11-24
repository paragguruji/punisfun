import nltk
from pywsd.lesk import simple_lesk
import gensim 
import numpy as np
import scipy.spatial as spatial
from gensim.models import word2vec
import re
from nltk.corpus import stopwords
from pywsd.lesk import simple_lesk

#Average feature extraction------------------------------
def avg_feature_vector(words, model, num_features):
        #function to average all words vectors in a given paragraph
        featureVec = np.zeros((num_features,), dtype="float32")
        nwords = 0
        #list containing names of words in the vocabulary
        index2word_set = set(model.index2word)
        for word in words:
            if word in index2word_set:
                print len(model[word])
                nwords = nwords+1
                featureVec = np.add(featureVec, model[word])

        if(nwords>0):
            featureVec = np.divide(featureVec, nwords)
        return featureVec
word2vec_model = gensim.models.Word2Vec.load_word2vec_format('C:\Users\lenovo\Downloads\glove.6B\glove.6B.50d.txt', binary=False, encoding='utf8')
#-----------------------------------------------

#Opening the file
fobj = open("Main_dataset.txt", 'r')
for  line in fobj.readlines():
    Data_holder = line.split('~' , 2)
    #print Data_holder[0]#sentence
    #print Data_holder[1]#pun

    #Original sentence
    Original_Sentence = Data_holder[0] #sentence[0] should come here
    Original_Sentence_Vector = avg_feature_vector(Original_Sentence.split(), model=word2vec_model, num_features=50)
    #----------------------------------------------------
    
    #Homophonic_word similarity will be required here insert similar words code here and get its context->stop words removal->similarity check
    
    #Words-Context Block PYWSD
    PunWord = Data_holder[1]# This is the word and is sentence[1]
    Context_From_PYWSD = simple_lesk(Original_Sentence, PunWord, pos='n');
    Contextual_Sentence = Context_From_PYWSD.definition();
    #----------------------------------------------------------
    
    
    #stop words removal
    stop = set(stopwords.words('english'))
    catcher1 = [i for i in Contextual_Sentence.lower().split() if i not in stop];
    print catcher1
    Contextual_Sentence = ""
    for word in catcher1:
        Contextual_Sentence = Contextual_Sentence + " " + word
    print Contextual_Sentence ###########THIS IS MY INPUT TO TRAINED MODEL
    #---------------------------------------------------------
    
    #Create an array to collect here
    #Contextual_Sentence became my sentence_2
    #sentence_2 = "she fell through the window but felt no pane"
    Vector_of_Words = avg_feature_vector(Contextual_Sentence.split(), model=word2vec_model, num_features=50)
    Similarity =  1 - spatial.distance.cosine(Original_Sentence_Vector,Vector_of_Words)
    print(Similarity)### array here Nested

fobj.close();
