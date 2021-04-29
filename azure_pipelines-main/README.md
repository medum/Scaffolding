Step 1: Launch Cloud Shell
Go to the Azure Console and launch a bash shell.
![image](https://user-images.githubusercontent.com/49653011/116450973-f0ae1c80-a829-11eb-9ebe-bf0308ca323a.png)
Step 2: Set Up Your GitHub Repo and Integrate Azure Pipelines
![image](https://user-images.githubusercontent.com/49653011/116451186-2d7a1380-a82a-11eb-8a08-9b37f5642038.png)
Step 3: Clone the Repo and Create a Flask ML Service
In your Azure Cloud shell environment, clone the GitHub repository you created.

1. Set up virtualenv:
python3 -m venv ~/.flask-ml-azure
source ~/.flask-ml-azure/bin/activate
2. Run make install

3. Create an app service and initially deploy your app in Cloud Shell:
az webapp up -n flask-ml-azure
 ![image](https://user-images.githubusercontent.com/49653011/116451385-6619ed00-a82a-11eb-9651-1a33d9956216.png)
 sucessfull deploymnet will be as shown below:
 ![image](https://user-images.githubusercontent.com/49653011/116484763-c6735380-a857-11eb-9043-885a28a8245b.png)

 4. Verify the deployed application works by browsing to the deployed url
Go to https://flask-ml-azure.azurewebsites.net/ and you should see the same output as in the screenshot below:
![image](https://user-images.githubusercontent.com/49653011/116451589-b002d300-a82a-11eb-973b-14738551acc3.png)
Step 4: Perform Prediction
change the permissions of the file using below command:
chmod 777 make_predict_azure_app.sh
Change the line in make_predict_azure_app.sh to match the deployed prediction:

-X POST https://<yourappname>.azurewebsites.net:$PORT/predict
A successful prediction will look like this:
![image](https://user-images.githubusercontent.com/49653011/116451777-ed676080-a82a-11eb-9083-fbbd817bf982.png)
 Sucess Test Cases
 ![image](https://user-images.githubusercontent.com/49653011/116491574-34277b80-a868-11eb-893e-3297b8413f96.png)
Sucess Deployment:
 ![image](https://user-images.githubusercontent.com/49653011/116491645-5a4d1b80-a868-11eb-8ca2-33b9760c20ca.png)

recording:
 
https://user-images.githubusercontent.com/49653011/116465149-d6306f00-a83a-11eb-90ed-02e4e77025fe.mp4

