from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
# from datetime import timedelta
from celery.schedules import crontab
from django.utils import timezone

@shared_task
def send_mail_task():
    print("Mail sending.......")

    # Send email every 5 minutes
    subject = 'welcome to Celery world'
    message = 'Hi thank you for using celery'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['manisha93singh@gmail.com']
    send_mail( subject, message, email_from, recipient_list,fail_silently=False )
    # print("Mail sent..............")

    return "Mail has been sent........"


@shared_task
def send_hello():
    print("HELLO.........")
    print("Current time is:", timezone.now())
    

# print_hello.apply_async(countdown=300, expires=timedelta(minutes=5))