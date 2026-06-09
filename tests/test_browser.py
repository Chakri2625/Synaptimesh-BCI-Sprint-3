from app.browser_controller import *

import time

open_browser()

time.sleep(2)

search_google(
    "Brain Computer Interface"
)

time.sleep(2)

search_google(
    "Python Automation"
)

time.sleep(2)

search_google(
    "SynaptiMesh Project"
)

time.sleep(2)

refresh_page()

time.sleep(2)

close_browser()