# Document encoding utilizing the inverted pyramid structure
### A Galvanize Capstone
---
#### Brief Project Description
---
This project was designed to be part of a larger research project.  The goal of the larger project is to improve document encoding to enrich any NLP analysis that relies on news story data (or other data sources that utilize a structure in their original construction).

Due to time constraints and the need to warrent further exploration, a proof of concept was the focus on the capstone project.

This project sought to alter the commonly used TF-IDF term weighting schema by introducting the concept of the inverted pyramid, a document format used in journalism.  Currently tested with document classification, with future tests involving other Natural Language Processing analysis.

---
#### Some definitions
---
TF-IDF - Stands for Term Frequency - Inverse Document Frequency.  This weights words in a document based on two things.  The IDF part scores a word based on how rare it is among all the documents.  The TF part scores a word based on how many times it appears within a single document.  For a more in depth discussion, feel free to read [this](tfidf.md)

Inverted Pyramid - A structure for writing news articles (among other types of documents) that places the most important information towards the beginning and less important information towards the end.  For a more in depth discussion, feel free to read [this](inverted_pyramid.md)

---
#### How its different
---

What this project does is replaces the TF part of the TF-IDF weighting schema with one that scores a word based on where it appears in a document.  Earlier appearances of a word are scored higher than later words or appearances of the same word.

---
#### Further information
---
To learn more about how it works, [click here](how_it_works.md)

To learn more about the code, [click here](code_info.md)

To learn more about the data set used for testing, [click here](dataset.md)

To see how it performs for classification, [click here](outcomes.md)
