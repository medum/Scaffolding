![image](https://user-images.githubusercontent.com/49653011/116579716-ac318800-a8e0-11eb-88d5-b7eb3f83cc27.png)

[CICDrecording.zip](https://github.com/medum/Scaffolding/files/6394345/CICDrecording.zip)
Create a git hub repo 
 launch an Azure Cloud Shell environment and create an ssh keys
 
![gitkeys](https://user-images.githubusercontent.com/49653011/116294162-a499a400-a765-11eb-92ca-787c84a19e8a.PNG)

Create the Make file
    write all the steps needed for the project, like installation of software, testing, lint ....
    include all in the make file and keep all the steps(install,lint,test)
    Make sure you have correct tabs other wise you may face below error:
    *** missing separator. stop. makefile
Create requirements.txt
   include below lines
   pylint
   pytest
Create the script file and test file.
 write negetive tests and positive tests
 
Execute make all, you should see the output shown in the screen shot
  ![makeall2](https://user-images.githubusercontent.com/49653011/116294952-8d0eeb00-a766-11eb-8352-09d1e8b9500e.PNG)
![makeall1](https://user-images.githubusercontent.com/49653011/116294956-8da78180-a766-11eb-95f8-bb524851f123.PNG)

go to git actions chick on set up a workflow yourself 
![image](https://user-images.githubusercontent.com/49653011/116456577-6ddc9000-a830-11eb-91a4-6ceaab7590d5.png)
modify the yml file as show below:
![image](https://user-images.githubusercontent.com/49653011/116456801-a8dec380-a830-11eb-9334-0028ccf83221.png)

this will do auto run when ever code is modified
![image](https://user-images.githubusercontent.com/49653011/116456986-df1c4300-a830-11eb-8064-68b1781a0d57.png)


 Doing recoding
    
CICDrecording.zip

Azure Pipe lines:
![image](https://user-images.githubusercontent.com/49653011/116579855-ccf9dd80-a8e0-11eb-9675-3dc1c27f9d8b.png)

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



