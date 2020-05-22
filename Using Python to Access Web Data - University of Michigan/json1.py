import json

data = '''
{
    "name" : "Chuck",
    "phone" : {
        "type" : "initl",
        "number" : "+15248766"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print('Name: ',info["name"])
print('Number: ', info["phone"]["number"])
