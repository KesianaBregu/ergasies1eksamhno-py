import tweepy

def countwords(tweets):
	totalwords = 0
	for i in range(len(tweets)):
		text = tweets[i].text
		countwords = len(text.split())
		totalwords += countwords
	return totalwords
	
def gettwitterapi():
	ckey = 'wN3EkGACO0UMmjKK6JralEf0T'
	csecret = 'mw7wydVFjL9ZpyrLAL2TGBESSc3tKguZ7OwX9ZRgeTrS4NPwbM'
	atoken = '834115247770333184-IrthQKNkJlk9ccrXfBPO1fjrx0vHC5p'
	asecret = '9mEOXpf8RIkxb6f6Sj17yCkkYv70JzAdkqedRkG2bIfl3'

	auth = tweepy.OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)
	return tweepy.API(auth)
	
api = gettwitterapi()

fuser = raw_input ("First user:")
suser = raw_input ("Second user:")
	
tweetsoffirst = api.user_timeline(screen_name = fuser,count=10)

totalwordsoffirst = countwords(tweetsoffirst)

tweetsofsec = api.user_timeline(screen_name = suser,count=10)

totalwordsofsec = countwords(tweetsofsec)
	
print "%s total words = "%(fuser)+ str(totalwordsoffirst)
print "%s total words = "%(suser)+ str(totalwordsofsec)
	
if (totalwordsoffirst < totalwordsofsec):
	print "%s is winner!"%(suser)
elif (totalwordsoffirst > totalwordsofsec):
	print "%s is winner!"%(fuser)
else :
	print "its a draw"
	

	
	
	