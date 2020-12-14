# NYC-Covid-Monitor

Before running this script on your server, replace `<YOUR_KEY>` in line 8 with your own IFTTT Webhook key. Then, enter `python nyc_covid_monitor.py` to run the script. The webhook will be triggered every time the covid number is updated.

The data is from New York State Department of Health. You could customize this script by changing counties in line 17 to any NY State county.

Reference: [New York State Department of Health | Health Data NY API](https://dev.socrata.com/foundry/health.data.ny.gov/xdss-u53e)
