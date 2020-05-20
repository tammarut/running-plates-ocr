import json
import os

path_answer = 'images/answer.json'


def read_answers(path_image):
    with open(path_answer) as json_answer:
        list_image = os.listdir(path_image)
        list_image.sort(key=lambda f: int(os.path.splitext(f)[0]))
        answer = []
        parsed_json = json.load(json_answer)
        for i in range(len(list_image)):
            answer.append(parsed_json[str(i)])

    return answer
