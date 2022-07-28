import snscrape.modules.twitter as sntwitter
import pandas as pd
import random

query = "from: until:now since:2022-01-01"
tweets = []
content = []
difference = []
binary = []
octet = []
result = []
limit = 100

def generate():
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        
        # print(vars(tweet))
        # break
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.date, tweet.user.username, tweet.content])
            content.append(len(tweet.content))
            
    df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
    dg = pd.DataFrame(content)

    for i in range(0, len(content)-1):
        difference.append(content[i + 1] - content[i])

    for i in difference:
        if(i > 0):
            binary.append(1)
        
        elif(i < 0):
            binary.append(0)

    n = 8

    for i in range(0, len(binary), n):
        octet.append(binary[i:i+8])

    for i in range(0, len(octet)):
        number = str(''.join(str(e) for e in octet[i]))
        dec_number = int(number, 2)
        result.append(dec_number)

    return int(result[random.randint(0, len(result) - 1)])

