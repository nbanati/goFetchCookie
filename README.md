# goFetchCookie
A simple selenium based script in python for automating the mundane task of fetching cookies by logging into a web application

Description: Often during development, one needs to fetch cookies from a website as a logged in user repetitively because cookies expire after a fixed duration. This selenium based python script is useful for automatic login and extraction of a cookie. 

Functionality: Automatically fetches the desired cookie from a web application and stores it in a text file.

Note: If you require to fetch cookies and use them in Postman repetitively, Postman pre-scripts are a better method. However, it requires more knowledge of the web application's login functionality. This selenium based script is an easy/fast way to do the same.

Requirements:
1. Python environment
2. Python's library for Selenium (use pip to install)
3. Chrome Selenium Driver (accessable by PATH)

Recommended Automation: Using a cron job or Window's Task scheduler the python script can be automated to run at a fixed interval.
