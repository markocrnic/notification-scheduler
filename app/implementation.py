import json
from flask import jsonify
import requests
from datetime import date, datetime
from api_management.api_management import getpath


user2flower_get_request = getpath('users2flowers/')
flower_get_request = getpath('flowers/')
user_get_request = getpath('users/')
email_send_request = getpath('sendEmail/')


def getUsersWithFlowers():
    try:

        print('Starting creation of user list to send mails.')
        request = requests.get(user2flower_get_request)
        data = request.json()
        status = request.status_code

        if status != 200:
            return {'msg': 'User2Flower API is not available.'}, 500

        flowers = getFlowers()
        if flowers == 500:
            return {'msg': 'Flower API is not available.'}, 500

        users = getUsers()
        if users == 500:
            return {'msg': 'User API is not available.'}, 500

        to_contact = checkForEmailNotification(data)

        to_contact = joinWithFlowers(to_contact, flowers)

        to_contact = joinWithUser(to_contact, users)

        to_contact = checkToWater(to_contact)

        sendMail(to_contact)

        printUsersToWhomSent(to_contact)

        return {'msg': 'Emails sent successfully'}

    except Exception as e:
        print(e)
        return {'msg': 'Something went wrong while gathering users to send email.'}, 500


def checkForEmailNotification(data):
    listToContact = []

    for user2flower in data:
        if user2flower['email']:
            listToContact.append(user2flower)

    return listToContact


def getFlowers():
    request = requests.get(flower_get_request)
    data = request.json()
    status = request.status_code

    if status != 200:
        return 500

    return data


def getUsers():
    request = requests.get(user_get_request)
    data = request.json()
    status = request.status_code

    if status != 200:
        return 500

    return data


def joinWithFlowers(to_contact, flowers):

    for contact in to_contact:
        for flower in flowers:
            if contact['flower_id'] == flower['flower_id']:
                contact['watering_period'] = flower['watering_period']
                contact['name_ser'] = flower['name_ser']
                contact['name_lat'] = flower['name_lat']
                contact['description'] = flower['description']

    return to_contact


def joinWithUser(to_contact, users):
    for contact in to_contact:
        for user in users:
            if contact['user_id'] == user['user_id']:
                contact['first_name'] = user['first_name']
                contact['last_name'] = user['last_name']
                contact['username'] = user['username']
                contact['email'] = user['email']

    return to_contact


def checkToWater(to_contact):
    list_to_contact = []
    # date_format = "%Y-%m-%d"
    current_date = date.today()
    for contact in to_contact:
        year, month, day = parseDate(contact['date_of_inception'])
        date_of_inception = datetime(int(year), int(month), int(day))
        delta = current_date - date_of_inception.date()

        if delta.days % int(contact['watering_period']) == 0:
            list_to_contact.append(contact)
    return list_to_contact


def sendMail(to_contact):

    headers = {'content-type': 'application/json'}
    email_to_send = {}
    for contact in to_contact:
        email_to_send['to'] = contact['email']
        email_to_send['subject'] = 'It is time to water your plant!'
        email_to_send['text'] = 'Hello ' + contact['first_name'] + '!\n\nYou should water your ' + contact['name_lat'] + '.\n\nWith regards,\nyour planthealthcare team!'
        email = jsonify(email_to_send)
        request = requests.post(email_send_request, headers=headers, data=json.dumps(email_to_send))


def printUsersToWhomSent(to_contact):

    for contact in to_contact:
        print('Mail sent to ' + contact['first_name'] + ' ' + contact['last_name'])


def parseDate(datetoparse):
    year = datetoparse.split('-')[0]
    month = datetoparse.split('-')[1]
    day = datetoparse.split('-')[2]

    return year, month, day
