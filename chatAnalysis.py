# graphs import
import matplotlib.pyplot as plt
from collections import OrderedDict

# _chat.txt is the exported file from whatsapp, and should be in the same directory as this file.
chatfile = open("_chat.txt", "r")

# makes a list, and assigns each line from the original file as an item
messages = [line for line in chatfile]

# function to figure out the cumulative messages per hour of the day.
def cumulativeHours():
    cumuHour = {hour : 0 for hour in range(24)}
    hours = [item[12:14] for item in messages]
    people = [item[22:26] for item in messages]

    for msg in hours:
        if (msg.isdigit()):
            hour = int(msg)
            if (hour >= 0 and hour <= 23):
                    cumuHour[hour] += 1
    print(cumuHour)

    plt.bar(cumuHour.keys(), cumuHour.values(), align='center')
    plt.xticks(range(len(cumuHour)), cumuHour.keys())

    plt.show()

def monthlymessages(messagestofilter):
    months = OrderedDict()
    months['04/2017'] = 0
    months['05/2017'] = 0
    months['06/2017'] = 0
    months['07/2017'] = 0
    months['08/2017'] = 0
    months['09/2017'] = 0
    months['10/2017'] = 0
    months['11/2017'] = 0
    months['12/2017'] = 0
    months['01/2018'] = 0
    months['02/2018'] = 0
    months['03/2018'] = 0
    months['04/2018'] = 0
    months['05/2018'] = 0
    #months = {'04/2017': 0,'05/2017': 0,'06/2017': 0,'07/2017': 0,'08/2017': 0,'09/2017': 0,'10/2017': 0,'11/2017': 0,'12/2017': 0, '01/2018': 0,'02/2018': 0,'03/2018': 0}
    for msg in messagestofilter:
        monthyear = msg[4:11]
        try:
            months[monthyear] += 1
        except KeyError: continue
    print(months)
    plt.bar(months.keys(), months.values(), align='center')
    plt.xticks(range(len(months)), months.keys())

    plt.show()

def howmuchdowemessage(messagestotest):
    cumuPerson = {" Cai" : 0, " Dar" : 0}
    people = [item[22:26] for item in messagestotest]
    for individual in people:
        if (individual == " Cai" or individual == " Dar"):
            cumuPerson[individual] += 1
    print(cumuPerson)

#call the functions
howmuchdowemessage(messages)
monthlymessages(messages)
