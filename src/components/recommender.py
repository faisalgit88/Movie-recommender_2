import os
import sys
# from src.exception import CustomException
# from src.logger import logging
import pandas as pd
from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    recommender_file_path=os.path.join("model","tmdb.csv")

class recommendation:
    def __init__(self):
        self.recommendation_config=ModelTrainerConfig()
         
    def get_recommendations(title):
        try:
            logging.info("Recommendation initiated")

            cosine_sim = cosine_similarity(count_matrix, count_matrix)
            idx = indices[title]
            sim_scores = list(enumerate(cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:11]
            movie_indices = [i[0] for i in sim_scores]
            tit = df2['title'].iloc[movie_indices]
            dat = df2['release_date'].iloc[movie_indices]
            rating = df2['vote_average'].iloc[movie_indices]
            moviedetails=df2['overview'].iloc[movie_indices]
            movietypes=df2['keywords'].iloc[movie_indices]
            movieid=df2['id'].iloc[movie_indices]
        
            return_df = pd.DataFrame(columns=['Title','Year'])
            return_df['Title'] = tit
            return_df['Year'] = dat
            return_df['Ratings'] = rating
            return_df['Overview']=moviedetails
            return_df['Types']=movietypes
            return_df['ID']=movieid

            return return_df
        
        except Exception as e:
            raise CustomException(e,sys)

    def get_suggestions():
        data = pd.read_csv('tmdb.csv')
        return list(data['title'].str.capitalize())
