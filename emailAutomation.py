import requests
import pytz
from datetime import datetime

// Setting the timezone to Asia/Kolkata

ist = pytz.timezone('Asia/Kolkata')

currentDate = datetime.date(datetime.now(tz=ist)).strftime('%d')

//It sends email to tenants on the first of every month and to owners, on the second of every month

tenantDate = '1'
ownerDate = '2'

if currentDate == tenantDate:
    requests.get('https://www.messageproperty.com/sendcontent/sendtenantemails')

if currentDate == ownerDate:
    requests.get('https://www.messageproperty.com/sendcontent/sendowneremails')
