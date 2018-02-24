import numpy as np
import pandas as pd
# Import the CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

text = [
    "Go until jurong point, crazy.. Available only …",
    "Ok lar… Joking wif u oni…",
    "Free entry in 2 a wkly comp to win FA Cup fina…",
    "U dun say so early hor… U c already then say…",
    "Nah I don’t think he goes to usf, he lives aro..."]

text = [
    "Le lièvre mange des fraises.",
    "Pierre est un lièvre et il a des fraises à proximité. C'est une aubaine pour un lièvre. Lièvre. Fraise.",
    "Pierre mange des fraises. "
]
# Create the basic token pattern
TOKENS_BASIC = '\\S+(?=\\s+)'

# Create the alphanumeric token pattern
TOKENS_ALPHANUMERIC = '[A-Za-z0-9éè]+(?=\\s+|.)'

# Instantiate basic CountVectorizer: vec_basic
vec_basic = CountVectorizer(token_pattern=TOKENS_BASIC)

# Instantiate alphanumeric CountVectorizer: vec_alphanumeric
vec_alphanumeric = CountVectorizer(token_pattern=TOKENS_ALPHANUMERIC,strip_accents=None)

# Fit and transform vec_basic
vec_basic.fit_transform(text)

# Print number of tokens of vec_basic
print("There are {} tokens in the dataset".format(len(vec_basic.get_feature_names())))

# Fit and transform vec_alphanumeric
vec_alphanumeric.fit_transform(text)

# Print number of tokens of vec_alphanumeric
print("There are {} alpha-numeric tokens in the dataset".format(len(vec_alphanumeric.get_feature_names())))

# Print number of tokens of vec_basic
print("\n\nTokens in the dataset", vec_basic.get_feature_names())

# Print number of tokens of vec_alphanumeric
print("\n\nAlpha-numeric tokens in the dataset", vec_alphanumeric.get_feature_names())

result = set(vec_basic.get_feature_names()) - set(vec_alphanumeric.get_feature_names())

print(result)

sentence3 = text[1]
print(vec_alphanumeric.transform([sentence3]))
print(vec_alphanumeric.get_feature_names()[15])
