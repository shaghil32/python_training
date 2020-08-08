import threading 
import requests
import redis

url = "http://127.0.0.1:8000"

con = redis.StrictRedis(host='localhost',port=6379)

def send_request(arg):
	req = requests.get(url,arg)
	print(str(arg)+" : : "+str(req))

while True:
	try:
	fetch = con.zrange('queue',-1,-1)
	if len(fetch) != 0:
		con.zrem('queue',fetch[0])
		print("The data fetched is "+fetch[0])
		worker = threading.Thread(target=send_request, args=(fetch[0],))
		worker.start()
	except:
		print("There is some error")

