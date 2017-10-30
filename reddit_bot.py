import praw
import config
import time
import os


def bot_login():
	print("Logging in!")
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "Aiiight dog comment responder v0.1")
	print("Logged in!")
	return r

def run_bot(r, comments_replied_to):
	print("Obtaining 25 comments...")



	for comment in r.subreddit('aiiightTest').comments(limit=10): 
		if "dog" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
			print("String with \"dog\" found in comment " + comment.id)
			comment.reply("Script response to DOGS....")
			print("Replied to comment " + comment.id)

			comments_replied_to.append(comment.id)

			with open (	'commentsRepliedTo.txt', 'a') as f:
				f.write(comment.id + "\n")

	print("Sleeping for 10 seconds..")
	#sleep for 10 seconds.
	time.sleep(10)
def get_saved_comments():
	if not os.path.isfile("commentsRepliedTo.txt"):
		comments_replied_to = []
	else:
		with open('commentsRepliedTo.txt', 'r') as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = filter(None, comments_replied_to)

	return comments_replied_to
comments_replied_to = get_saved_comments()
r = bot_login()
while True:
	run_bot(r, comments_replied_to)



#Part 3: https://www.youtube.com/watch?v=Wo2udG3e1qM