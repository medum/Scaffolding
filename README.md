
Teleboard Link
Please Check the attached excel sheet[CICDProjectPlan.xlsx](https://github.com/medum/Scaffolding/files/6461368/CICDProjectPlan.xlsx)




Architectural Diagram:
![image](https://user-images.githubusercontent.com/49653011/117881954-d3d90680-b277-11eb-9887-4a8377f67ca0.png)



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



Future Improvement:
 Include sulenium test cases
 pip install -U selenium
 sudo apt-get install -y chromium-browser
Include load test cases 

 Youtube link
 https://youtu.be/dVtEU3GI0E4
    



Azure Pipe lines:


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
 
 Locust.py
 Output
 ![image](https://user-images.githubusercontent.com/49653011/118043138-fab03f00-b342-11eb-894e-b609bc58b87d.png)
![image](https://user-images.githubusercontent.com/49653011/118043363-4367f800-b343-11eb-8bbe-e35470c8dd6c.png)
![image](https://user-images.githubusercontent.com/49653011/118043484-6abec500-b343-11eb-89df-8a32f5142863.png)

 ![image](https://user-images.githubusercontent.com/49653011/116760582-4b3ea880-a9e3-11eb-8d21-0d308df83f64.png)

Sucess Deployment:
![image](https://user-images.githubusercontent.com/49653011/117856950-433ffd80-b25a-11eb-862b-7b2e4660d7f1.png)

![image](https://user-images.githubusercontent.com/49653011/117854759-cca20080-b257-11eb-8d76-10a645dc22db.png)
![image](https://user-images.githubusercontent.com/49653011/117854158-35d54400-b257-11eb-98d2-1d1a42a16ce7.png)
![image](https://user-images.githubusercontent.com/49653011/117854233-4c7b9b00-b257-11eb-8a5e-85b2174eac6e.png)

recording:
 You tube link
https://youtu.be/fDYkBap5KKU



