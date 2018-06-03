import os
import re
import urllib.parse
def text(file_text):
    # REQUIRE: input file_tone should be format .txt
    file = open(file_text)
    sentence = urllib.parse.quote(file.read())
    os.system("curl --user '4fbb610e-a433-4c18-8856-69c3f2a3986e':'8RTDJNscJblA' 'https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2017-02-27&text=%s&features=sentiment,keywords&keywords.sentiment=true'->text.txt"%sentence)
    file.close()

    sentiment = ''
    file2 = open("text.txt")
    for line in file2.readlines():
        if (re.match('\"label\":*', line.strip(" "))):
            sentiment = (eval(line.strip(" ").strip("\n").strip(",").split(":")[1]))
    file2.close()

    keyword = []
    file3 = open("text.txt")
    for line in file3.readlines():
        if (re.match('\"text\":*', line.strip(" "))):
            keyword.append(eval(line.strip(" ").strip("\n").strip(",").split(":")[1]))
    file3.close()

    text_info = dict({"sentiment":sentiment,"keyword":keyword})
    return text_info