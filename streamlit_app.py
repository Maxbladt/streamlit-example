import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import logging
import time
import pandas as pd

#I want logging to be to bot.log
logging.basicConfig(filename='bot.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


def fill_form(email_address):
    # Get current directory
    current_directory = os.getcwd()
    # Define selenium options

    # Create a new instance of the Firefox driver
    # Here, I assume that chromedriver is in the same directory as your Python script
    driver = webdriver.Chrome(service=webdriver.chrome.service.Service(executable_path=f'{current_directory}/chromedriver'))

    # rest of the code here...

def send_emails(n):
    # Load the csv
    df = pd.read_csv('emails.csv')

    # Initialize counter
    sent_emails = 0

    for index, row in df.iterrows():
        # Check if form has been sent (1) or not (0)
        if row['form_send'] == 0:
            # Send form
            fill_form(row['emails'])

            # Update row in DataFrame to indicate form has been sent
            df.at[index, 'form_send'] = 1

            # Increment counter
            sent_emails += 1

            # Check if the desired number of emails have been sent
            if sent_emails >= n:
                break

    # Save the updated DataFrame back to the CSV
    df.to_csv('emails.csv', index=False)

# Streamlit code
st.title('Email Sender')

number_of_emails = st.slider('Select the number of emails to send', 1, 100, 45)

if st.button('Send Emails'):
    st.write(f'Sending {number_of_emails} emails...')
    send_emails(number_of_emails)
    st.write(f'{number_of_emails} emails have been sent.')
