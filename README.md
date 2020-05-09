# slack-reminder-bot

## Prerequisites
```
* Python 2.7
* npm 6.9.0
```
## Setup
1. Add serverless via npm package
```console
npm install --save serverless-python-requirements
```

2. Add serverless-python-requirements via npm package
```console
npm install --save serverless-python-requirements
```

3. Install Python package dependencies
```console
pip install -r requirements.txt
```

4. Change configurations in handler.py
```python
SPREADSHEET_ID = '<gsheet spreadsheet id>'
SLACK_TOKEN = 'Slack bot token'
SLACK_CHANNEL = '#<slack channel name>'
```

5. Create Google service account on the domain where the Google Sheet resides - ref: https://developers.google.com/identity/protocols/oauth2/service-account. After the google service account it created - Make sure to provide view access to the service account email on the specific GSheet.

6. Install the cron lambda on your aws account (Make sure aws credentials [~/.aws/credentials] is pointing to the account where the lambda needs to be created).
```console
serverless deploy
```
