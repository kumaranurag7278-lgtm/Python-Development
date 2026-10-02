import requests
import datetime
import smtplib

MY_LATITUDE = 30.67995
MY_LONGITUDE = 76.72211

MY_EMAIL = "anurag.7278@gmail.com"
MY_PASSWORD = "Security9128"


def iss_near_me():

    response = requests.get(
        url="http://api.open-notify.org/iss-now.json"
    )
    response.raise_for_status()

    data = response.json()

    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    if (MY_LATITUDE - 5 <= latitude <= MY_LATITUDE + 5 and
            MY_LONGITUDE - 5 <= longitude <= MY_LONGITUDE + 5):
        return True

    return False


def is_night():

    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }

    response = requests.get(
        url="https://api.sunrise-sunset.org/json",
        params=parameters
    )
    response.raise_for_status()

    data = response.json()

    sunrise = datetime.datetime.fromisoformat(
        data["results"]["sunrise"]
    )

    sunset = datetime.datetime.fromisoformat(
        data["results"]["sunset"]
    )

    # API gives UTC, so get current time in UTC
    time_now = datetime.datetime.now(datetime.timezone.utc)

    if time_now >= sunset or time_now <= sunrise:
        return True

    return False


if iss_near_me() and is_night():

    with smtplib.SMTP("smtp.gmail.com",587) as  connection:

        connection.starttls()   #Encrypt your msg 

# Authentication 
        connection.login(
            user=MY_EMAIL,
            password=MY_PASSWORD
        )
# Mail send 

        connection.send_mail(
            from_addr =MY_EMAIL,
            to_addr = MY_EMAIL,
            msg = "Subject:ISS overhead \n\n Look up! The ISS is near you."
        )


