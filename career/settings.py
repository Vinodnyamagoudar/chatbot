SEARCH_KEY = "AIzaSyBXBp0EVoJ0MBEK61A3GxT6Rlu6iS_sgLQ"
#SEARCH_ID = "4180288a52f0f463b"
SEARCH_ID = "905374672d23045d0"
COUNTRY = "in"
SEARCH_URL = "https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&num=10&gl=" + COUNTRY
RESULT_COUNT = 20

import os
if os.path.exists("private.py"):
    from private import *