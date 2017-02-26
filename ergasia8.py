import tweepy
from tweepy import OAuthHandler

def gettwitterapi():
    ckey = 'wN3EkGACO0UMmjKK6JralEf0T'
    csecret = 'mw7wydVFjL9ZpyrLAL2TGBESSc3tKguZ7OwX9ZRgeTrS4NPwbM'
    atoken = '834115247770333184-IrthQKNkJlk9ccrXfBPO1fjrx0vHC5p'
    asecret = '9mEOXpf8RIkxb6f6Sj17yCkkYv70JzAdkqedRkG2bIfl3'
    auth = tweepy.OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    return tweepy.API(auth)
    
def getfollowersids(api,username):
    ids = []
    pages = tweepy.Cursor(api.followers_ids, screen_name=username).pages()
    for page in pages:
        ids.extend(page)
    return ids 

api = gettwitterapi()

fuser= raw_input ("first user: ")
fids = getfollowersids(api, fuser)
print "%s total followers: "%(fuser)+str(len(fids))

suser = raw_input ("second user: ")
sids = getfollowersids(api, suser)
print "%s total followers: "%(suser)+str(len(sids))

samefollowers = list(set(fids).intersection(sids))
print "samefollowers: "+str(samefollowers)
