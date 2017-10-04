# Shane Bryan and the Case of the Inverted Pyramid
### A Galvanize Capstone
---
##### Brief Project Description
---
No this isn't the newest young adult novel.

This project sought to alter the commonly used TF-IDF term weighting schema by introducting the concept of the inverted pyramid, a document format used in journalism.  Currently tested with document classification, with future tests involving other Natural Language Processing analysis.

---
##### The what?
---
TF-IDF - Stands for Term Frequency - Inverse Document Frequency.  This weights words in a document based on two things.  The IDF part scores a word based on how rare it is among all the documents.  The TF part scores a word based on how many times it appears within a single document.  For a more in depth discussion, feel free to read [this](../blob/master/tfidf)

Inverted Pyramid - A structure for writing news articles (among other types of documents) that places the most important information towards the beginning and less important information towards the end.  For a more in depth discussion, feel free to read [this](../blob/master/inverted_pyramid)

---
##### Ok, so what are you doing?
---

What this project does is replaces the TF part of the TF-IDF weighting schema with one that scores a word based on where it appears in a document.  Earlier appearances of a word are scored higher than later words or appearances of the same word.

---
#### Further information
---
To learn more about how it works, [click here](../blob/master/how_it_works)

To learn more about the code, [click here](../blob/master/code_info)

To learn more about the data set used for testign, [click here](../blob/master/dataset)

To see how it performs for classification, [click here](../blob/master/outcomes)
