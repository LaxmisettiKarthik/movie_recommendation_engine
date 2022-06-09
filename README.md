# movie_recommendation_engine
This Python Project is regarding the Algorithms and the sub-topic covers the [Movie Recommender] which is built based on Machine Learning and Deep Learning. My project helps the users by giving the Movie predictions based on their Taste and choice. This project is built with algorithms that allow the ML model to predict the Movies in 3 different ways which are as follows:
(1) Popularity
(2) Content-based Filtering Approach
(3) Collaborative-based Filtering Approach

Let's see each category in detail and the app flow...

# Movie Recommender Window

At first the User need to give his user ID and Enter the Movie that he want to watch.The user interfacen of this Window Would look exactly like this...

![image](https://user-images.githubusercontent.com/105920583/172834000-4f4d895f-167b-4736-a6d2-d80f20d72414.png)


After giving all the required details and clicking on the Recommend button the user is fetched with 3 main categories of recommendation of movies they are as follows...

# 1. Popularity

In this popularity recommendation, the user will get the top most rated Movies from the entire database and users based on user's ratings. These movies are the same for all the users because these ratings are taken from all the total average users. 

This part will look like this:

![image](https://user-images.githubusercontent.com/105920583/172833326-cd787d4d-0c2e-4434-a1c3-b94fd4e4ede1.png)

# 2. CONTENT-BASED FILTERING


In this type of recommendation, the movies are fetched based on the similar movie name, genre, cast & crew of the film, category of the movie, etc. when two different users search for the same movie name these results are the same but when two different users search two different movie names the results are different cause here we are taking the movie name as the key component to fetch other movies based on content.

*Here we used the COSINE SIMILARITY Algorithm.

# This part will look like this for the movie SPIDER MAN:


![image](https://user-images.githubusercontent.com/105920583/172837289-a280b0f3-42d8-4fae-b4a9-f6c80e88f28b.png)



# 3. COLLABORATIVE-BASED FILTERING

In this type of recommendation, Movies are fetched to users based on collaborative filtering. Here these movies are specific to each user to user. The results are also very specific and unique for different users. For if two users with different User IDs search for the same movie name the results suggested to user 1 is different from user 2.

*Here we are using the MATRIX FACTORIZATION Algorithm
Example:
This part will exactly look like this if two users with different user ids like
 user 1: User ID 66 
 user 2: User Id 98
will search for the same movie spider-man (Movie name and User ID may be of your desired choice ) 

# These are the results for user 1:

![image](https://user-images.githubusercontent.com/105920583/172839425-e41b48be-e3e6-419f-b9c3-11adc06bc13a.png)
![image](https://user-images.githubusercontent.com/105920583/172839523-fc76838a-6b3a-4cc7-af41-d0803e55cbf9.png)

# These are the results for user 2:

![image](https://user-images.githubusercontent.com/105920583/172839763-423a5515-69cf-4def-99e2-f3da5d0bc128.png)
![image](https://user-images.githubusercontent.com/105920583/172839847-3d954821-fad2-4860-a8b9-308e522aa871.png)







By above examples you can find there are differnt movie recommendations for differnt users.


As this Model is deployed using the Streamlit framework in Streamlit Cloud we can use this on the Website as well as Android App by making API requests.
The interface in Mobile Android App can be viewed in two modes they are:
# 1. portrait mode


![Screenshot_2022-06-09-17-24-34-24_108946f426b9466a8f9637bfb706458b](https://user-images.githubusercontent.com/105920583/172842915-9fe590e4-67e2-49e9-8f58-564cd062008f.jpg)





# 3. Landscape mode


![Screenshot_2022-06-09-17-26-18-34](https://user-images.githubusercontent.com/105920583/172843051-2f23fb8e-657e-4e10-8ad7-0d0ffc0a2aeb.jpg)







these views are fine and good in both views...

# The interface on Website can be viewed in this way...


![image](https://user-images.githubusercontent.com/105920583/172843161-0cd2babf-cbfa-4a13-ac97-8ec052f88d4c.png)



#Extra features..
Being deployed in Streamlit it can also allow us to change a few extra aspects as shown in the picture both in Mobile App and on Website

![image](https://user-images.githubusercontent.com/105920583/172844850-fd96ab13-0425-4ed1-a86d-8a02964c8ca2.png)

# We can also mmake the app to view in Wide view
![image](https://user-images.githubusercontent.com/105920583/172845010-18556f47-05e5-483e-bddd-7e3596f3f7c5.png)



# We can also chnage the Themes like DARK Mode & LIGHT Mode
![image](https://user-images.githubusercontent.com/105920583/172845377-73d40030-81a9-4eda-a2b0-e71cac581825.png)



# Used Python libraries are:
```import pickle
import pandas as pd
import streamlit as st
import requests
import bz2
import pickle
import _pickle as cPickle
