import requests
import json

payload = {"value1": 'gut'}

def trigger(webhook="https://maker.ifttt.com/trigger/{}/with/key/{}",event="vhs-kurs", apikey='[YOUR_WEB_HOOK_API_KEY]'):
	print(webhook.format(event, apikey))
	headers = {'content-type': 'application/json'}
	r = requests.get(webhook.format(event, apikey), data=json.dumps(payload), headers=headers)
	return(r.status_code)


if __name__ == '__main__':
    print(trigger())
