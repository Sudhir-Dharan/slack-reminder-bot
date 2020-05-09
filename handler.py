import logging
from datetime import datetime, date
import pickle
import os
from google.oauth2 import service_account
import googleapiclient.discovery

from slackclient import SlackClient

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SPREADSHEET_ID = ''
RANGE = 'A2:G'
SLACK_TOKEN = "" # found at https://api.slack.com/#auth)
SLACK_CHANNEL = ""
SERVICE_ACCOUNT_FILE = 'credentials.json'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def starter(event, context):
    current_time = datetime.now()
    name = context.function_name
    logger.info("Your cron function " + name + " started at " + str(current_time))

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials, cache_discovery=False)    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE).execute()
    values = result.get('values', [])

    today = date.today()

    sc = SlackClient(SLACK_TOKEN)
    line_count = 0
    for row in values:
    	line_count += 1
    	bday_checker = datetime.strptime(row[2], "%d/%m").date()
    	if bday_checker.month == today.month and bday_checker.day == today.day:
    		if sc.rtm_connect():
    			message = "Happy Birthday " + row[1] + " :birthday:"
    			print sc.api_call("chat.postMessage",link_names=1, as_user="true", channel=SLACK_CHANNEL, text=message)
    		else:
    			print("Connection Failed, invalid token?")

    	anniv_checker = datetime.strptime(row[5], "%m/%d/%Y").date()
    	if anniv_checker.month == today.month and anniv_checker.day == today.day:
    		if sc.rtm_connect():
    			yr_completed = today.year - anniv_checker.year
    			message = "Happy Anniversary " + row[1] + " :tada:. Congrats on completing " + str(yr_completed) + " years with Symphony Talent."
    			print sc.api_call("chat.postMessage",link_names=1, as_user="true", channel=SLACK_CHANNEL, text=message)
    		else:
    			print("Connection Failed, invalid token?")
    logger.info("Your cron function " + name + " ended at " + str(datetime.now()))
