# FantasticFour
FantasticFour Inc. Developed an User Friendly- software application and SQL database management system called "Medical Doctor". The application documents all interactions between patients and the healthcare providers. Medical Doctor streamlined the process of recording patients' and workers' informations

## Step by Step System Installation
System Requirement: Window OS, MySQL Server Database

### 1. Installing MySQL
Follow this [link](https://dev.mysql.com/doc/refman/8.0/en/windows-installation.html) for directions to install MySQL on Window

### 2. Setting up Databases
After mySQL is installed. Set up a new connection for the database in MySQL WorkBench.
![MySQL New Connection](https://github.com/congnguyen53/FantasticFour/blob/master/MDPic/newconnection.png)
New Connection name will be used as hostname to connect to the database later

### 3. Loading the model (Database Design)
After new database connection is established. Proceed to load the model file given by our team.
![Load Model](https://github.com/congnguyen53/FantasticFour/blob/master/MDPic/loadmodel.png)

This is the Database Design created for the SQL Database Management System.

### 4. Forward Engineer the table.
After the Model is loaded, Forward Engineer the tables of the database into the established server.
![Forward Engineer](https://github.com/congnguyen53/FantasticFour/blob/master/MDPic/forward%20engineer.png)

### 5. Database Server Established
Refresh the database to check if all tables are loaded correctly.
![Refresh](https://github.com/congnguyen53/FantasticFour/blob/master/MDPic/refresh.png)

### 6. Connect “Medical Doctor” to MySQL Server
Open the main exe file inside the Medical Doctor folder.
![Login SQL](https://github.com/congnguyen53/FantasticFour/blob/master/MDPic/SQLlogin.png)


## Using Medical Doctor as Administrator
All the functionality of Medical Doctor of Version 1.0. If there are any errors please contact F4 Inc for a patch update.

### 1. Log-In into “Medical Doctor”
Default embedded admin account:
Username: __*admin*__
Password: __*admin*__

![Log-in](https://github.com/congnguyen53/FantasticFour/blob/master/MDPic/Login-Screen.JPG)

### 2. Create New User (Doctor, Nurse or Administration)
To create new Medical Doctor users. Fill out the employee information fields. All new accounts will be saved into the database. 

![New User](https://github.com/congnguyen53/FantasticFour/blob/master/MDPic/NewUserCreated.JPG)

### 3. Historical Log
All application activities and database modification will be recorded. They are displayed only for administrator users.

![Logging](https://github.com/congnguyen53/FantasticFour/blob/master/MDPic/historylog.JPG)

### 4. Adjustment to User account
Administrators can update and delete user accounts.

## Using Medical Doctor as Healthcare Professionals

### 1. Log-In
Using the Login information provided by the IT administrator of the hospital. **Username** will be the first 3 letters of the employee last name (can be less depending on the length of the name). <br />
**Password** will be randomly generated pins (4 numbers). Can be changed by the administrator later.

![Log-in](https://github.com/congnguyen53/FantasticFour/blob/master/MDPic/Login-Screen.JPG)

### 2. MainScreen






