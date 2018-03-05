import urllib2
import subprocess

class Calendar:

    def getHelpTitle(self):
        return "Calendar"

    def getHelpText(self):
        return 'Use /thisweek to get this week\'s calendar\n Use /week <weekNr> to get the week calendar \n Use /nextweek to get the calendar of next week'

    def renderCalendarImage(self, weekNr):
        if classNumber < 1:
            return False
        quarter = 1
        #w15 = s10
        if weekNr > 15:
            quarter = 4
        elif weekNr > 25:
            quarter = 1
        elif  weekNr > 35:
            quarter = 2
        elif weekNr > 45:
            quarter = 3

        url = "http://misc.hro.nl/roosterdienst/webroosters/CMI/kw" + quarter + "/" + weekNr + "/c/c00"+ self.classNumber +".htm"
        req = urllib2.Request(url)
        try:
            resp = urllib2.urlopen(req)
        except urllib2.HTTPError as e:
            return False
        else:
            subprocess.call(["webkit2png", url, "-x", "1920", "1080", "--output", "school.png"])
            return True

    def week(self, bot, update, args):
        chat_id = update.message.chat_id
        _week = update.message.date.isocalendar()[1]
        thisWeek = str(_week) if _week >= 10 else "0" + str(_week)
        try:
            if len(args) > 0:
                thisWeek = int(args[0])
                if thisWeek < 1:
                    bot.sendMessage(chat_id, text='We hebben een grapjas in de tent!')
                    return
                thisWeek = str(thisWeek) if thisWeek >=10 else "0" + str(thisWeek)
            
            if self.renderCalendarImage(thisWeek):
                bot.sendPhoto(chat_id, photo=open("school.png", "rb"))
            else:
                bot.sendMessage(chat_id, text='De rooster maker mag wel is doorwerken...')
        except ValueError:
            bot.sendMessage(chat_id, text='Vul een week nummer in, noob')
        except IndexError:
            bot.sendMessage(chat_id, text='Vul een week nummer in, noob')

    def nextWeek(self, bot, update, args):
        chat_id = update.message.chat_id
        _week = update.message.date.isocalendar()[1] + 1
        nextWeekString = str(_week) if _week >= 10 else "0" + str(_week)
        if self.renderCalendarImage(nextWeekString):
            bot.sendPhoto(chat_id, photo=open("school.png", "rb"))
        else:
            bot.sendMessage(chat_id, text='De rooster maker mag wel is doorwerken...')

    def classNumber(self, bot update args):
        if len(args) > 0:
                cn = int(args[0])
                if cn < 1:
                    bot.sendMessage(chat_id, text='We hebben een grapjas in de tent!')
                    return
                this.classNumber = str(cn)

    def __init__(self, dp):
        self.dp = dp
        self.classNumber = 0
        dp.addTelegramCommandHandler("class", self.classNumber)
        dp.addTelegramCommandHandler("week", self.week)
        dp.addTelegramCommandHandler("nextWeek", self.nextWeek)
        dp.addTelegramCommandHandler("nextweek", self.nextWeek)
        dp.addTelegramCommandHandler("thisWeek", self.week)
