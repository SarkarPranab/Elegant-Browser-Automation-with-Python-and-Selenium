
from keep_alive import keep_alive
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time 
from collections import namedtuple
from threading import Thread
from os.path import isfile
from PIL import Image
import os
from datetime import date
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import csv

# we can now start Firefox and it will run inside the virtual display
keep_alive()
opts = Options()
opts.headless = True
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)

PAGE="https://popspins.com/login.php"
sched = BlockingScheduler()

    # put the rest of our selenium code in a try/finally
    # to make sure we always clean up at the end
try:
  def some_job():
    print("Its Fine")
    browser.execute_script("window.open('');")
    time.sleep(5)
    browser.get(PAGE)
    print(PAGE.title) #this should print "Google"
    time.sleep(3)
    browser.save_screenshot("image.png")
    time.sleep(3)
    image = Image.open("image.png")
    # Showing the iamge
    time.sleep(3)
    input_username = browser.find_element_by_css_selector("input[name='username']").send_keys("AlphaMatrix")
    time.sleep(3)
    input_pwd =  browser.find_element_by_css_selector("input[name='password']").send_keys("Ct98V3L*FSGsR*z")
    time.sleep(3)
    sign_in = browser.find_element_by_css_selector("button[name='action']").click()
    time.sleep(7)
    Claiming = browser.find_element_by_css_selector("a[class='btn btn-success pulsen3']")
    time.sleep(3)
    spins_left = browser.find_element_by_css_selector("span[id='spins']").text

    print(spins_left)
    time.sleep(3)
    spins_left_int = int(spins_left)
    if spins_left_int > 0:
      time.sleep(3)
      Claiming.click()
      browser.implicitly_wait(10)
    else:
      print("ERROR")
    time.sleep(5)
    print("Its Fine")

    e = datetime.now()
    print ("Current date and time = %s" % e)
    print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
    print("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))
    
    time.sleep(3)
    #browser.close()

  #Success
  
  scheduler = BlockingScheduler()
  scheduler.add_job(some_job, 'interval', minutes=70)
  scheduler.start()



finally:
    print("Check For ERROR")
    browser.quit()
