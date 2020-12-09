import praw

subreddit_list = ['funny','askreddit','gaming','aww','pics','science','worldnews','news','music','videos','movies','todayilearned','showerthoughts','iama','gifs','books']

reddit = praw.Reddit(client_id="_f6T1aPrwfeugw",
                     client_secret="eNmlFBwuITKGemz_Ua53eZqc8VU-vQ",
                     password="-------Password---------",
                     user_agent="testscript by u/fakebot3",
                     username="dfusiauewhiufn")


target = open("data.txt", 'w') # Open file
target.truncate()
count = 0

for x in range(1000000):
        for sub in subreddit_list:
                for comment in reddit.subreddit(sub).comments(limit=2):
                        target.write(comment.body)
                        target.write('\n'*10)
                        print(count)
                        count += 1


target.close()
