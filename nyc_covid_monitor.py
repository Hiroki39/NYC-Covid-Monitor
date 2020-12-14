import pytz
import datetime
import time
import requests

status_list = []
IFTTT_URL = "https://maker.ifttt.com/trigger/nyc_numbers_changed/with/key/\
             <YOUR_KEY>"  # replace <YOUR_KEY> with your IFTTT Webhook Key

while True:
    date = (datetime.datetime.now(pytz.timezone("US/Eastern")) -
            datetime.timedelta(days=1)).date().isoformat()

    params = {
        "test_date": date,
        # Work for all counties in NY State
        "$where": "county in ('New York', 'Queens', 'Kings', 'Richmond',\
                              'Bronx')"  # NYC Counties
    }

    # Get numbers from New York State Statewide COVID-19 Testing API
    results = requests.get("https://health.data.ny.gov/resource/xdss-u53e.json",
                           params=params).json()

    if results:
        total_positive = sum(int(result['new_positives'])
                             for result in results)
        total_tests = sum(int(result['total_number_of_tests'])
                          for result in results)
        percent_positive = "{:.2%}".format(total_positive / total_tests)

        curr_list = [total_positive, total_tests, percent_positive]

        # if there's an update for the covid numbers, make a POST request
        if status_list != curr_list:
            status_list = curr_list
            requests.post(IFTTT_URL, params={
                "value1": status_list[0],
                "value2": status_list[1],
                "value3": status_list[2]
            })

    time.sleep(1800)  # Check for update every half hour
