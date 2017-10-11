# graphs import
import matplotlib.pyplot as plt

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


def howmuchdowemessage(messagestotest):
    cumuPerson = {"Cait" : 0, "Darr" : 0}
    people = [item[22:26] for item in messagestotest]
    for individual in people:
        if (individual == "Cait" or individual == "Darr"):
            cumuPerson[individual] += 1
    print(cumuPerson)

#call the functions
howmuchdowemessage(messages)
cumulativeHours()
