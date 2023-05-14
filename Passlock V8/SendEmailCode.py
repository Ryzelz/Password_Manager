# -*- coding: utf-8 -*-
"""
Created on Sun May 14 08:43:32 2023

@author: ryzel
"""

import ssl
import smtplib
from email.message import EmailMessage

class EmailSender:
    def __init__(self, email_sender, email_password):
        self.email_sender = email_sender
        self.email_password = email_password

    def send_email(self, email_receiver):
        print('emailmodule work')
        subject = "Email Verification Code: 911420"
        body = """Verify your email: \n 
        911420
        """

        em = EmailMessage()
        em['From'] = self.email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)
        
        em['X-Priority'] = '1'
        
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.email_sender, self.email_password)
            smtp.send_message(em)
