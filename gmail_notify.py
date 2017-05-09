import sys, feedparser, winsound
#Here, we import modules needed for this program
newEmail=""
#get username and password from database using simple face and voice of person
USERNAME=user.gmail_username
PASSWORD=user.gmail_password
PROTO="https://"
SERVER="mail.google.com"
PATH="/gmail/feed/atom"
#We assign variables with values. Fill in your username and password
def mail(checker):
    email = int(feedparser.parse(
        PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH
    )["feed"]["fullcount"])
#parses your account data and sends it to gmail
    if email > 0:
        newEmail = 1
    else:
        newEmail = 0
    #checks for mail

    if newEmail==1:
         winsound.Beep(440, 500)
         winsound.Beep(370, 500)
         winsound.Beep(392, 500)

#Here plays sound if email present but we can implement this to read and reply email using google gmail API