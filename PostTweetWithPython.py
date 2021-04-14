#Readme file before going through the code!
!pip install tweepy  #run this line once to install tweepy libary.
# once installed remove the above line from your code.

import tweepy
def OAuth(accessKey, accessKeySecret, accessToken, accessTokenSecret):
    try:
        auth = tweepy.OAuthHandler(ak,aks)
        auth.set_access_token(at,ats)
        return auth
        
    except Exception as e:
        return none
 
oauth = OAuth(accessKey, accessKeySecret, accessToken, accesstokenSecret) #replace accesskey with your accesskey generated after creating the app, replace all with the required values and put the values in '').
apicall = tweepy.API(oauth)
 
apicall.update_status('Here is a sample tweet from API call program. Harshdeep')
print ('Tweet Created')
