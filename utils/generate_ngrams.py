import pandas as pd
import numpy as np
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer
from utils.preprocessing import get_texts, stop_words

# Use this to read pkl
# with open('data/n_grams/{}_{}.pkl'.format(sector, score_type), 'rb') as handle:
#     feature_names = pickle.load(handle)

ticker_library = pd.read_csv(os.path.join("data", "tickers.csv"))

def get_cik(ticker):
    """ Get the cik for the ticker specified by the input argument 
    Input:
        ticker(str): ticker of the company e.g. "FB"
    """
    return ticker_library[ticker_library.ticker == ticker].secfilings.values[0][-10:]

def get_ciks(tickers):
    ciks = []

    for ticker in tickers:
        ciks.append(get_cik(ticker))

    return ciks

df_esg_score = pd.read_excel("data/esg_score.xlsx", sheet_name = "data")

sectors = ['Consumer Cyclical', 'Energy', 'Industrials', 'Healthcare',
       'Basic Materials', 'Consumer Defensive', 'Utilities', 'Technology',
       'Financial Services', 'Communication Services', 'Real Estate']
score_types = ["governanceScore", "environmentScore", "socialScore"]
not_listed = ["BBWI"]

for sector in sectors:
    for score_type in score_types:
        esgs = df_esg_score[df_esg_score["sector"] == sector][["Company", "socialScore", "governanceScore", "environmentScore"]]
        score = esgs[score_type]
        alpha = 0.3
        upper_score = np.quantile(score, 1 - alpha)
        lower_score = np.quantile(score, alpha)

        bad_companies = list(esgs[esgs[score_type] > upper_score]["Company"].values)
        good_companies = list(esgs[esgs[score_type] < lower_score]["Company"].values)

        for t in not_listed:
            if t in bad_companies:
                bad_companies.remove(t)
            if t in good_companies:
                good_companies.remove(t)

        tickers = good_companies + bad_companies
        ciks = get_ciks(tickers)
        ret = get_texts(ciks, tickers)
        docs = ret["docs"]
        
        n_min = 2
        n_max = 3
        cv = CountVectorizer(max_df=0.7, stop_words=stop_words, max_features=200, ngram_range=(n_min, n_max))
        word_count_vector = cv.fit_transform(docs)
        feature_names = cv.get_feature_names()

        with open('data/n_grams/{}_{}.pkl'.format(sector, score_type), 'wb') as handle:
            pickle.dump(feature_names, handle, protocol=pickle.HIGHEST_PROTOCOL)