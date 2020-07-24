
class Weibo_user:
    def __init__(self,uid,username,creatAt,description, followersCount,gender,isVerified, verifiedReason,frequentlyTags,post,postInTopic,comments):
        self.uid = uid
        self.username = username
        self.creatAt = creatAt
        self.description = description
        self.followersCount = followersCount
        self.gender = gender
        self.isVerified = isVerified
        self.verifiedReason = verifiedReason
        self.frequentlyTags = frequentlyTags
        self.post = post
        self.postInTopic = postInTopic
        self.comments = comments

class topic_by_research_parse_result:
    def __init__(self,dataRowList,uids):
        self.dataRowList = dataRowList
        self.uids = uids