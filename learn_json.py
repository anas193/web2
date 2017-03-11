import json
my_dict = {"firstName": "Анастасия", "lastName": "Кащеева", "github": {"nik": "anas193", "profil": "https://github.com/anas193", "repositories": ["edu"]}}
f = open('data.json', 'w')
f.write(json.dumps(my_dict))
f.close()

