# PreTrainedVectorReader
A toy reader for reading different pre-trained word-embedding files, so I may not have to install all different models and use different apis.
When the file is readed, a class similar to a Word2vec is returned. Access a word's vector by model[word] (like a dictionary).
Can choose to read all vectors as unit-vectors, or in their original form.
Can provide a list (set) of desired words so that all other words will be ignored.

Now supports the following functions:
Read from Google News pre-trained word2vec model, binary form: from_word2vec_binary()
Read from GloVe pre-trained model, plain text form: from_glove_plain() 

This module is not tested, please report any bug, thanks.
