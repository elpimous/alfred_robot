#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#parts for sending command
import httplib2
from urllib.parse import urlencode, quote

#for sending order on system
import os

mary_host = "localhost"
mary_port = "59125"

#sentence to speek
input_text = "tout ceci n'est qu'un test !"

#build query
query_hash = {"INPUT_TEXT":input_text,
              "INPUT_TYPE":"TEXT", # Input text
              "LOCALE":"fr",
              "VOICE":"pierre-voice-hsmm", # Voice informations (be sure that voices are compatible : 5.1 != 5.2)
              "OUTPUT_TYPE":"AUDIO",
              "AUDIO":"WAVE",
              }

query = urlencode(query_hash)

#launch query to marytts server
h_mary = httplib2.Http()
resp, content = h_mary.request("http://%s:%s/process?" % (mary_host, mary_port), "POST", query)

#  Decode the wav file or raise an exception if no wav files
if (resp["content-type"] == "audio/x-wav"):

    # Write the wav file
    f = open("/tmp/marytts_sentence.wav", "wb")
    f.write(content)
    f.close()

    # Play the wav file
    os.system('aplay /tmp/marytts_sentence.wav')

else:
    raise Exception(content)
