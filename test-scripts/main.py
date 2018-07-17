import json
from locust import HttpLocust, TaskSet, task
from data import jobIds
import random
 
class UserBehavior(TaskSet):
    
    def get_user(self):
        user = random.choice(jobIds)
        return user

    @task
    def JobsQueue(self):
        user = self.get_user()
        response = self.client.get(f"{path}")
 
class WebsiteUser(HttpLocust):
    min_wait = 0  # minimun wait before start new task (in millisecond)
    max_wait = 0  # maximun wait before start new task (in millisecond)

    task_set = UserBehavior