# tweet the current serial value (temperature)
# uses tweepy and PySerial, assumes you're on windows with port COM3
import tweepy
import serial
import time

#this should be removed before being put on GitHub

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN_KEY= ''
ACCESS_TOKEN_SECRET= ''


def tweet(status):
    '''
    updates the status of my twitter account
    requires tweepy (https://github.com/joshthecoder/tweepy)
    '''
    if len(status) > 140:
        raise Exception('status message is too long!')
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    result = api.update_status(status)
    return result


arduino = serial.Serial('\\.\COM3', 9600)

status = arduino.readline()
adaptedstatus = 'the value on the serial port is %s' % status
print(adaptedstatus)

filename = raw_input('Do you want to tweet this value? (Y or N): ')

if filename == 'Y':
    tweet(adaptedstatus)
    print('consider it tweeted.')
else:
    print('okay, well, um errr just remember that number i guess?')

arduino.close()




