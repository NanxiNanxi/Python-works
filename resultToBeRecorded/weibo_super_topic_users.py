import requests
# from pyquery import PyQuery as pq
import pprint
import random
import datetime
import pandas as pd
from MyModels import Weibo_user
from MyModels import topic_by_research_parse_result
import pytz

user_agent = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",

]


def get_user_agent():
    return random.choice(user_agent)


def get_html(webpage):
    header = get_user_agent()
    html = requests.get(webpage, header).json()
    return html


def get_since_id(json):
    since_id = html["data"]["cardlistInfo"].get("since_id")
    return since_id


def print_to_excel():
    currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def parse_html(json):
    cards = html["data"]["cards"]
    super_topic_posts = {}
    new_post_list = []
    uids = []
    ObjParseResult = None
    # some mblog are embedded inside of a card_group, but most of them are not
    for card in cards:
        card_group = card.get("card_group")
        if card_group:
            for single_card in card_group:
                mblog = single_card.get("mblog")
                if mblog:
                    super_topic_posts["uid"] = mblog["user"]["id"]
                    super_topic_posts["username"] = mblog["user"]["screen_name"]
                    super_topic_posts["followers"] = mblog["user"]["followers_count"]
                    super_topic_posts["text"] = mblog["raw_text"].replace('\n', ' ')
                    super_topic_posts["comments"] = mblog["comments_count"]
                    super_topic_posts["created at"] = mblog["created_at"]
                    super_topic_posts["hasZhuYilong"] = '否'
                    if '朱一龙' in super_topic_posts["text"]:
                        super_topic_posts["hasZhuYilong"] = '是'
                        uids.append(super_topic_posts["uid"])
                    dfNewRow = pd.Series({'uid': super_topic_posts["uid"], 'username': super_topic_posts["username"],
                                          'followers': super_topic_posts["followers"],
                                          'post': super_topic_posts["text"], 'comments': super_topic_posts["comments"],
                                          'created at': super_topic_posts["created at"],
                                          'hasZhuYilong': super_topic_posts["hasZhuYilong"]})
                    new_post_list.append(dfNewRow)

        if not card_group:
            mblog = card.get("mblog")
            if mblog:
                super_topic_posts["uid"] = mblog["user"]["id"]
                super_topic_posts["username"] = mblog["user"]["screen_name"]
                super_topic_posts["followers"] = mblog["user"]["followers_count"]
                super_topic_posts["text"] = mblog["raw_text"].replace('\n', ' ')
                super_topic_posts["comments"] = mblog["comments_count"]
                super_topic_posts["created at"] = mblog["created_at"]
                super_topic_posts["hasZhuYilong"] = '否'
                if '朱一龙' in super_topic_posts["text"]:
                    super_topic_posts["hasZhuYilong"] = '是'
                    uids.append(super_topic_posts["uid"])
                dfNewRow = pd.Series({'uid': super_topic_posts["uid"], 'username': super_topic_posts["username"],
                                      'followers': super_topic_posts["followers"], 'post': super_topic_posts["text"],
                                      'comments': super_topic_posts["comments"],
                                      'created at': super_topic_posts["created at"],
                                      'hasZhuYilong': super_topic_posts["hasZhuYilong"]})
                new_post_list.append(dfNewRow)

    ObjParseResult = topic_by_research_parse_result(new_post_list, uids)
    return ObjParseResult


def parse_weibo_account(json):
    uid = None
    username = None
    creatAt = None
    description = None
    followersCount = None
    gender = None
    isVerified = None
    verifiedReason = None
    frequentlyTags = None
    tagList = []
    weiboList = []
    post = None
    postInTopic = None
    comments = None

    cards = json["data"]["cards"]
    for card in cards:
        card_group = card.get("card_group")
        if card_group:
            for single_card_group in card_group:
                groups = single_card_group["group"]
                if groups:
                    for group in groups:
                        tagList.append(group["title_sub"])
        if tagList.count != 0:
            frequentlyTags = " ".join(tagList)

        mblog = card.get("mblog")
        if mblog:
            creatAt = mblog["created_at"]
            followersCount = mblog["user"]["followers_count"]
            uid = mblog["user"]["id"]
            username = mblog["user"]["screen_name"]
            print(username)
            gender = mblog["user"]["gender"]
            isVerified = mblog["user"]["verified"]
            if isVerified:
                verifiedReason = mblog["user"]["verified_reason"]
            source = mblog.get("source")
            if source:
                postInTopic = source
            post = mblog["raw_text"].replace('\n', ' ')
            comments = mblog["comments_count"]
            description = mblog["user"]["description"]
            weiboUser = Weibo_user(uid, username, creatAt, description, followersCount, gender, isVerified,
                                   verifiedReason, frequentlyTags, post, postInTopic, comments)
            print(f"in group {weiboUser.uid}")
            weiboList.append(weiboUser)

    return weiboList


since_id = ""
pageLimit = 10
postLimit = 30
url = "https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E9%87%8D%E5%90%AF%E4%B9%8B%E6%9E%81%E6%B5%B7%E5%90%AC%E9%9B%B7&page_type=searchall"
post_dataframe = pd.DataFrame(
    columns=['uid', 'username', 'followers', 'post', 'comments', 'created at', 'hasZhuYilong'])
page = 0
while page != pageLimit:
    if page != 0:
        url = f"{url}&page={page+1}"
    html = get_html(url)
    obj_parseResult = parse_html(html)
    new_post_list = obj_parseResult.dataRowList
    for post in new_post_list:
        post_dataframe = post_dataframe.append(post, ignore_index=True)
    page = page + 1

currentChineseTime = datetime.datetime.now().astimezone(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d_%H%M%S')
post_dataframe.to_csv(
    f'C:\\Users\\nancy\\Desktop\\DataAnalyze\\Spiders\\output\\chongqi_posts_{currentChineseTime}.csv', index=False,
    mode='w', encoding="utf_8_sig")
uids = obj_parseResult.uids
user_post_dataframe = pd.DataFrame(
    columns=["uid", "username", "creatAt", "description", "followersCount", "gender", "isVerified", "verifiedReason",
             "frequentlyTags", "post", "postInTopic", "comments"])

for uid in uids:
    print(uid)
    userPage_url = f"https://m.weibo.cn/api/container/getIndex?type=uid&value={uid}&containerid=107603{uid}"
    print(userPage_url)
    counter = 0
    while counter != postLimit:
        if counter != 0:
            since_id = user_html["data"]["cardlistInfo"].get("since_id")
            print(since_id)
            if since_id:
                userPage_url = f"{userPage_url}&since_id={since_id}"
        header = get_user_agent()
        parse_result = requests.get(userPage_url, header)
        user_html = parse_result.json()
        user_post_list = parse_weibo_account(user_html)
        for userPost in user_post_list:
            userDataRow = pd.Series({"uid": userPost.uid, "username": userPost.username, "creatAt": userPost.creatAt,
                                     "description": userPost.description, "followersCount": userPost.followersCount,
                                     "gender": userPost.gender, "isVerified": userPost.isVerified,
                                     "verifiedReason": userPost.verifiedReason,
                                     "frequentlyTags": userPost.frequentlyTags, "post": userPost.post,
                                     "postInTopic": userPost.postInTopic, "comments": userPost.comments})
            user_post_dataframe = user_post_dataframe.append(userDataRow, ignore_index=True)
        counter = counter + 1

currentChineseTime = datetime.datetime.now().astimezone(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d_%H%M%S')
user_post_dataframe.to_csv(
    f'C:\\Users\\nancy\\Desktop\\DataAnalyze\\Spiders\\output\\user_posts_{currentChineseTime}.csv', index=False,
    mode='w', encoding="utf_8_sig")





