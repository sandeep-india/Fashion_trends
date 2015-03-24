from twitter import *
from threading import Timer
import nltk
import time

mins =0

token = '319175103-JkoQuf6N8LvRNIwbjOKwltLulldFzCgxNuwb5PpQ'
token_key = 'QtFCPe83WHMm9OipOXN0s8bEfQ63NWGcrLrs9df1xTp6o'
con_secret = 'ltV1pu46OfalumpIDJJy1gUFJ'
con_secret_key = 'PuKWVkxuplwMtJLN0fuuIvguJV5ArzMbUrFWihEWKMZZoxUVqv'

tracked = 'trousers'

t = Twitter(auth = OAuth(token, token_key, con_secret, con_secret_key))
twitter_stream = TwitterStream(auth = OAuth(token, token_key, con_secret, con_secret_key))

hairtrends = []

iterator = twitter_stream.statuses.filter(track=tracked)

for tweet in iterator:
	sentence = tweet['text']
	tokens = sentence.split()
	if tracked in tokens:
		position = ((tokens.index(tracked))-1)
		tagged = nltk.pos_tag(tokens)
		# print tagged
		if position >= 0:
			if tagged[position][1] == 'NN':
				hairtrends.append((tagged[position][0]))
				print hairtrends


