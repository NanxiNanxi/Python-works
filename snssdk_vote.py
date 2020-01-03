import requests
import json
import pandas as pd
import time
from datetime import datetime
import pytz
import urllib
#调用api接口
def dorequest(url):
    try:
        response = urllib.request.urlopen(url, timeout=10).read()
    except urllib.error.HTTPError as e:
        response = e.fp.read()
    result = json.loads(str(response, encoding='utf-8'))
    return result


if __name__ == "__main__":
    voteDict = {}
    voteBefore = 0
    vote = 0
    url = '<API from snssdk's App>'

    df0k = pd.DataFrame(columns=['日期', '第一', '票数', '新增'])
    df1k = pd.DataFrame(columns=['日期', '第二', '票数', '新增'])
    df2k = pd.DataFrame(columns=['日期', '第三', '票数', '新增'])
    df3k = pd.DataFrame(columns=['日期', '第四', '票数', '新增'])
    df0q = pd.DataFrame(columns=['日期', '第一', '票数', '新增'])
    df1q = pd.DataFrame(columns=['日期', '第二', '票数', '新增'])
    df2q = pd.DataFrame(columns=['日期', '第三', '票数', '新增'])
    df3q = pd.DataFrame(columns=['日期', '第四', '票数', '新增'])
    while True:
        data = dorequest(url)
        dataStr = json.dumps(data)
        data = json.loads(dataStr)
        currentChineseTime = datetime.now().astimezone(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
        print(currentChineseTime)
        i=0
        while i != 4:
            kingName = data['data']['popular_male_star'][i]['name']
            kingTotalVote = data['data']['popular_male_star'][i]['ticket']
            queenName = data['data']['popular_female_star'][i]['name']
            queenTotalVote = data['data']['popular_female_star'][i]['ticket']

            if (kingName not in voteDict):
                voteDict[kingName] = 0
                voteDict[queenName] = 0
            kingIncrease = int(kingTotalVote) - voteDict[kingName]
            queenIncrease = int(queenTotalVote) - voteDict[queenName]
            if i == 0:
                dfNewRowK = pd.Series(
                    {'日期': currentChineseTime, '第一': kingName, '票数': int(kingTotalVote), '新增': kingIncrease})
                df0k = df0k.append(dfNewRowK, ignore_index=True)
                df0k.to_csv('C:/Users/nancy/Desktop/dev/output/toutiaoking1.csv', index=False, mode='w',
                            encoding="utf_8_sig")
                dfNewRowQ = pd.Series(
                    {'日期': currentChineseTime, '第一': queenName, '票数': int(queenTotalVote), '新增': queenIncrease})
                df0q = df0q.append(dfNewRowQ, ignore_index=True)
                df0q.to_csv('C:/Users/nancy/Desktop/dev/output/toutiaoqueen1.csv', index=False, mode='w',
                            encoding="utf_8_sig")
            if i == 1:
                dfNewRowK = pd.Series(
                    {'日期': currentChineseTime, '第二': kingName, '票数': int(kingTotalVote), '新增': kingIncrease})
                df1k = df1k.append(dfNewRowK, ignore_index=True)
                df1k.to_csv('C:/Users/nancy/Desktop/dev/output/toutiaoking2.csv', index=False, mode='w',
                            encoding="utf_8_sig")
                dfNewRowQ = pd.Series(
                    {'日期': currentChineseTime, '第二': queenName, '票数': int(queenTotalVote), '新增': queenIncrease})
                df1q = df1q.append(dfNewRowQ, ignore_index=True)
                df1q.to_csv('C:/Users/nancy/Desktop/dev/output/toutiaoqueen2.csv', index=False, mode='w',
                            encoding="utf_8_sig")
            if i == 2:
                dfNewRowK = pd.Series(
                    {'日期': currentChineseTime, '第三': kingName, '票数': int(kingTotalVote), '新增': kingIncrease})
                df2k = df2k.append(dfNewRowK, ignore_index=True)
                df2k.to_csv('C:/Users/nancy/Desktop/dev/output/king3.csv', index=False, mode='w',
                            encoding="utf_8_sig")
                dfNewRowQ = pd.Series(
                    {'日期': currentChineseTime, '第三': queenName, '票数': int(queenTotalVote), '新增': queenIncrease})
                df2q = df2q.append(dfNewRowQ, ignore_index=True)
                df2q.to_csv('C:/Users/nancy/Desktop/dev/output/toutiaoqueen3.csv', index=False, mode='w',
                            encoding="utf_8_sig")
            if i == 3:
                dfNewRowK = pd.Series(
                    {'日期': currentChineseTime, '第四': kingName, '票数': int(kingTotalVote), '新增': kingIncrease})
                df3k = df3k.append(dfNewRowK, ignore_index=True)
                df3k.to_csv('C:/Users/nancy/Desktop/dev/output/toutiaoking4.csv', index=False, mode='w',
                            encoding="utf_8_sig")
                dfNewRowQ = pd.Series(
                    {'日期': currentChineseTime, '第四': queenName, '票数': int(queenTotalVote), '新增': queenIncrease})
                df3q = df3q.append(dfNewRowQ, ignore_index=True)
                df3q.to_csv('C:/Users/nancy/Desktop/dev/output/toutiaoqueen4.csv', index=False, mode='w',
                            encoding="utf_8_sig")

            voteDict[kingName] = int(kingTotalVote)
            voteDict[queenName] = int(queenTotalVote)
            i = i + 1

        time.sleep(60)


