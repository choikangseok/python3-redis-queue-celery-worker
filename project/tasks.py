from pymongo import MongoClient
from celery import Celery
from wgetmanager import *
from celery.exceptions import SoftTimeLimitExceeded
import logging

app = Celery('tasks', backend='rpc://', broker='redis://localhost:6379')

@app.task(bind=True, name='tasks.my_task_0.jobs', soft_time_limit=300)
def my_task_0(self, Objectid, First_value, Second_value):
    try:
        pass
        #로직 정의 
        
    except Exception as e:
        logging.error(f"[my_task_0], [{e}]")
    finally:
        return f"{obj.today} {obj.Objectid} finished!"

@app.task(bind=True, name='tasks.my_task_1.jobs', soft_time_limit=300)
def my_task_1(self, Objectid, First_value, Second_value):
    try:
        pass
        #로직 정의 
        
    except Exception as e:
        logging.error(f"[my_task_1], [{e}]")
    finally:
        return f"{obj.today} {obj.Objectid} finished!"

@app.task(bind=True, name='tasks.my_task_2.jobs', soft_time_limit=300)
def my_task_2(self, Objectid, First_value, Second_value):
    try:
        pass
        #로직 정의 
        
    except Exception as e:
        logging.error(f"[my_task_2], [{e}]")
    finally:
        return f"{obj.today} {obj.Objectid} finished!"
        
@app.task(bind=True, name='tasks.my_task_3.jobs', soft_time_limit=300)
def my_task_3(self, Objectid, First_value, Second_value):
    try:
        pass
        #로직 정의 
        
    except Exception as e:
        logging.error(f"[my_task_3], [{e}]")
    finally:
        return f"{obj.today} {obj.Objectid} finished!"
