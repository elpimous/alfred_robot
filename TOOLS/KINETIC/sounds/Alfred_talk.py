#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# HTTP + URL packages
import httplib2
from urllib.parse import urlencode, quote # For URL creation

import os


# Mary server informations
mary_host = "localhost"
mary_port = "59125"

# Input text
input_text = "de impensable peintre de peinture"

# Build the query
query_hash = {"INPUT_TEXT":input_text,
              "INPUT_TYPE":"TEXT", # Input text
              "LOCALE":"fr",
              "VOICE":"pierre-voice-hsmm", # Voice informations  (need to be compatible)
              "OUTPUT_TYPE":"AUDIO",
              "AUDIO":"WAVE", # Audio informations (need both)
              }
query = urlencode(query_hash)
print("query = \"http://%s:%s/process?%s\"" % (mary_host, mary_port, query))

# Run the query to mary http server
h_mary = httplib2.Http()
resp, content = h_mary.request("http://%s:%s/process?" % (mary_host, mary_port), "POST", query)

#  Decode the wav file or raise an exception if no wav files
if (resp["content-type"] == "audio/x-wav"):

    # Write the wav file
    f = open("/tmp/output_wav.wav", "wb")
    f.write(content)
    f.close()

    # Play the wav file
    os.system('aplay /tmp/output_wav.wav')

else:
    raise Exception(content)
