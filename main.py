import praw

reddit = praw.Reddit("one_and_only", user_agent="one_and_only user agent")

print(reddit.user.me())