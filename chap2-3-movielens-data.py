# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd


unames = ['user_id', 'gender', 'age', 'occupatoin', 'zip']
users = pd.read_table('./movielens/users.dat', sep='::', 
                      header=None, names=unames, engine='python')

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('./movielens/ratings.dat', sep='::', 
                        header=None, names=rnames, engine='python')
                        
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('./movielens/movies.dat', sep='::', 
                       header=None, names=mnames, engine='python')

data = pd.merge(pd.merge(ratings, users), movies)

mean_ratings = data.pivot_table(
    values='rating', 
    index=['title'], 
    columns=['gender'], 
    aggfunc='mean'
)

active_titles = ratings_by_title.index[ratings_by_title >= 250]
mean_ratings_for_active_titles = mean_ratings.ix[active_titles]
mean_ratings_for_active_titles['diff'] = mean_ratings_for_active_titles['M'] - mean_ratings_for_active_titles['F']