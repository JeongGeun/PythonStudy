import requests
import json

url = "https://swapi.dev/api/people/1/"
res =requests.get(url).json()

#print(type(res))

dic1 = {'ramyeon':'Korea','ramen':'Japan','noodle':['ramyeon','ramen']}
obj1 = json.dumps(dic1)
#print(type(dic1))


url2 ='https://nghttp2.org/httpbin/put'
res2 =requests.put(url2,data=obj1)

print(res2.text)