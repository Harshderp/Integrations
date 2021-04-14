#Readme file before going through the code!
#!pip install tweepy  #uncomment this line to install a library('tweepy') that will be used to tweet on twitter.


import tweepy
def OAuth(accessKey, accessKeySecret, accessToken, accessTokenSecret):
    try:
        auth = tweepy.OAuthHandler(ak,aks)
        auth.set_access_token(at,ats)
        return auth
        
    except Exception as e:
        return none
 
oauth = OAuth(Your accessKey, Your accessKeySecret, Your accessToken, Your accesstokenSecret)
apicall = tweepy.API(oauth)
 
apicall.update_status('Here is a sample tweet from API call program. Harshdeep')
print ('Tweet Created')
