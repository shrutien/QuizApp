from django.test import TestCase
import requests
# Create your tests here.

url = 'http://127.0.0.1:9999/exam/dashboard/'
token_key = 'a2f6376ec5762ae46e53aeca0331375bddd1bebe'
data = {
	'username': 'testing_instructor',
	'password': 'Dgsl$321'
}
r = requests.post(url,data,headers='Authorization': 'Token {0}'.format(token_key))
print(r.json())