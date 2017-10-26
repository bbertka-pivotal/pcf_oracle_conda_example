#!/usr/bin/python
import cfworker
import time
import json

worker = cfworker.cfworker()

"""
Api Calls go here
"""
@worker.app.route('/<message>')
def hello(message):
	return json.dumps({'message':message})


"""
This is our asynchronous worker
"""
worker.start()
while True:
	time.sleep(3)
	print "Hello Python"


worker.stop()
