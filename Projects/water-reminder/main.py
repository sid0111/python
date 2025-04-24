import time
from notifypy import Notify

while True:
    notification = Notify()
    notification.title = "Reminder"
    notification.message = "Sip some water."
    notification.send()
    time.sleep(10)