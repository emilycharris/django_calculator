# django_calculator
Django calculator homework

_This was a two-part assignment I completed as part of my work at The Iron Yard_

##Part One
Objective: Create a basic django calculator that takes 2 text inputs and an operator from a dropdown menu and calculates a result.

**Learning Objectives**

After completing this assignment, you should be able to:
- Create a Django web app from scratch
- Integrate the Twitter Bootstrap CSS framework into your app
- Understand how to create HTML elements and apply a class to basic elements
- Create named inputs
- Work with forms, GET requests, and Querystrings

**Requirements**
- Create a new Django project and called it django_calculator.
- Integrate Twitter bootstrap into your static directory or use it via a CDN.
- Create a single url/view that shows an html page with 2 text inputs, a dropdown of math operators, and a submit button.
- When you submit the value it should calculate the result of the two text inputs with the given operator.
- Output the result onto the page.
- Output the equation onto the page.

##Part Two


**Learning Objectives**

After completing this assignment, you should be able to:
- Implement new features into existing applications
- Understand the built in Django authentication system including:
- Django's Login/Logout Views
- Django's User creation form
- Be able to create models that have a ForeignKey to a django User instance.
- Have a "logged in user only" url that will show a user their history of operations they've created.


**Requirements:**
- Add an Operation model to your application and include all important fields relevant to tracking operation history
- Create a url that allows a user to create a user account
- Create a page that allows a user to log in to your application
- Adapt your existing "math" view to create a Operation instance in the database if the user initiating the request is currently logged in.
- In a user's profile page, show them a list of their operations they have created.

In completing this assignment, I used Python and Django.
