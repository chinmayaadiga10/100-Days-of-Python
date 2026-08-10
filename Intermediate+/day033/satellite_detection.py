#working with parameters in API requests -> 

import requests
import datetime as dt
import smtplib
import math

MY_EMAIL=""
PASSWORD=""
MY_LAT=32.219044
MY_LONG=76.323402

#checking if satellite is currently near our latitude and longitude
def is_satellite_overhead():
    # this api returns the latitude,longitude of the satellite
    response=requests.get(url="http://api.open-notify.org/iss-now.json") 
    print(response)
    response.raise_for_status()
    data=response.json()
    print(data)

    # getting and storing the data from the iss API
    iss_longitude=float(data["iss_position"]["longitude"])
    iss_latitude=float(data["iss_position"]["latitude"])
    
    # adding a 5 degree margin for both longitude and latitude
    if math.fabs(MY_LAT-iss_latitude)<=5  and math.fabs(MY_LONG-iss_longitude)<=5:
        return True
    return False
    



# checking if the currently it is night so that we can spot ISS in the sky
def is_night():

    # getting current time in UTC format
    now=dt.datetime.now(dt.timezone.utc)
    time_now=now.hour
    print(time_now)


    parameters={
        "lat":MY_LAT,
        "lng":MY_LONG,
        "formatted":0
    }

    #this API returns the sunrise and the sunset times for the given coordinates, (passed in params)
    response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data=response.json()
    # print(data)

    # getting the sunrise and sunset time of our location using API and storing them in variables
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])
    
    # checking if it is currently night or day
    if time_now>=sunset or time_now<=sunrise:
        return True
    return False
        
    
# if the satellite is overhead and the time is night, we send mail to the user to go and look up in the sky.
if is_satellite_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com")as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        message=f"SUBJECT:Look Up\n\nThe ISS is above you at this time"
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=message)

