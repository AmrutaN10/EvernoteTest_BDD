# Evernote Web Application UI Testing using Selenium with Python behave BDD framework
## Pre-requisites:
#### -Firefox browser
#### -Clone project
#### -Install required packages from requirement.txt

### Helper module:
It contains all common import libraries
### Locator module:
It contains all the web elements and their respective locations that are being used in UI testing
### Page Object module:
It contains all the web page classes contains web elements and action methods
### Features module:
It contains all the feature files and feature step defination scripts.
### reports module:
It contains allure JSON format test execution results summary reports
## How to execute automation tests?
#### -Clone the repository
#### -Change current directory to clone repository location in local system
#### -Update test data: Valid, Invalid login credentials in Login.feature and InvalidLogin.feature file (if only user wanted to try with new test data)
#### -Type following commands sequentially in commandline interface:
```
pip install -r requirement.txt
cd Evernote
behave Features
```
Once all test cases are exeuted successfull you can check console output from command line and JSON reports generated from Evernote_BDD/reports.

Upon succesful execution of test cases Console output should be similar to below:

![image](https://user-images.githubusercontent.com/105941762/169699959-28bfe7e2-af0d-465c-9b28-b9c9abc97e45.png)


## How to import Jenkins job to build and execute automation tests?
## Pre-requisites:
#### -ShiningPanda Jenkins plugin

### To Import Evernote build job:

#### -Open Jenkins
#### -Navigate to Dashboard
#### -Click on Manage Jenkins
#### -Click on Jenkins CLI under tools and Actions
#### -Download jenkins-cli.jar
#### -Open command line and navigate to jenkins-cli.jar download location
#### -Copy and paste the Evernote_JenkinsBuildJobExport.xml to the same location as jenkins-cli.jar
#### -execute below command after replacaing as per below:
Replace **http://server** with your jenkin server address in below command.
Replace **username:password** with your jenkins username and password in below command.
```
java -jar jenkins-cli.jar -s http://server -auth username:password create-job NewjobName_BDD < Evernote_BDD_JenkinsBuildJobExport.xml
```

Once job is imported successfully.
Open Jenkins and verify the created Newjob

![image](https://user-images.githubusercontent.com/105941762/169702044-0365ca82-5e81-4b1d-a682-9d86e25ae720.png)


Open job and click on configure
#### Naviagte to Source Code Management -> GIT -> Repositories -> Credentials
#### select user jenkins credentials from dropdown
#### Build -> Custom Python Builder -> Home
#### Change directory path to you local machine python installation directory

Save job and Click on Build Now
upon successful completion: compile output should look like below:

![image](https://user-images.githubusercontent.com/105941762/169700748-579dccba-5517-4299-a9ee-05466f74724c.png)

