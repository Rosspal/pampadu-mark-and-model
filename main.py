
import requests
import json

url_mark = "https://b2c.pampadu.ru/b2c/dict/mark"
url_model = "https://b2c.pampadu.ru/b2c/dict/model"
headers = {'widgetid': "769267b8-f8f9-4f36-aedd-a7d1f431e48e"}
#persent = 0

def get_marks():
    response_mark = requests.get(url_mark, headers=headers)
    return response_mark.json()

def get_models(id):
    response_model = requests.get(url_model, params={'markId': id}, headers=headers)
    return response_model.json()

def gluing_marks_and_models():
    loading_percentage = 0
    list = []
    marks = get_marks()
    for mark in marks:
        id = mark["id"]
        models = get_models(id)
        for model in models:
            full_name = mark["title"] + " " + model["title"]
            record = {'full_name': full_name, 'mark': mark["title"], 'model': model["title"]}
            list.append(record)

        loading_percentage = loading_percentage + 0.132275132
        print(str(round(loading_percentage, 1)) + "%")

    return list


def test_data():
    list = []
    marks = get_marks()
    mark = marks[0]
    id = mark["id"]
    models = get_models(id)
    for model in models:
        full_name = mark["title"] + " " + model["title"]
        record = {'full_name': full_name, 'mark': mark["title"], 'model': model["title"]}
        print(record)
        list.append(record)

    return list



def save_to_json(data):
    with open('data.txt', 'w') as file:
        json.dump(data, file, ensure_ascii=False)


if __name__ == '__main__':
    data = gluing_marks_and_models()
    print("successful")
    print(json.dumps(data, ensure_ascii=False))


