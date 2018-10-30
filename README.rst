HashTag Generation From Text Files
==========================
---------------
Input Files:
---------------
A series of text files, e.g., doc1.txt,...,doc6.txt

---------------
Output File:
---------------
- log.txt: log file containing all logging info
- hashtag_table.txt: text file containing JSON representation of Hashtag Table

---------------
How-to-Run:
---------------
python3 run.py

---------------
Requirements (Recommended):
---------------
- Python 3.6.3
- Scikit-Learn 0.19.1
- Numpy 1.13.3
- NLTK 3.3 (with punkt and stopword package installed)

---------------
Notes:
---------------
- Input text files are defined within run.py (in default, doc1.txt, doc2.txt, doc3.txt are compared)
- The number of output hastags is specified by variable topnumber in run.py (in default, it's set to 1)