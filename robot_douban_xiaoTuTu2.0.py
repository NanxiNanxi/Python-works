import requests
import json
import random
import time

#headers get from Douban APP (need to be aware of ssl)
postHeaders = {
    'Authorization': 'Bearer *****',
    'User-Agent': '**********',
    'Content-Type': '*******************',
    'Host': 'frodo.douban.com',
    'Accept-Encoding': '****'
}


comments = [
    <Your comment dictionary>

]

commentParams = {
        'text': <get a random comment from comments>
    }

grpurl =<API grap from Douban APP>


def getGroupJsonData(groupUrl, header):
    page = requests.get(groupUrl, headers=header, verify=False).json()
    dataStr = json.dumps(page)
    data = json.loads(dataStr)
    return data

if __name__ == "__main__":
    while True:
        data = getGroupJsonData(grpurl, getHeaders)
        postedTopic = None
        i = 0
        while i != 20:
            #get topic number
            if int(data['topics'][i]['comments_count']) < 3:
                topicNum = data['topics'][i]['url'].split('topic/')[1].split('/')[0]
                #if this topic is different from the topic robot replied last time, then post a comment
                if topicNum != postedTopic:
                    commentUrl = f'https://frodo.douban.com/api/v2/group/topic/{topicNum}/create_comment'
                    response = requests.post(commentUrl, headers=postHeaders,verify = False,data=commentParams)
                    postedTopic = topicNum
                    time.sleep(120)
                    break
            else:
                pass
            i = i+1
        time.sleep(60)

