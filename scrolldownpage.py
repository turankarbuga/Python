# js scroll down page

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True

        
# Sample use

jscommand = """
followers_list = document.querySelector("div[role = 'dialog'] ul") # select div
followers_list.scrollTo(0, followers_list.scrollHeight); 
var lenOfPage=followers_list.scrollHeight;
return lenOfPage;
"""

lenOfPage = self.browser.execute_script(jscommand)
match = False
while (match == False):
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = self.browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match = True
