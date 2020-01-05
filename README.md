# Python-works
* This is a repository for Python works

### Sina_vote_Yingxiangli.py   
* This is a spider script for getting result from a Sina page every 30 second (did not count the loading time)
  ---
### weibo_vote_king&queen.py  
* This is a spider script for getting result from a Weibo page every 60 second
---
### robot_douban_xiaoTuTu.py  
  * This is a simple logic robot for Douban. It can find the posts on Douban groups which have no reply comment yet and post the first comment.According to Douban's anti-spider mechanism, if the robot post 3 comments within 1 minutes, you may get a vertification pic. Since I have not find a good ocr to deal with it, I put about 1.5 minute's waiting time between each comment.
---
### robot_douban_xiaoTuTu2.0.py   
* Douban has a anti-spider machanism, so we may have to use the APP api to do the get and post process, this is ver2.0 which is using api
---
### resultToBeRecorded folder   
* contains three spider scripts (for WeiboKingQueenVote result/ WeiboAnnualNominee / Annual Influencers(yingxiangli.py)), get the voting result and output the record to csv. csvToExcel is a script for converting several csv files to one excel with several sheets
---
### snssdk.py   
  * This is a spider script to get the voting result from snssdk's mobile App. Use fiddler to grab the package and find the api for the result page, then parse it and get the result, finally output result to csv
---
