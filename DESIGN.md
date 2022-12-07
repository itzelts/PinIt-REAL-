Our webapp is implemented usin a mix of html, css, javascript, and python. 

Python

The file app.py is implemented using python. It is here that we set up the webapp's structure and routing using flask.
On app.py, we set up all the different routes for our webapp using both "GET" and "POST" methods. 
A "GET" request renders the html file for that corresponding page on our webapp. 
Certain pages, such as 'Locations', 'Leaderboard' and 'Logout' only take "GET" requests.
These pages only return a page to the user, but dont necessarily take in user input.
For example, both 'Locations' and 'Leaderboard' just present users with information.
The information displayed depends on what was queried for the page.

A Note on the Database

We created our database using SQL. We created two tables to store information: one for users and one for locations.
The users table stores information on a user when they register. 
It stores user id, username, and password. 
This is important as it keeps a user signed in once they have initiated a session.
The locations table stores information on all the locations uploaded on the app.
It stores location id, name, description, and rank. 
Rank here is set to 0. 
When a new location is stored, its rank is 0. This will be updated later on according to user interaction.
We imported SQL from cs50 to execute command on our database. 
We query for data, insert data, and update data throughout the lenght of our code. 

Python Continued

Pages such as 'Location' and 'Leaderboard' use "SELECT". To show all the locations we just query for all the locations coordinates on the database. 
This information is then passed to the corresponding html file to appear on our map.
For leaderboard, the same thing is done, but all the data of locations is retrieved and is ordered by rank, from highest to lowest. 
This too is passed onto the corresponding html file to appear on our table. 
Other pages such as 'Login', 'Register', 'Upload' take both "GET" and "POST" requests.
"GET" requests simply render the according html file.
"POST" requests take in user input.

A Note on HTML Files

The HTML files set up the layout of our pages. 
The main part of these pages is a form that accepts user input.
Take for example the 'Login' page.
The html provides an input field for the user to input username and password. 
The hmtl also extends the layout and overall structure of our webapp.
It is here that we code the navigating bar with buttons that link to other pages on the webapp.

Python Continued 
Python then works with the imput provided via the html forms. 
This is done through the command "request.form.get". 
Several things can be done with this information. 
For example, in our code for 'Login', 'Register' and 'Upload' we can ensure that the form is filled out properly.
We can check the user inputted information for all fields on the form, and that certain fields meet certain specifications (such as the specifications for a password).
If something is not filled out properly, a warning is flashed notifying the user of their error.
The user is also redirected to that page again, meaing they cannot move on until the form is filled. 
Furthermore, queries are run on the database in order to allow that a user session is initiated.
When a user tries to register, a "SELECT" query is used to ensure that the username that user wants does not already exist.
When a user tries to log in, a "SELECT" query is used to ensure the user is logging in with correct information.
Furthermore an "Insert" query is used to register a new user by inserting them into the webapp's database.
Here the function "hash_password" is used to save the password as a hash. 
It is also here that a user's session is initiated to keep that user logged in. 
The 'Upload' page works similarly.
The page takes in user input to get a location's name and description. 
A "SELECT" query here is used to check whether a user's desired upload does not already exist on the database.
If it does not, an "INSERT" command is run to add the location to the database.
Otherwise, the location is not added again. 
Instead, we use an "UPDATE" command to change the ranking of the location.
Since the rank of a location is set to 0, the rank is increased by one everytime a location is tried to be inserted again.
This increasesthe locations rating.
Furthermore, it is here that we take in a users location.

Geolocation

To get a users location, we imported a module called geocoder.
This function takes in a users location and ouputs the correspoding longitude and latitude coordinates. 
We store these points into the locations table. 
This is what is passed onto the 'Locations' page in order to add markers to the map. 

The Map

We used a javascript function to upload a map into our website. This funciton is called initMap, and we made the center of the map at Harvard. 
We then created a for loop that puts pins on the map based on what locations are in our locations table. 
We created this map so that users can visualy see what locations are near them. 

CSS

When designing the CSS of our website, we looked at a few examples before we started. One of the ones that stood out was Instagram. 
On Instagram's login page, they have a grey border around the form, so we took this idea into account on our website. 
As far as colors, we knew that we both liked blue and that most real and well know websites have a white background, so we implemented these colors. 
We added images above all the forms to make the website more appealing. We created a nav bar with all our options, so that they are easy to find on all pages.
We also insured our color scheme was easy to look at and read, this is why there's high contrast between the white text and the blue background/vise versa. 







