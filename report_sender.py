import requests

def send_whatsapp_report(phone, message):
    url = "https://api.callmebot.com/whatsapp.php"
    params = {
        "phone": phone,
        "text": message,
        "apikey": "YOUR_API_KEY"
    }

    r = requests.get(url, params=params)
    return r.status_code == 200