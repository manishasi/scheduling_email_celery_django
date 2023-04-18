from django.shortcuts import render
from django.http import HttpResponse
from .tasks import *
# from .helper import *

def index(request):
    
    send_mail_task.delay()
    print(send_mail_task.delay(),'*******************')

    send_hello.delay()
    # print(send_hello(),"hello---------------------")

    # return render(request, 'home.html')

   

    # sleepy.delay(5)
    # print(add(3,4))
    # result = add.delay(3, 5)
  
    # return HttpResponse("<h1>Hello ,from send without celery show</h1>")
    # return HttpResponse("<h1>Hello ,from send mail show</h1>")
    return HttpResponse("<h1>Hello ,send mail HELLO</h1>")




# command run for celery server:
#python manage.py runserver
# celery -A scheduling_emails_with_celery_django  worker --pool=solo -l info
# celery -A scheduling_emails_with_celery_django beat -l INFO