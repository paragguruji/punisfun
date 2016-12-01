# Data for Christian F. Hempelmann's pun-based model of sound similarity

This archive contains data for Christian F. Hempelmann's pun-based
model of sound similarity.  The data files correspond to the seven
appendices from Hempelmann (2003).

## Manifest

### Appendix A - CLAWS tag set.pdf

This PDF is an annotated version of the CLAWS tag set (Garside, 1997)
that was used for the word class identification in Appendix E.

### Appendix B - Syntactic function tag set.pdf

This PDF lists the syntactic function for which the pun-target pairs
were tagged initially, before being tagged with CLAWS.  These tags do
not appear in Appendix E, though are used in the main text of
Hempelmann (2003).

### Appendix C - Consonant distributions and frequency.tsv

This tab-delimited text file is a table listing the frequencies of
consonants in three different positions as extracted from the 127,070
entries of the
[CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict):
word-initial, word-final, and word-medial. These figures were used to
assess if the consonants were subject to change in certain
environments overproportionately to their regular occurrence.

### Appendix D - Non-corresponding segments.tsv

This tab-delimited text file is a table listing the non-corresponding
segments in the main corpus of target-pun pairs listed in Appendix E,
including the number of the pair in the database, the pair itself, the
immediate segmental environment, and the cost incurred by the
non-correspondence violation according to the preliminary cost
table. The leading numbers correspond to those in Appendix E, where
the full target-pun domain of the examples is listed.

### Appendix E - Main corpus of target-pun pairs.tsv

This tab-delimited text file is a table listing the 1182 pun-target
pairs selected from Sobkowiak's (1992) corpus.  The columns are as
follows:

* no. -- pair number
* pun
* target
* pun phon -- phonemic transcription of pun
* target phon -- phonemic transcription of target
* idiomaticity
* page no. -- page number from Crosbie (1977)
* grammaticality
* remark
* dialect
* POS pun -- CLAWS part of speech of pun
* POS target -- CLAWS part of speech of target
* x -- a marking field (unused)
* sum cost -- sum cost according to the preliminary cost table
  (Appendix G)
* sum/phon. -- sum cost per segment
* stress shift -- e=earlier in pun than in target; l=later
* syllable number -- -1=one syllable less in pun than target; +1=one
  more; +2 = two more

### Appendix F - Instrusion frequency table.tsv

This tab-delimited text file corresponds to the table from Sobkowiak
(1991:223). It is the primary basis for the cost table in Appendix G.

### Appendix G - Cost table.tsv

This tab-delimited text file is Hempelmann's preliminary cost table
based on the following formulas, where x is frequency attested by
Sobkowiak as documented in Appendix F, and 161 is the highest
frequency among the vowels:

| segment pair type | formula                 |
|-------------------|-------------------------|
| C/C C/. V/.       | y=x^-0.6 (asymptotic)   |
| V/V               | y=0.3-0.3x/161 (linear) |
| C/V V/C           | 1 (unattested)          |

## References

Crosbie, John S. (1977) Crosbie's Dictionary of Puns. New York, NY:
Harmony.

Garside, Roger. (1997) Using CLAWS to annotate the British National
Corpus. http://www.natcorp.ox.ac.uk/docs/garside_allc.html

Hempelmann, Christian F. (2003) Paronomasic Puns: Target
Recoverability Towards Automatic Generation. Ph.D. thesis. West
Lafayette, IN: Purdue University.

Sobkowiak, Włodzimierz. (1991) Metaphonology of English Paronomasic
Puns. Vol. 26. University of Bamberg Studies in English
Linguistics. Frankfurt: Lang. ISBN: 3-631-43761-7.

## Contact

Tristan Miller
miller@ukp.informatik.tu-darmstadt.de
November 9, 2016
