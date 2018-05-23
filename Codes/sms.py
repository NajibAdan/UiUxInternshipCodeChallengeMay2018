'''
UiUx Internship Code Challenge
'''

import africastalking


def main():
    numbers = raw_input(
        'Please enter the numbers to send messages to, seperate each number by a comma: '
    )
    message = raw_input('Please enter your message: ')

    numbers_list = numbers.split(',')

    username = 'username'
    apikey = 'apikey'

    africastalking.initialize(username, apikey)
    sms = africastalking.SMS
    try:
        response = sms.send(message, numbers_list)
        for x in response['SMSMessageData']['Recipients']:
            if x['status'] == 'Success':
                print '********************************************************************************'
                print 'Message has been successfully send to the number' + x['number']
                print 'Message ID: ' + x['messageId']
                print 'Message Cost: ' + x['cost']
                print '********************************************************************************'
            else:
                print '*********************************************************************************'
                print 'Message could not be delivered to the number' + x['number'] + ' because of ' + x['status']
                print '*********************************************************************************'
    except ValueError as e:
        print e


if __name__ == '__main__':
    main()
