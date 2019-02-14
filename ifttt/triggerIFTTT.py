import requests


def trigger(webhook="https://maker.ifttt.com/trigger/{}/with/key/{}",event="vhs-kurs", apikey='[YOUR_WEB_HOOK_API_KEY]'):
	print(webhook.format(event, apikey))
	r = requests.get(webhook.format(event, apikey))
	return(r.status_code)


if __name__ == '__main__':
    print(trigger())
