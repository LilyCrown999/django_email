import threading
from urllib import response
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.views.generic import TemplateView
# from django.core.mail import send_mail
import smtplib
from email.message import EmailMessage

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
    def post(self, request):

        name = request.POST['name']
        subject = request.POST['subject']
        e_message = request.POST['message']
        email_header = request.POST['header']

        context = {
            'fieldValues': request.POST
        }
        # print(message)
        html_text = f"""<html>\n{e_message}\n</html>"""
        
        sender_email_address = "xasdxasd926@gmail.com"
        email_password = "xasdxasdpass"

        try:
         # Emailing goes here

            email_smtp = "smtp.gmail.com"
            message = EmailMessage()
            message['Subject'] = email_header
            message['From'] = 'Michael @' + sender_email_address
            message['To'] = subject
            
            # Add message content as html type
            message.set_content(html_text, subtype='html')
            
            server = smtplib.SMTP(email_smtp, '587')
            server.ehlo()
            server.starttls()
            server.login(sender_email_address, email_password)
            server.send_message(message)
            server.quit()

            messages.success(request, f" Email sent sucessfully from {name} using {sender_email_address} 😉")
        except Exception as e:
            messages.info(request, "Something went wrong, please try again !!!")
            messages.info(request, e)
            print(e)


        return render(request, 'home.html', context=context)



