
# PinIt!

Welcome to PinIt!

## Getting Started

### The Right Repository
First make sure you are in the PinIt folder. You can run 'cd PinIt' on your terminal

### Running Flask

To run our application in FLask, execute 'flask run'

This shout ouput a port (likely something along the lines of http://127.0.0.1:5000). Open this link on the browser of your choice. You should now be able to interact with our webapp!

## Background

At Harvard it can be particularly difficult to find things to do nearby. If you have the time to go out (which is doubtful here), it can be hard to find just where to go. If you have looked up 'things to do near me' you have probabably rolled your eyes at the amount of tours that show up (a Harvard self guided tour?). Our application hopes to make this better. On this platform, college students can upload/share places they like near campus. Users can see what places are nearby to visit and which ones are the most popular. When a user is at a place they would like to visit, the app records their location and adds it to our database. This is available to all users on the app. 

## Configuration

### Register and Log In

Once you have PinIt successfully running in yours computer's browser, you must login. If you have previosly made an account, you may log in here. If you sucessfully log in, you will be redirected to the 'Locations' page.

Otherwise, if you dont already have an account, you will have to create an account to continue. You can register by clicking on 'Register' on the right side of the navigation toolbar. A form will appear. All fields are required and clearly labeled. To properly register, you must adhere to all specificatoins. Once you have registered you will be redirected to the 'Locations' page. 

### Navigating Between Tabs

To navigate to one of the different tabs, chose the desired tab from the navigation bar.

### Locations 

The 'Locations' page shows a map with all locations that have been uploaded by all of the webapp's users. Each unique location here is represented by a marker on the map. The map is centered at Harvard. So the map should allow users to visualize the proximity of a location to campus. 

### Leaderboard

The 'Leaderboard' page shows the most popular places to visit amongst the webapp's current users. The locations are displayed on a table. Places with the most recommendations (i.e, trending among users) are displayed at the top. Popularity decreases down the list. 

### Upload

The upload page allows users to upload a place to the webapp. If a user is currently at a place they like, they may upload the place at that instant. A user must provide the name of the location as well as a small description of what the place is. The webapp automatically records the users location to store where that location is (and add it to the map). Once an upload is published, the user is redirected to the 'Leaderboard' page. If the location is new to the app, the user should now see a new entry on the map. Else if that location had already been uploaded, the user should see their upload higher up on the leaderboard's table. 

### Logout

To logout, click on the 'Logout' option at the top right of the navigation bar.

## Video 
Link to our video: 




