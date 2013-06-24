import sys
import urllib.request
import json

if len(sys.argv) is 1:
	url = 'http://api.justin.tv/api/stream/list.json?channel=gocnak'
elif len(sys.argv) == 2:
	url = 'http://api.justin.tv/api/stream/list.json?channel=' + str(sys.argv[1])
elif len(sys.argv) == 3:
	url = 'http://api.justin.tv/api/stream/list.json?channel=' + str(sys.argv[2])
	

f = urllib.request.urlopen(url).read()
if len(f) > 2:
	jsonData = json.loads(f.decode("utf8"))[0]['channel']
	print('{0} is live playing {1}!\nStream title: {2}'.format(jsonData['title'], jsonData['meta_game'], jsonData['status']))
else:
	print('User is not live.')
# s = str(jsonData['channel']['status']).encode(sys.stdout.encoding, errors="replace") #this may be needed to fix some stupid shit at some point