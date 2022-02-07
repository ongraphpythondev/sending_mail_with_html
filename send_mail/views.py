from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.

def mail(request):

    if request.method == "GET":
        return render(request, "send_mail/home.html")

    if request.method == 'POST' : 

        subject = request.POST.get('subject')
        message = request.POST.get('message')
        html_message = render_to_string('send_mail/mail_page.html' , {"email": request.POST.get('email')})
        plain_message = strip_tags(html_message)
        
        email_from = settings.EMAIL_HOST_USER
        recipient_list = []
        recipient_list.append(request.POST.get('email') )
        
        send_mail(subject, message , email_from ,recipient_list , html_message=html_message)
    
        return render(request, "send_mail/home.html" , {"message" : "succesfully send email"})

