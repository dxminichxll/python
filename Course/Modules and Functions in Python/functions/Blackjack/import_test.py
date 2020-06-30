import blackjack
from blackjack import *

# In Python, functions are not made private, so they can be accessed when imported, we use underscores at the start
# of function names to show they are not meant to be used.
# When we use * to import, python takes this into consideration and doesn't give us access to the functions starting
# with an underscore
# Anything with double underscores at the start of end of their name, should not be changed but can be used

g = sorted(globals())
for x in g:
    print(x)
# ^^ prints all global variables, when we import with *, it shows a lot more variables

# print(__name__)

blackjack._deal_card(blackjack.dealer_card_frame)
blackjack.play()
