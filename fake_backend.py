import json
from collections import namedtuple
import arrow
from uuid import uuid4

'''
Just building this up a step at a time.
'''


_vote = '''
{
  "VoteHeader" : {
    "vote_id" : "200",
    "name" : null,
    "owner" : "Ian Joicey",
    "is_public" : true,
    "created_dt" : null,
    "last_update_dt" : null,
    "expiry_dt" : null,
    "has_expired" : null,
    "total_votes" : 67,
    "category" : "Programming",
    "sub_category" : "Languages",
    "Vote" : {
      "question" : "What is your favoriate language?",
      "vote_type" : 0,
      "default_id" : -1,
      "voted_id" : -1,
      "help" : "Lets see who likes what language",
      "answers" : [
        {
          "id" : 1,
          "title" : "Python 2.7",
          "subtitle" : "Version 3",
          "votes_to_date" : 0
        },

        {
          "id" : 2,
          "title" : "Python 3.6",
          "subtitle" : "Version 2",
          "votes_to_date" : 0
        },

        {
          "id" : 3,
          "title" : "C++",
          "subtitle" : "",
          "votes_to_date" : 0
        },

        {
          "id" : 4,
          "title" : "Java",
          "subtitle" : "",
          "votes_to_date" : 0
        },

        {
          "id" : 5,
          "title" : "Javascript",
          "subtitle" : "",
          "votes_to_date" : 0
        }
      ]
    }
  }
}
'''


class VoteDataClass():
    _answer_flds = 'id, title, subtitle, votes_to_date'
    AnswerRecord = namedtuple('AnswerRecord', _answer_flds)

    def __init__(self, json_str=None):
        # header
        self.vote_id = ''  # uuid 4
        self.name = ''
        self.owner = ''
        self.is_public = ''
        self.created_dt = ''
        self.last_update_dt = False
        self.expiry_dt = None
        self.has_expired = None
        self.category = -1
        self.sub_category = 0
        self.total_votes = 0
        self.language = ""

        # vote
        self.question = ''
        self.vote_type = -1
        self.default_id = 0  # select one
        self.voted_id = None
        self.help = ""

        # answers
        self.answers = []  # a list of namedtuples

        if json_str:
            self.parse_json(json_str)

    def parse_json(self, json_str):
        '''
            populate the class with the json string recived from the server.
        '''
        vote_dict = json.loads(json_str)

        head = vote_dict['VoteHeader']
        for k, v in head.items():
            if hasattr(self, k):
                setattr(self, k, v)

        vote = head['Vote']
        for k, v in vote.items():
            if hasattr(self, k):
                setattr(self, k, v)

        answers = vote['answers']
        for ans in answers:
            # TODO: Not sure whats going on here!
            _ = self.AnswerRecord(**ans)
            # self.answers.append(ans_nt)

    def __repr__(self):
        # TODO: do something nice here
        pass


def fake_vote_record():
    rec = VoteDataClass(_vote)
    # do a few things to the fake record
    rec.vote_id = str(uuid4())
    utc_time = arrow.utcnow()
    rec.created_dt = str(utc_time)
    rec.last_update_dt = rec.created_dt
    rec.expiry_dt = utc_time.shift(hours=1)
    return rec

if __name__ == '__main__':
    vc = fake_vote_record()
    for k, v in vc.__dict__.items():
        print('{:>10} {}'.format(k, v))
