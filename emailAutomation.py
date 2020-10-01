import requests
import pytz
from datetime import datetime

// Setting the timezone to Asia/Kolkata

ist = pytz.timezone('Asia/Kolkata')

currentDate = datetime.date(datetime.now(tz=ist)).strftime('%d')

//You can change 1 and 2 to respective dates of the month

tenantDate = '1'
ownerDate = '2'

if currentDate == tenantDate:
    requests.get('https://www.messageproperty.com/sendcontent/sendtenantemails')

if currentDate == ownerDate:
    requests.get('https://www.messageproperty.com/sendcontent/sendowneremails')
