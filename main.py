from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

'''opts = Options()
opts.headless = True
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)
browser.get('https://duckduckgo.com')
search_form = browser.find_element_by_id('search_form_input_homepage')
search_form.send_keys('real python')
search_form.submit()
results = browser.find_elements_by_class_name('result')
print(browser.title)'''

# we can now start Firefox and it will run inside the virtual display
opts = Options()
opts.headless = True
assert opts.headless  # Operating in headless mode
browser = Firefox(options=opts)

    # put the rest of our selenium code in a try/finally
    # to make sure we always clean up at the end
try:
    browser.get('http://www.google.com')
    print(browser.title) #this should print "Google"

finally:
    browser.quit()
