class Time():
    hours = 0
    mins = 0

    def __init__(self, hours, mins):

        self.hours = hours
        self.mins = mins

    def addTime(t1, t2):
        sum = Time()
        sum.hours = t1.hours + t2.hours
        sum.mins = t1.mins + t2.mins

        if sum.mins >= 60:
            sum.mins = sum.mins - 60
            sum.hours = sum.hours + 1
        return sum

    def displayTime(self):
        print(self.hours, "Hours", self.mins, "Minutes")

    def displayMinute(self):
        print(self.hours*60 + self.mins, "Minutes")


timeNow = Time(9,50)
timeNow.displayTime()
timeNow.displayMinute()


