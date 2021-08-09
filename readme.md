Assignment: Dojo Survey
Objectives:
Practice creating a server with Flask from scratch
Practice adding routes to a Flask app
Practice having the client send data to the server with a form
Practice redirecting after the POST request.
Use Session to display the form data on the result page.


When you build this, please make sure that your program meets the following criteria:

http://localhost:5000 - have this display a nice looking HTML form.  The form should be submitted to '/process'
Save form data into session.
http://localhost:5000/result - have this display a html with the information that was submitted by POST
Don't forget that any inputs we want to be able to access from the form submission need to have a name!

It's always a good idea to print request.form to see if the form is delivering all the information you need in your routing method.