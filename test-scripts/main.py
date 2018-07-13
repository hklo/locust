import json
from locust import HttpLocust, TaskSet, task
 
 
class UserBehavior(TaskSet):
 
    min_wait = 0  # minimun wait before start new task (in millisecond)
    max_wait = 0  # maximun wait before start new task (in millisecond)
 
    @task
    def JobsQueue(self):
 
        data = {'payload': '{\'job_id\':0,\'db_country_code\':\'stage\',\'update_status_flag\':false}', 'properties': {
            'message_id': 'JobPostingSiVA11/stage/job_id/0/2017-12-08 11:57:37',
            'delivery_mode': 2,
            'priority': 5,
            'content_type': 'application/json',
            'timestamp': '1512705462',
            'app_id': 'siva',
            }}
 
        response = self.client.request(
            method='GET',
            url='https://inlyt6uoh8.execute-api.ap-southeast-1.amazonaws.com/stage/v1/applications',
            headers={
                'Content-Type': 'application/json',
                'Authorization': 'Bearer 7996238841329bee2fce5022fa2b79250b90cd466b6c56e67989d7e112c43a04'
            }
        )
 
 
class WebsiteUser(HttpLocust):
 
    task_set = UserBehavior