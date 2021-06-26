# Final-Project
Web Programming with Django

# Introduction
#### Video Demo:  <https://youtu.be/062xDUWBdww>
#### Description: ToDoList is a website where you can add, edit and delete notes.

# Project Structure

## Main Page
In the main page you can add a new note by click "+" button. You can also change existing notes by click on them or delete them by click "x" button. You should confirm deleting on the delete page by click "Delete" button. Besides, if you want to find the note, just input any words in the center input box, and click "Search" button. 

![main page](/screenshots/mainpage.PNG)
![edit page](/screenshots/edit.PNG) 
![delete page](/screenshots/delete.PNG) 

## Create page
In the create page you can add a title, description and date of the note, then click "Submit" button. If you want to cancel changes, just click "Back" at the top of page.

![create page](/screenshots/create.PNG) 

## Login page
Before creating notes, you need to login. Just paste your username and password in according fields. If you don't have an account yet, click "Register" below on the page.

![login page](/screenshots/login.PNG) 

## Register page
Fill in the fields "Username", "Password" and "Password confirmation" and click "Register" button.

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
