# views.py
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings

def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        from_email = request.POST.get('from_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recipient_list = ['ramz1230777@gmail.com']  # Замените на нужный адрес

        try:
            send_mail(
                subject,
                f'Name: {name}\nEmail: {from_email}\n\nMessage:\n{message}',
                from_email,
                recipient_list,
                fail_silently=False,
            )
            return HttpResponse('Email sent successfully!')
        except Exception as e:
            return HttpResponse(f'Failed to send email: {str(e)}')

    return render(request, 'myapp/contact.html')


def index(request):
    return render(request, 'myapp/index.html')
