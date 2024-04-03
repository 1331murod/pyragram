from celery import shared_task
import requests
from .models import *
from celery.schedules import crontab
from datetime import datetime, timedelta
import requests 
from pyrogram import Client
import time
import asyncio
from celery import Celery
from reklama_boti.celery import app





api_id = 27427265
api_hash = '604b38998cfbbd7241aafec002b50b78'


async def send_message(group_id):
    message = Advertising.objects.first().title
    client = Client(name='me_client',api_id=api_id, api_hash=api_hash)
    await client.start()
    await client.send_message(str(group_id), message)
    await client.stop()



@app.task()
def salom():
    groups = Groups.objects.values_list('groups', flat=True)
    for group_id in groups:
         asyncio.run(send_message(group_id))