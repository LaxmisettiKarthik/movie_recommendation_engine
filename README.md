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

# 2. Content-based filtering 


In this type of recommendation, the movies are fetched based on the similar movie name, genre, cast & crew of the film, category of the movie, etc. when two different users search for the same movie name these results are the same but when two different users search two different movie names the results are different cause here we are taking the movie name as the key component to fetch other movies based on content.

*Here we used the COSINE SIMILARITY Algorithm.








# Used Python libraries are:
```import pickle
import pandas as pd
import streamlit as st
import requests
import bz2
import pickle
import _pickle as cPickle
