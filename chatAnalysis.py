import matplotlib.pyplot as plt

chatfile = open("_chat.txt", "r")

messages = [line for line in chatfile]

def cumulativeHours():
    cumuHour = {hour : 0 for hour in range(24)}
    cumuCait = {hour : 0 for hour in range(24)}
    cumuDarren = {hour : 0 for hour in range(24)}

    hours = [item[12:14] for item in messages]
    people = [item[22:26] for item in messages]

    for msg in hours:
        if (msg.isdigit()):
            hour = int(msg)
            if (hour >= 0 and hour <= 23):
#                    cumuCait[hour] += 1
#                elif(people[hour] == "Darr" ):
                    cumuDarren[hour] += 1
#                else:
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
    print cumuPerson

howmuchdowemessage(messages)
cumulativeHours()
