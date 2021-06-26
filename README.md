# Final-Project
Web Programming with Web Programming with Python and JavaScript

# Introduction
#### Video Demo:  <https://youtu.be/062xDUWBdww>
#### Description: ToDoList is a website where you can add, edit and delete notes. First you should create an account or login. At the top of page you will see how many tasks you have. A website has a user-friendly interface, "+" and "x" buttons mean "add" and "delete". To edit a note just click on it. Next to notes there're circles of the different colors: red if note isn't completed and orange if it is.

# Project Structure

## Main Page
In the main page you can add a new note by click "+" button. You can also change existing notes by click on them or delete them by click "x" button. Besides, if you want to find the note, just input any words in the center input box, and click "Search" button. Also you can always change an account by click "Logout" at the top of page.

![main page](/screenshots/mainpage.PNG)

## Edit Page
In the edit page you can edit such fields as title, description, date and complete. Completed notes are crossed off and their circle color changes from red to orange.

![edit page](/screenshots/edit.PNG) 

## Delete page
You should confirm deleting by click "Delete" button.

![delete page](/screenshots/delete.PNG) 

## Create page
In the create page you can add a title, description and date of the note, then click "Submit" button. If you want to cancel changes, just click "Back" at the top of page.

![create page](/screenshots/create.PNG) 

## Login page
Before creating notes, you need to login. Just paste your username and password in according fields. You'll receive a warning if there're any mistakes. If you don't have an account yet, click "Register" below on the page.

![login page](/screenshots/login.PNG) 

## Register page
Fill in the fields "Username", "Password" and "Password confirmation" and click "Register" button. If you already have an account, click "Login" below on the page.

![register page](/screenshots/register.PNG) 

# Setup
```
git clone https://github.com/aveclick/ToDoList.git
cd ToDoList
pip install django
```

When the dependent packages are installed, you can run this command to run your server.
```
python manage.py runserver
```

# Finally
Thanks for  [CS50x 2021](https://cs50.harvard.edu/x/2021/)
26.06.2021
