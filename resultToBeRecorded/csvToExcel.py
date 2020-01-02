import pandas as pd
import pytz
from datetime import datetime

'''
Tyoe Number:
king&queen: 1
影响力：2
年度人物：3

'''
def findDocToGo(typeNum):
    currentChineseTime = datetime.now().astimezone(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
    if typeNum ==1:
        df1k = pd.read_csv('/Users/lanzhou/Desktop/test/needToGo/king1.csv')
        df2k = pd.read_csv('/Users/lanzhou/Desktop/test/needToGo/king2.csv')
        df3k = pd.read_csv('/Users/lanzhou/Desktop/test/needToGo/king3.csv')
        df4k = pd.read_csv('/Users/lanzhou/Desktop/test/needToGo/king4.csv')
        df1q = pd.read_csv('/Users/lanzhou/Desktop/test/needToGo/king1.csv')
        df2q = pd.read_csv('/Users/lanzhou/Desktop/test/needToGo/king2.csv')
        df3q = pd.read_csv('/Users/lanzhou/Desktop/test/needToGo/king3.csv')
        df4q = pd.read_csv('/Users/lanzhou/Desktop/test/needToGo/king4.csv')
        fileNameK = f'WeiboKing{currentChineseTime}.xlsx'
        fileNameQ = f'WeiboQueen{currentChineseTime}.xlsx'
    if typeNum ==2:
        df1 = pd.read_csv('/Users/lanzhou/Desktop/test/needToGo/yingxiangli1.csv')
        df2 = pd.read_csv('/Users/lanzhou/Desktop/test/needToGo/yingxiangli2.csv')
        df3 = pd.read_csv('/Users/lanzhou/Desktop/test/needToGo/yingxiangli3.csv')
        df4 = pd.read_csv('/Users/lanzhou/Desktop/test/needToGo/yingxiangli4.csv')
        fileName = f'WeiboYingXiangLi{currentChineseTime}.xlsx'
    if typeNum ==3:
        df1 = pd.read_csv('/Users/lanzhou/Desktop/test/needToGo/niandu1.csv')
        df2 = pd.read_csv('/Users/lanzhou/Desktop/test/needToGo/niandu2.csv')
        df3 = pd.read_csv('/Users/lanzhou/Desktop/test/needToGo/niandu3.csv')
        df4 = pd.read_csv('/Users/lanzhou/Desktop/test/needToGo/niandu4.csv')
        fileName = f'WeiboAnnualNominee{currentChineseTime}.xlsx'

    try:
        if typeNum ==1:
            with pd.ExcelWriter(fileNameK) as writer:
                df1k.to_excel(writer,'第一',index = False)
                df2k.to_excel(writer,'第二',index=False)
                df3k.to_excel(writer,'第三',index=False)
                df4k.to_excel(writer,'第四',index=False)
            with pd.ExcelWriter(fileNameQ) as writer:
                df1q.to_excel(writer,'第一',index = False)
                df2q.to_excel(writer,'第二',index=False)
                df3q.to_excel(writer,'第三',index=False)
                df4q.to_excel(writer,'第四',index=False)

        else:
            with pd.ExcelWriter(fileName) as writer:
                df1.to_excel(writer,'第一',index = False)
                df2.to_excel(writer,'第二',index=False)
                df3.to_excel(writer,'第三',index=False)
                df4.to_excel(writer,'第四',index=False)

    except FileNotFoundError:
        pass
    
findDocToGo(2)