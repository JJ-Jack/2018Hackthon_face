import os
import urllib.parse
import json
def tones(file_tone):
    #REQUIRE: input file_tone should be format .txt
    file = open(file_tone)
    sentence = file.read()
    sentence = dict({"text":sentence})
    os.system("touch tone.json")
    f = open("tone.json", 'w')
    json.dump(sentence,f)
    f.close()
    os.system("curl -X POST --user 'cb9220b2-4212-4fc1-975a-4a586ee1995b':'vHWtQZzkWkQb' --header 'Content-Type: application/json' --data-binary @tone.json 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21'->tone.txt")
    file2 = open("tone.txt")
    content = file2.read()
    content = eval(content)
    file2.close()
    file.close()
    tone = content["document_tone"]["tones"][0]["tone_name"]
    return tone

