import logging

from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from justwork.celery import app
from .models import Page,Block

@app.task
def upd_counter(pk):
    obj=Page.objects.get(id=pk)
    lst=[i['id'] for i in obj.block.values('id')]
    blocks = Block.objects.filter(id__in=lst)
    for block in blocks:
        block.counter = block.counter + 1
        block.save()