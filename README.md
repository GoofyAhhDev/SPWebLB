# SPWebLB
> A modern leaderboards website for StrikePractice

## Author


Made by https://github.com/apotpvp

Dm for questions: Jordy#2411


## What is it?


This api Runs a Flask Website that utilizes an API to get data from a MariaDB Database and display them on the site.



The API is written in Python and the website is written in HTML, and uses Tailwind to create the CSS.



This api is written for the use of MariaDB! make sure you have a MariaDB Database. Other databases such as MongoDB or Mysql will not work.




![image](https://user-images.githubusercontent.com/72379044/236197867-9d2298a6-eec3-4604-bcc6-b378039fb3a8.png)





HOW TO REPLICATE

1. Clone repository
2. Make sure you have python and pip installed

    https://www.python.org/downloads/


    https://pypi.org/project/pip/


    pip install pip

3. install the requirements folder by using the following command in the directory of your downloaded files
    " pip install -r requirements.txt "

    ![image](https://user-images.githubusercontent.com/72379044/236198786-8960f215-9f23-45c6-a4e7-8a40c00a3a50.png)

4. Create a .env file to store database credentials


    Use the following format for your .env file otherwise the api won't work. please remove my default stuff and fill in with your own


        DB_HOST=yourip/yoururl
        DB_USER=yourdatabaseuser
        DB_PASSWORD=yourdatabasepassword
        DB_NAME=yourdatabasename
        DB_PORT=yourdatabaseport default port is 3306 most likely
    ![image](https://user-images.githubusercontent.com/72379044/236198112-ae75fd8c-8d5d-4af2-990d-33de6e366d44.png)

5.  go into your terminal and type "python api.py" to run the website.

    ![image](https://user-images.githubusercontent.com/72379044/236198231-7410dbcb-bbd6-4a6e-ac66-3951063eb0d5.png)

6.  website will be displayed on http://127.0.0.1:5000 or http://localhost:5000/ if you run this on a server you may need to open some ports or smth or redirect it.
