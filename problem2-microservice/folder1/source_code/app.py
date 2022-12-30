from flask import Flask, request
import validators
import requests
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

keywords = ["bonfire", "cardio", "case", "character", "bonsai", "bonfier"]
keywords.sort()

@app.route("/prefixes")
def hello_world():
	keywords_in_url = request.url.split("?")[1].split("=")[1].split(",")
	
	temp_list = [i for i in keywords]
	temp_list1 = []
	keywords_response_list = []
	for i in keywords_in_url:
		if i in keywords:
			k = 0
			while k < len(i):
				for j in temp_list:
					if i[k] == j[0]:
						temp_list1.append(j[1:])
				temp_list = [ x for x in temp_list1 ]
				temp_list1 = []
				if(len(temp_list) == 1):
					break
				k += 1
			prefix = temp_list[0]
			prefix = i[:-len(prefix)]
			keywords_response_list.append({"keyword": i,"status": "found","prefix": prefix})
		else:
			keywords_response_list.append({"keyword": i,"status": "not_found","prefix": "not_applicable"})
		temp_list = [i for i in keywords]
	return keywords_response_list
		
app.run(debug=True)

#http://localhost:5000/numbers?url=http://localhost:8090/fibo&url=http://localhost:8090/primes
#prefixes?keywords=bonfire,bool
#[bonfire, cardio, case, character, bonsai]
