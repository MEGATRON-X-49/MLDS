data['len'] = np.array([len(tweet.text) for tweet in tweets])
data['ID'] = np.array([tweet.id for tweet in tweets])
data['Date'] = np.array([tweet.created for tweet in tweets])
data['Source'] = np.array([tweet.cource for tweet in tweets])
data['Likes'] = np.array([tweet.favourite_count for tweet in tweets])
data['RTS'] = np.array([tweet.retweet_count for tweet in tweets])
