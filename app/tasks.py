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





api_id = 23474017
api_hash = '8f7bd64b6364be9a9cffa5c1fcbbf5aa'








async def send_message(group_id):
    message = Advertising.objects.first().title
    client = Client(name='me_account', api_id=api_id, api_hash=api_hash)
    await client.start()
    await client.send_message(str(group_id), message)
    await client.stop()



@app.task()
def salom():
    groups = Groups.objects.values_list('groups', flat=True)
    for group_id in groups:
        asyncio.run(send_message(group_id))

