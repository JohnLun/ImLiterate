# import urllib library
from urllib.request import urlopen
  
# import json
import json

def get_definition(word):
    api_key = "d98bcc41-7387-4462-97a6-a380a51bbcc6"

    url_part_1 = "https://www.dictionaryapi.com/api/v3/references/learners/json/"
    url_part_2 = word
    url_part_3 = "?key=" + api_key
    final_url = url_part_1 + url_part_2 + url_part_3

    response = urlopen(final_url)

    data_json = json.loads(response.read())
    if len(data_json) == 0:
        print("Error: Word cannot be found")
        return

    all_data = data_json[0]
    #definition_section = all_data['def'][0]['sseq'][0][0][1]['dt'][0]
    definition_section = all_data['meta']['app-shortdef']
    part_of_speech = definition_section['fl']
    definition = definition_section['def']
    print(part_of_speech)
    print(definition)
