import os
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Import and filter the dataset
dataset = pd.read_csv(os.path.join(os.curdir, 'movies.csv'))
dataset.dropna(inplace=True)
columns = ['keywords', 'original_title', 'cast', 'genres', 'overview']
for col in columns:
    dataset[col] = dataset[col].apply(lambda x: re.sub('[|,!?.]', ' ', x.lower()))
dataset['tags'] = dataset[columns].agg(' '.join, axis=1)

# Vectorization of Required Coluumns
cv = CountVectorizer(max_features=20000, stop_words='english')
vector = cv.fit_transform(dataset['tags'].values.astype('U')).toarray()

# Creating similarity matrix (Collaborative filtering)
similarity_matrix = cosine_similarity(vector)

class MovieRecommendation:
    def __init__(self, category: str, value: str) -> None:
        self.category = self._find_category(category)
        self.value = value.lower()

    def _find_category(self, category: str) -> str:
        match category.lower():
            case 'name':
                return 'original_title'
            case 'genre':
                return 'genres'
            case 'keyword':
                return 'keywords'
            case 'cast':
                return 'cast'

    def recommend(self, count: int) -> list:
        movies = []
        try:
            index = dataset[dataset[self.category].str.contains(self.value)].index[0]
            distance = sorted(list(enumerate(similarity_matrix[index])), reverse=True, key=lambda x: x[1])
            for idx,_ in distance[:count]:
                movies.append({
                    'id': dataset.iloc[idx].id,
                    'title': dataset.iloc[idx].original_title,
                    'imdb_id': dataset.iloc[idx].imdb_id,
                    'image': 'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbDl6bTZvM3g5YWw1b3lqaHh5dzh5OXkydTBqenI4OHd3N3pycnhiciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xTk9ZvMnbIiIew7IpW/giphy.gif'
                })
        except IndexError:
            movies = None
        return movies

