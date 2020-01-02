# Python-works
This is a repository for Python works

1. Sina_vote_Yingxiangli.py
  This is a spider script for getting result from a Sina page every 30 second (did not count the loading time)
2. weibo_vote_king&queen.py
  This is a spider script for getting result from a Weibo page every 60 second
3. robot_douban_xiaoTuTu.py
  This is a simple logic robot for Douban. 
  It can find the posts on Douban groups which have no reply comment yet and post the first comment.
  According to Douban's anti-spider mechanism, if the robot post 3 comments within 1 minutes, you may get a vertification pic. 
  Since I have not find a good ocr to deal with it, I put about 1.5 minute's waiting time between each comment.
4. recordToBeRecorded folder
  contains three spider scripts (for WeiboKingQueenVote result/ WeiboAnnualNominee / Annual Influencer celeberaties), get the voting result and output the record to csv. csvToExcel is a script for converting several csv files to one excel with several sheets
