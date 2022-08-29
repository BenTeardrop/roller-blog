# The Roller Blog



A blog for inline skaters, big wheels, racing, agressive and everything else iline skating related.
you can share for example images, ideas and spots to go skate to.

tech used: django, django summernote, presql.



live link

![dif screens](static/photos/isitresponsive.png)


## Features


### the Navbar

![navbar](/static/photos/navbar.png)

1. roller blog logo:

    ![logo](/static/photos/rollerblog-logo-nav.png)

    the roller blog logo present on all the pages and links you back to the home page
    
2. home:

    present on all the pages and links you back to the home page

3. register:



    ![register page](/static/photos/sign-up-form.png)

    - the register link apears when the user hasn't registered or logged in and takes you to the register form
    - the sign up page features username, email, and password with a sign in option if you already have registered
    

4. login:

    ![login page](/static/photos/sign-in-form.png)

    - the login apears only if you haven't logged in or registered
    - the login/ sign up section features a username input as well as the password with an option to sign up if        you haven't yet 
    

5. logout:

    ![logout page](/static/photos/sign-out-form.png)

    - the logout only appears on the navbar if the user has logged in
    - you can then logout/ sign out by clicking on the button and it will redirect you to the homepage.
    

6. Create Post:

    ![create post page](/static/photos/create-post-nav.png)

    - redirects you to the create a post page (see below for details)
    
6. reviews:

    ![reviews link nav](/static/photos/reviews.png)

    - takes you to the reviews page where you can check previous reviews and add your own. As long as you have sign up and logged in
    - the review page is there to leave an impression of the whole blog and it gives you a space to request the administrators about the website
    
    ![reviews page](/static/photos/reviews-form.png)


### the main roller artwork

a colourful artwork with a rollerblader
to catch people's attention
![main artwork](https://www.gannett-cdn.com/presto/2022/08/04/USAT/a331028a-368e-41d7-9590-01f23a2afdfe-herosolcotti.PNG?crop=2987,1681,x12,y0&width=2560) 

### Create post

a button takes you to a page to create a post for the blog

![createpost page](/static/photos/create-post-form.png)

the Create post page allows the user to post their own news or/and idea about rollerskating or inline skating.
the user can then choose a title for there post a text content and an image and then either publish or draft the post.

### the blog

- the list of blog posts with a default image with 3 different type of skates
    here if the user hasn't uploaded their own.
    features the post title, the post time and date as well as a featured photo that could be chosen by the user*

![blog section](/static/photos/theblog.png)
![inline skates](https://pyxis.nymag.com/v1/imgs/d74/27b/7702abdc8a039a96b13eec053c1afca3fc-bic-rollerblades.jpg)

- you also have featured in the blog posts the amount of thumbs up people left

![blog thumbs and time](/static/photos/thumbs-up-dates-time.png)

- and a site pagination set to 5 posts per page to keep it clean and clear

![blog pagination](/static/photos/nextpage.png)


### blog post detail

![post detail page](/static/photos/post-detail-part-1.png)
![post detail page](/static/photos/post-detail-part2.png)


- each blog post is a link to the post detail page where you can read more about the post, like it with a thumbs up and commment on it as well.
- the user need to be signed in to comment and the comment need to be approved by admin first. 

### the comment section

section on the post detail page where you can post comments about the post

![comment section](/static/photos/comments.png)

### warning messages

    - warning messages when the user hasn't sign in

![warning sign in](/static/photos/warning-need-to-signin.png)

    - when the user sign in or sign out or sign up

![warning sign in out](/static/photos/warning-signout.png)


    

### bottom of the page

various social links 

![social links](/static/photos/bottom-links.png)

### tasks github templates

    - i have used the agile template on github to follow the tasks needed for the project


![github tasks](/static/photos/tasks-templates.png)



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
    - html checker no fault found
![html checker](/static/photos/html-checker.png)

    - css checker no fault found
![css checker](/static/photos/Css-checker.png)


    - pep8: Checked all python code and all is right





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


