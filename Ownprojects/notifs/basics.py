import notify2
import time

notify2.init('app name')

n = notify2.Notification("Title",
                         "text text text",
                         "notification-message-im"   # Icon name
                        )
while True:
    n.show()
    time.sleep(1)
