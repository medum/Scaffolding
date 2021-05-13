import requests
from locust import HttpUser, constant, task


class MyReqRes(HttpUser):

    wait_time = constant(1)
    host = "https://flask-ml-azure.azurewebsites.net/"

    @task
    def get_users(self):
        res = self.client.get("/")
        print(res.status_code)
        assert res.status_code == 200

    @task
    def predict(self):
        data = {"CHAS": {"0": 0}, "RM": {"0": 6.575}, "TAX": {"0": 296.0}, "PTRATIO": {"0": 15.3},
                    "B": {"0": 396.9},
                    "LSTAT": {"0": 4.98}}
        response = self.client.post('/predict', json=data)
        assert response.status_code == 200
