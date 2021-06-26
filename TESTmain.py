from keep_alive import keep_alive
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
from collections import namedtuple
from threading import Thread
from os.path import isfile
from PIL import Image
import os
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import date 
import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert



# we can now start Firefox and it will run inside the virtual display
keep_alive()
opts = Options()
opts.headless = True
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
PAGE = "http://collabedit.com/tgqpm"
sched = BlockingScheduler()

# put the rest of our selenium code in a try/finally
# to make sure we always clean up at the end
try:

    def some_job():
        print("Its Fine")
        
        time.sleep(5)
        e = datetime.now()
        print ("Current date and time = %s" % e)
        print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
        print("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))
        time.sleep(3)
        browser.close()

    #Success

    scheduler = BlockingScheduler()
    scheduler.add_job(some_job, 'interval', minutes=1)
    scheduler.start()

finally:
    browser.quit()
