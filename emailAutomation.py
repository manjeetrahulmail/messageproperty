import requests
import pytz
from datetime import datetime

ist = pytz.timezone('Asia/Kolkata')

currentDate = datetime.date(datetime.now(tz=ist)).strftime('%d')

tenantDate = '1'
ownerDate = '2'

if currentDate == tenantDate:
    requests.get('https://www.messageproperty.com/sendcontent/sendtenantemails')

if currentDate == ownerDate:
    requests.get('https://www.messageproperty.com/sendcontent/sendowneremails')