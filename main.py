import json
import praw


class FleuryEtBot:
    def __init__(self, loginfo):
        try:
            with open(loginfo, 'r') as jsonlog:
                log = json.load(jsonlog)
            if log['user_agent'] == "example":
                self.reddit = None
            else:
                self.reddit = praw.Reddit(client_id=log['client_id'],
                                          client_secret=log['client_secret'],
                                          user_agent=log['user_agent'])
        except:
            # Should catch errors
            pass


if __name__ == '__main__':
    print("Fleury et Bot")
