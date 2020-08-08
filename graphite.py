import requests
import json
import sys

if len(sys.argv)>1:
	threshold=float(sys.argv[1])
	war=float(sys.argv[2])
	t_name=sys.argv[3]
else:
	exit(3)

try:
	
	url = "https://play.grafana.org/api/datasources/proxy/1/render?target=aliasByNode(movingAverage(scaleToSeconds(apps.fakesite.*.counters.requests.count,%201),%202),%202)&format=json&from=-5min"
	data=requests.get(url)
	data_json = data.json()
	targets=len(data_json)
	flag=0
	if targets<1:
		print("UNKNOWN")
		sys.exit(3)
	else:
		for i in range(targets):
			if data_json[i]['target'] == t_name:
				datapoints=len(data_json[i]['datapoints'])
				for j in range(datapoints):
					flag=1
					if data_json[i]['datapoints'][j][0] > war:
						print("CRITICAL")
						sys.exit(2)
					if data_json[i]['datapoints'][j][0] > threshold:
						print("WARNING")
						sys.exit(1)
	if flag==0:
		print("UNKNOWN")
		sys.exit(3)
	else:
		print("OK")
		sys.exit(0)
except:
	pass



