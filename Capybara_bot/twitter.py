import tweepy
import time
from intro import bienvenue 
from phrase import sentence
import random
from random import randrange


#clés d'authentification
api_key = "XXXXXXXXXXXXXXXXX"
api_secret = "XXXXXXXXXXXXXXXXXXXXXX"
bearer_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client_id = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
client_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

Client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret, wait_on_rate_limit=False)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)



# fait appel à l'API d'authentification:
api= tweepy.API(Client, wait_on_rate_limit=True)



n=0

url_id = input("Veuillez entrez le lien du tweet : ")

#Fonction de cisaillement permettant d'obtenir l'ID automatiquement:
while url_id[n] != '/': 
    url_id[n+1]
    n= n-1
    id_answer = url_id[n+1:]
    
#pioche un nombre aléatoire en fonction du nombre d'éléments dans la liste:    
for index, element in enumerate(sentence):
    p = index 

n = randrange(p)
 

#permet de répondre à un tweet:
Client.create_tweet(in_reply_to_tweet_id= id_answer, text=sentence[n])


