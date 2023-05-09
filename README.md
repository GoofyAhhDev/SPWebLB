# SPWebLB
> A modern leaderboards website for StrikePractice

## Author


Made by https://github.com/apotpvp

Dm for questions: Jordy#2411


## What is it


* This project Runs a Flask Website that utilizes an API to get data from a MariaDB Database and display them on a webpage.




* The API is written in Python and the website is written in HTML, and uses Tailwind to create the CSS.



* This API is specifically designed for use with MariaDB. Please ensure that you have a MariaDB database available. Other databases, such as MongoDB or         MySQL, will not work with this API.

* Use the same Database as the one you use for StrikePractice on your server
* Plugin link:
  https://www.spigotmc.org/resources/strikepractice-%E2%80%93-1v1-2v2-bots-fights-pvp-events-parties-build-fights-and-more.46906/




![image](https://user-images.githubusercontent.com/72379044/236197867-9d2298a6-eec3-4604-bcc6-b378039fb3a8.png)





## How to Replicate

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


## FAQ

* How do i add new ladders (kits)?
    1. Go into the api.py file and add a new def for the ladder you want to add. you have to replace "ladderhere" with the ladder you want to add and "name_of_collum"
     with the collum name in you database. they have to be the same otherwise the api can't find it in the table in the DB.
     
  
        ![image](https://github.com/apotpvp/SPWebLB/assets/72379044/fecf045f-d9cd-4490-bafa-e2015357fe8b)

    2. next you need to add the def to the flask routing.
    fill "ladderhere" with the last part of the def you created previously. you should replace "ladder" with the kit
    
    
    ![image](https://github.com/apotpvp/SPWebLB/assets/72379044/d4e9f9ee-eac9-472d-92c2-c7a53c7b5724)

    4. you have to add the flask route to the stats.html route


    ![image](https://github.com/apotpvp/SPWebLB/assets/72379044/6c2cb2a3-0044-4f6b-a3d6-a15204683040)
    
    
    also add your ladder to the rendertemplate
    
    
    ![image](https://github.com/apotpvp/SPWebLB/assets/72379044/813d91fb-b3c1-4ae0-92c2-429e71c25ed0)

    6. Next you need to copy this div



    ![image](https://github.com/apotpvp/SPWebLB/assets/72379044/8607499d-6c13-4d41-aa60-0fcbee4fcc5e)

    and edit it so the ladder shows up
 * My imports are broken!

    1. make sure you have installed requirements.txt
    2. make sure your python is up to date.
    3. if requirements.txt doesn't work you would need to install the imports manually
    4. make sure you add the folder you installed the imports in to your PYTHONPATH

        see for help: https://docs.python.org/3/using/windows.html
        
        
        https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages
        
