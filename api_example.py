import requests
import json


r = requests.get('http://jsonplaceholder.typicode.com/photos/')
fr = r.json()
filename = "posts_" + str(len(fr)) + ".txt"
file = open(filename, 'w')
file.write(r.text)
file.close()

r = requests.get('http://jsonplaceholder.typicode.com/posts/?userId=4')
fr = r.json()
filename = "my_post.txt"
file = open(filename, 'w')
file.write(json.dumps(fr[3]))
file.close()




