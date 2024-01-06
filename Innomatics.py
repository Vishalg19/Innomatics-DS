#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
movies_df = pd.read_csv("movies.csv")
ratings_df = pd.read_csv("ratings.csv")


# In[2]:


grouped_ratings_df = ratings_df.groupby("movieId").agg(count=("rating", "count"), mean_rating=("rating", "mean"))

joined_df = movies_df.join(grouped_ratings_df, on="movieId", how="inner")


filtered_df = joined_df[joined_df["count"] > 50]


# In[3]:


filtered_df


# In[4]:


sorted_df = filtered_df.sort_values(by="mean_rating", ascending=False)


# In[5]:


sorted_df


# In[6]:


top_movie = sorted_df.iloc[0]


# In[7]:


top_movie


# In[8]:


sorted_df = filtered_df.sort_values(by="count", ascending=False)


# In[9]:


top_5_movies = sorted_df.head(5)


# In[10]:


top_5_movies


# In[14]:


sci_fi_df = filtered_df[filtered_df["genres"] == "|Sci-Fi|"] # Assuming "genre" column exists
sorted_sci_fi_df = sci_fi_df.sort_values(by="count", ascending=False)


# In[15]:


sci_fi_df


# In[ ]:




