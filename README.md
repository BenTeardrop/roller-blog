# The Roller Blog



A blog for inline skaters, big wheels, racing, agressive and everything else iline skating related.
you can share for example images, ideas and spots to go skate to.

tech used: django, django summernote, presql.



live link

![dif screens]()


## Features


### the Navbar

![navbar]()

1. roller blog logo
the roller blog logo present on all the pages and links you back to the home page
![logo]()
2. home
present on all the pages and links you back to the home page
3. register
the register link apears when the user hasn't registered or logged in and takes you to the register form
![register page]()
4. login
the login apears only if you haven't logged in or registered
![login page]()
5. logout
the logout only appears on the navbar if the user has logged in
![logout page]()
6. Create Post
redirects you the the create a post page
![create post page]()
6. reviews 
takes you to the reviews page where you can check previous reviews and add your own. As long as you have sign up and logged in
![reviews page]()


### the main roller artwork

a colourful artwork with a rollerblader
![main artwork]() 

### Create post

a button takes you to a page to create a post for the blog

![createpost page]()

### the blog

the list of blog posts with a default image with 3 different type of skates
here 
features the post title, the post time and date as well as a featured photo that could be chosen by the user*
![blog section]()
![inline skates](https://pyxis.nymag.com/v1/imgs/d74/27b/7702abdc8a039a96b13eec053c1afca3fc-bic-rollerblades.jpg)

you also have featured in the blog posts the amount of thumbs up people left

and a site pagination set to 5 posts per page to keep it clean and clear

### blog post detail

![post detail page]()

each blog post is a link to the post detail page where you can read more about the post, like it with a thumbs up and commment on it as well.
the user need to be signed in to comment and the comment need to be approved by admin first. 

### the comment section

section on the post detail page where you can post comments about the post

![comment section]()

### bottom of the page

various social links 

![social links]()



# models

i created three models

1. class post 

2. class comment 

3. class review



# Testing

i have manualy manually and automatically tested this project by doing the following

* automatic testing the create form and review form in **test_form.py**
* manual testing on links and buttons and pagination.

## bugs
    several issues with the slug on the create post
    CreatePost had a conflict
    *issues wiring up the user photo from the create post form 


### solved bugs
    added the save function in the model.py to automatically attach the slug to the post title
    imported the CreateView method following django docs 




## remaining bugs
    issues wiring up the image input in the create post form. only available via the admin panel at the moment.
    i need to figure out how to connect it with the cloudinary database.

## validator testing







# deployment


this project was deployed using heroku

* step for deployment
 * fork or clone this repository
 * create a new heroku app
 * link the heroku app to the repository
 * click on deploy







# Credit

* based on the code institute codestar blog

* exerpts from rollernews.com

* then and now rollerblading podcast


