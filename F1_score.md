F1-score

Purpose:
precision és recall kombinált mérése

Formula:
F1 = 2 * (precision * recall) / (precision + recall)

Mikor fontos:
imbalanced dataset esetén

Miért:
accuracy félrevezető lehet


F1-score viselkedése:

precision magas + recall alacsony → F1 közepes
precision alacsony + recall magas → F1 közepes
precision és recall is magas → F1 magas

F1 megbünteti ha az egyik metrika nagyon rossz