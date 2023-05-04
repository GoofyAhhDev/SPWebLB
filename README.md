# SPLeaderboardsSite
Leaderboards website for Strike Practice


Made by https://github.com/apotpvp

Dm for questions: Jordy#2411



This api Runs a Flask Website

This api is written for the use of MariaDB! make sure you have a MariaDB Database. Other databases such as MongoDB or Mysql will not work.


HOW TO REPLICATE

1. Clone repository
2. Make sure you have python and pip installed
    https://www.python.org/downloads/

    https://pypi.org/project/pip/
        pip install pip
3. install the requirements folder by using the following command in the directory of your downloaded files
    pip install -r requirements.txt
4. Create a .env file to store database credentials
    Use the following format for your .env file otherwise the api won't work. please remove my default stuff and fill in with your own
        DB_HOST=yourip/yoururl
        DB_USER=yourdatabaseuser
        DB_PASSWORD=yourdatabasepassword
        DB_NAME=yourdatabasename
        DB_PORT=yourdatabaseport default port is 3306 most likely
5.  go into your terminal and type "python api.py" to run the website.
6.  website will be displayed on http://127.0.0.1:5000 or http://localhost:5000/ if you run this on a server you may need to open some ports or smth or redirect it.
