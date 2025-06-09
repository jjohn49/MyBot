from datetime import datetime, date, time
import random

currentDate: datetime = None
commitTimes = set()


def generateCommitTimes(lowRange, highRange) -> None:
    for i in range(random.randint(lowRange,highRange)):
        hour = random.randint(8,20)
        minute = random.randint(0,59)
        commitTime = time(hour=hour, minute=minute)
        commitTimes.add(commitTime)

with open("/Projects/Data.txt", 'r') as file:

    while True :
        if currentDate == datetime.now() and currentDate.time() in commitTimes:
            commitTimes.remove(currentDate.time())
            file.write("Commit: " + datetime.now)
            exec(f'git add . && git commit -m "added commit for {datetime.now()}" && git push')

            if len(commitTimes) > 0:
                sorted = sorted(list(commitTimes))
                print(f'The next commit is at {sorted[0]}')
            else:
                print("There are no more commits scheduled for today")
        elif currentDate != datetime.now():
            currentDate = datetime.now()
            if currentDate.weekday() >= 5:
                generateCommitTimes(4,11)
            else:
                generateCommitTimes(0,6)

            if len(commitTimes) > 0:
                sorted = sorted(list(commitTimes))
                print(f'The first commit is at {sorted[0]}')
            else:
                print("There are no commits scheduled today")





