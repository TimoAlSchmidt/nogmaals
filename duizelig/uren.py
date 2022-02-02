#Print de hele uren van de dag. Voor de ochtend voeg je 'AM' toe. Voor de middag voeg je 'PM' toe

for n in range(2):
    for i in range(1,13):
        if n == 0:
            print(str(i)+":00 AM")
        else:
            print(str(i)+":00 PM")