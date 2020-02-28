import os
import slack
import datetime
from datetime import date
import time
import benzScraper 

def getCuisine():
        dayOfTheWeek = benzScraper.getDayOfTheWeek()
        print ("Today is: ", dayOfTheWeek)
        return "Today's Cuisine is: " + '*' + benzScraper.cuisineWeek[benzScraper.getNumberOfTheWeek()] + '*' + '\n' + benzScraper.potato

client = slack.WebClient(token="")

response = client.chat_postMessage(
    channel = '#general',
    text = getCuisine(),
    icon_emoji = ":stuffed_flatbread:"
)
