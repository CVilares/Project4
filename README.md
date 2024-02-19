# Porto Sips - Discovering Porto's Hidden Gems

Welcome to Porto Sips, your ultimate guide to uncovering the best bars in Porto, Portugal.

Embark on a journey through the vibrant and historic streets of Porto as we unveil the city's hidden gems and top-rated bars. Whether you're a seasoned traveler or a local enthusiast, Porto Sips is your go-to destination for exploring the rich tapestry of Porto's bar scene.

Indulge in the essence of Portuguese culture as you immerse yourself in the eclectic ambiance of Porto's renowned bars. From charming taverns tucked away in cobblestone alleys to sleek and modern lounges boasting panoramic views of the Douro River, Porto Sips offers a curated selection of venues to suit every taste and preference.

Join our community of passionate bar aficionados as we share insider tips, personal experiences, and captivating stories from the heart of Porto's nightlife. With Porto Sips, your journey to discovering Porto's finest bars begins here. Cheers to unforgettable experiences and endless adventures in Porto!

[View the live project here.](https://berlin-bestbeers.herokuapp.com/)

﻿![Responsive_Design_in_all_gadgets](/static/images/responsive_design.jpg)

## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux)
  * [Project Goals:](#project-goals)
  * [Strategy used:](#strategy-used)
 * [Agile Workflow](#agile-workflow)
   * [User stories:](#user-stories)
      * [EPIC Admin Account management](#epic-admin-account-management)
      * [EPIC Post](#epic-post) 
      * [EPIC Like and Dislike](#epic-like-and-dislike) 
      * [EPIC Edit and Delete comment and posts](#epic-edit-and-delete-comment-and-posts) 
      * [EPIC UX and UI](#epic-ux-and-ui) 

* [Features](#features)
  * [Installed Features](#installed-features)
    * [Navigation bar:](#navigation-bar)
    * [Home page:](#home)
    * [Blog page](#blog)
    * [Bars List](#bars_list)
    * [Register function:](#register-function)
    * [Login page:](#login-page)
    * [Logout page:](#logout-page)
    * [Add a post:](#add-a-post)
    * [Post detail:](#post-detail)
    * [Post update:](#post-update)
    * [Comment update:](#comment-update)
    * [Django Admin superuser:](#django-admin-superuser)
    * [System Feedback messages:](#system-feedback-messages)
    * [Footer:](#footer)
    * [Meta Data:](#meta-data)
  * [Features to Implement in the future](#features-to-implement-in-the-future)
* [Design](#design)
  * [Wireframes](#wireframes)
  * [Database Design](#database-design)
	  * [Classes:](#classes)
	  * [Site map](#site-map)
	  * [Colours used](#colours-used)
	  * [Typography](#typography)
	  * [Images](#images)

* [Technologies](#technologies)
  * [Languages Used:](#languages-used)
  * [Frameworks and Libraries Used:](#frameworks-and-libraries-used)
  * [Software and Web Applications Used:](#software-and-web-applications-used)
* [Tests](#tests)
  * [Browser tests](#browser-tests)
  * [Responsiveness](#responsiveness)
  * [Validators:](#validators)
    * [W3C Markup Validator:](#w3c-markup-validator)
    * [W3C CSS Validator:](#w3c-css-validator)
    * [JSHint:](#jshint)
    * [PEP8 Online:](#pep8-online)
    * [Lighthouse test:](#lighthouse-test)
  * [Tests on user stories](#tests-on-user-stories)
  * [Further tests](#further-testing)
  * [Solved bugs](#solved-bugs)
  * [Known bugs](#known-bugs)
* [Deployment](#deployment)
* [Resubmission](#resubmission)
* [Credits](#credits)
  * [Code](#code)
  * [Acknowledgements](#acknowledgements)


## User Experience (UX)

### Project Goals:
The main goal of this project is to design a blog for craft beer enthusiasts living in or travelling through Berlin, Germany. 
This website should allow a CRUD functionality, where each user can register an account, login into that, logout, create his/her own visits to craft beer bars around the city, as well as read, comment,and delete posts and comments, without the need for an administrator to be present. 
The user should have full control over his own posts and comments.