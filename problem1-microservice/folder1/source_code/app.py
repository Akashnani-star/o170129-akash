from flask import Flask, request
import validators
import requests
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/numbers")
def hello_world():
	rem_time = 350
	start_time_for_bootstrap = time.time()
	urls = request.url.split("?")[1].split("&")
	new_urls = []
	for i in urls:
		url = i.replace("%2F","/").split("=")[1]
		if validators.url(url):
			new_urls.append(url)
	mylist = []
	end_time_for_bootstrap = time.time()
	rem_time -= int((end_time_for_bootstrap - start_time_for_bootstrap) * 1000)
	for i in new_urls:
		start_time = time.time()
		response = requests.get(i)
		end_time = time.time()
		rem_time -= int((end_time-start_time)*1000)
		if rem_time <= 0:
			print(rem_time)
			a = list(set(mylist))
			a.sort()
			return a
		if response.status_code >=200 and  response.status_code <= 299:
			for j in response.json()["numbers"]:
				mylist.append(j)
	a = list(set(mylist))
	a.sort()
	return a
app.run(debug=True)

#http://localhost:5000/numbers?url=http://localhost:8090/fibo&url=http://localhost:8090/primes
