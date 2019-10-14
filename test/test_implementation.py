import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '../app'))

#from interface import app
import implementation
from flask import json

data_user_2_flower = [
    {
        "date_of_inception": "2019-09-22",
        "email": True,
        "flower_id": "24",
        "user2flower_id": "12",
        "user_id": "59"
    },
    {
        "date_of_inception": "2019-09-22",
        "email": True,
        "flower_id": "24",
        "user2flower_id": "13",
        "user_id": "58"
    }]

data_user_2_flower_no_mail = [
    {
        "date_of_inception": "2019-09-22",
        "email": False,
        "flower_id": "19",
        "user2flower_id": "5",
        "user_id": "59"
    },
    {
        "date_of_inception": "2019-09-22",
        "email": False,
        "flower_id": "19",
        "user2flower_id": "6",
        "user_id": "58"
    }]

flowers = [
    {
        "description": "This is a test flower. Used for testing functionality of email. It will be sent every day.",
        "flower_id": "24",
        "name_lat": "Test_Flower",
        "name_ser": "Test_cvet",
        "watering_period": "1"
    }
]

joined_user_2_flower_with_flowers = [
    {
        "date_of_inception": "2019-09-22",
        "email": True,
        "flower_id": "24",
        "user2flower_id": "12",
        "user_id": "59",
        "description": "This is a test flower. Used for testing functionality of email. It will be sent every day.",
        "name_lat": "Test_Flower",
        "name_ser": "Test_cvet",
        "watering_period": "1"
    },
    {
        "date_of_inception": "2019-09-22",
        "email": True,
        "flower_id": "24",
        "user2flower_id": "13",
        "user_id": "58",
        "description": "This is a test flower. Used for testing functionality of email. It will be sent every day.",
        "name_lat": "Test_Flower",
        "name_ser": "Test_cvet",
        "watering_period": "1"
    }
]

users = [
    {
        "admin": "True",
        "email": "marko.crnic@devoteam.com",
        "first_name": "Marko",
        "last_name": "Crnic",
        "user_id": "59",
        "username": "mcrnic"
    },
    {
        "admin": "True",
        "email": "milos.covilo@devoteam.com",
        "first_name": "Milos",
        "last_name": "Covilo",
        "user_id": "58",
        "username": "mcovilo"
    }
]

joined_user_2_flower_with_users = [
    {
        "date_of_inception": "2019-09-22",
        "flower_id": "24",
        "user2flower_id": "12",
        "user_id": "59",
        "description": "This is a test flower. Used for testing functionality of email. It will be sent every day.",
        "name_lat": "Test_Flower",
        "name_ser": "Test_cvet",
        "watering_period": "1",
        "email": "marko.crnic@devoteam.com",
        "first_name": "Marko",
        "last_name": "Crnic",
        "username": "mcrnic"

    },
    {
        "date_of_inception": "2019-09-22",
        "flower_id": "24",
        "user2flower_id": "13",
        "user_id": "58",
        "description": "This is a test flower. Used for testing functionality of email. It will be sent every day.",
        "name_lat": "Test_Flower",
        "name_ser": "Test_cvet",
        "watering_period": "1",
        "email": "milos.covilo@devoteam.com",
        "first_name": "Milos",
        "last_name": "Covilo",
        "username": "mcovilo"
    }
]

# Test create contact list based on emails
def test_create_contact_list_based_on_emails_successful():

    to_contact = implementation.checkForEmailNotification(data_user_2_flower)

    assert to_contact == data_user_2_flower


# Test create contact list based on emails
def test_create_contact_list_based_on_emails_with_no_mails_successful():

    to_contact = implementation.checkForEmailNotification(data_user_2_flower_no_mail)

    assert to_contact == []


# Test join with flowers
def test_join_user2flower_data_with_flowers():

    to_contact = implementation.joinWithFlowers(data_user_2_flower, flowers)

    print(str(to_contact) + '\n')
    print(str(joined_user_2_flower_with_flowers))

    assert to_contact == joined_user_2_flower_with_flowers


# Test join with users
def test_join_user2flower_data_with_users():

    to_contact = implementation.joinWithUser(joined_user_2_flower_with_flowers, users)

    assert to_contact == joined_user_2_flower_with_users


# Test check user to water plant
def test_check_date_to_water_plants():

    to_contact = implementation.checkToWater(joined_user_2_flower_with_users)

    assert to_contact == joined_user_2_flower_with_users

