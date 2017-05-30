#!/usr/bin/env python3

from preTrainedReader import PreTrainedVectorReader as ptvr
import numpy as np
import locale, sys

#google_model = ptvr.from_word2vec_binary('./pre_trained/GoogleNews-vectors-negative300.bin', unitvector=True)

#print(google_model.vocab[:100])
#print(google_model['dog'])

print(locale.getpreferredencoding())
print(sys.version)
glove_model = ptvr.from_glove_plain('./pre_trained/glove.twitter.27B.25d.txt', unitvector=True)
print(glove_model.vocab[:100])
print(glove_model['dog'])
