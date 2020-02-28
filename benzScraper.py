from bs4 import BeautifulSoup
import requests
import datetime
from datetime import date
import time 

def getDayOfTheWeek():
    weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    today = date.today()
    year = today.year
    month = today.month
    day=today.day
    todayDay = datetime.date(year,month,day)
    newDay = todayDay.weekday()
    dayOfTheWeek = weekDays[newDay]
    return (dayOfTheWeek)

def getNumberOfTheWeek():
    weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    today = date.today()
    year = today.year
    month = today.month
    day=today.day
    todayDay = datetime.date(year,month,day)
    newDay = todayDay.weekday()
    return newDay

#Check if its a weekend
dayOfTheWeek = getDayOfTheWeek()
if (dayOfTheWeek == "Saturday" or dayOfTheWeek == "Sunday"):
    print (dayOfTheWeek)
    print ("Buddy, do you really have nothing better to do then check whats for lunch at work on the weekends. Wait till Monday lmao.")
    exit()
#Scrape the website
benzLink = "https://docs.google.com/document/u/1/d/e/2PACX-1vRR3xvkdmB8yuc86jH1lYyw5eLUDOo5luEyx_k9oxeF5xaSVUA1wrumEYWkvJGKiBy3xNUsNswPN59u/pub"
benzResponse = requests.get(benzLink, timeout=5)
benzContent = BeautifulSoup(benzResponse.content, "html.parser")

#Format the scraped information
food = []
for item in (benzContent.find_all("span")):
    food.append(item.text)
while("\xa0" in food): 
    food.remove("\xa0") 
while("" in food): 
    food.remove("")

mealList =[]
cuisineWeek = []

#Get the cuisine for the day
start = 0
end = 0
i = 3
while i < (len(food)):
    if (food[i-2]=="menu"):
        cuisineWeek.append(food[i])
    i+=1

#Figure out start an end indeces of meals of the day in list
weekDay = getDayOfTheWeek()
index = 0
newList = []
while index < (len(food)):
    if weekDay in str(food[index]):
        start = index + 1
    if "menu" == str(food[index]) and start != 0:
        end = index  
        break
    if "next week" in str(food[index]) and start != 0:
        end = index
        break
    index += 1

#Add all the food for a given day to a new list
while start < end:
    newList.append(food[start])
    start += 1

#Add asteriks to bold face when sent onto slack
counter = 0
while counter < len(newList):
    if "Per" in str(newList[counter]):
        counter += 1
    else:
         newList[counter] = "_" + newList[counter] + "_"
    counter += 1

#too lazy to debug more but add \n here bc above is too much work
#and requires debugging
counter = 0
# for i, val in enumerate(newList):
#     print (i, ":", val)

anotherList = []
i = 0
while i < len(newList):
    if i == 0:
        anotherList.append(newList[i])
    if ("Protein" in str(newList[i-1]) or "Please" in str(newList[i-1]) ):
        anotherList.append(newList[i])
    i += 1
# print (anotherList)
# while counter < len(newList):
#     if "Protein" in str(newList[counter]):
#         newList[counter] = newList[counter] + "\n"
#     if "Please" in str(newList[counter]):
#         newList[counter] = newList[counter] + "\n"
#     counter += 1

del anotherList[0]
# anotherList[5] = "_Chickpea Salad in a Citrus-Poppy Seed Vinaigrette _"
potato = '\n'.join(anotherList)
print (potato)
