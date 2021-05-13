from locust import HttpUser, constant, task


class MyReqRes(HttpUser):

    wait_time = constant(1)
    host = "https://flask-ml-azure.azurewebsites.net/"

    @task
    def get_users(self):
        res = self.client.get("/")
        print(res.status_code)
        assert res.status_code == 200
