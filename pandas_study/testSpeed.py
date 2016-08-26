from WindPy import w
from datetime import datetime
w.start(showmenu=False)

sum = 0
count = 10



for i in range(count):
    time1 = datetime.now()
    data = w.wsq("P1701.DCE", "rt_latest,rt_ask1,rt_bid1")
    time2 = datetime.now()



print('avg=',(time2-time1)/count)
