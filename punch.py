import os
import sys
import random

import requests
import yaml

source = requests.get('https://raw.githubusercontent.com/abhishtagatya/punchline/master/joke.yaml')
content = yaml.load(source.text)

selected_content = (content[random.randint(0, len(content) - 1)])

print(selected_content['joke'])
user_guess = input()
if user_guess == selected_content['punchline']:
    print("You just ruined my joke >:(")
else :
    print(selected_content['punchline'])
