from locust import HttpLocust, TaskSet, task, between
import json

class LoadTestCCS(TaskSet):
    def on_start(self):
        pass

    def on_stop(self):
        pass
    
    @task(1)
    def call_api1(self):
        api_url = '/api/v1/userinfo?tableName=baseinitializecivil&startDate=01/01/2019%2012:00:00%20AM&endDate=01/31/2019%2012:00:00%20AM&productForm=4&limit=100'
        header = {
            "Authorization": "5fed08c6-338d-445b-8f06-1dad4645c4ee"
        }
        response = self.client.get(api_url, headers = header, name = 'API 1')
        print('response code: {}'.format(response.status_code))

    @task(1)
    def call_api2(self):
        api_url = '/api/v1/records/latestperplatformnetworknumber?tableName=basestationcivildata&startDate=10/1/2019%2012:00:00%20AM&endDate=10/30/2019%2012:00:00%20AM&platformNetworkNumber=00010120210703202041562290150202&limit=100'
        header = {
            "Authorization": "2553f87b-6d61-4b26-b12c-7a9e66ede21e"
        }
        response = self.client.get(api_url, headers = header, name = 'API 2')
        print('response code: {}'.format(response.status_code))

    @task(1)
    def call_api3(self):
        api_url = '/api/v1/records?tableName=basestationcivildata&startDate=10/1/2019%2012:00:00%20AM&endDate=10/30/2019%2012:00:00%20AM&platformNetworkNumber=00010120210703202041562290150202&limit=100'
        header = {
            "Authorization": "2553f87b-6d61-4b26-b12c-7a9e66ede21e"
        }
        response = self.client.get(api_url, headers = header, name = 'API 3')
        print('response code: {}'.format(response.status_code))

class WebsiteUser(HttpLocust):
    task_set = LoadTestCCS
    wait_time = between(3, 5)