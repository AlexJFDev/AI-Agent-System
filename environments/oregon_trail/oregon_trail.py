import random

from interfaces import Environment
from interfaces import Agent

INSTRUCTIONS = (
"This program simulates a trip over the oregon trail from Independence, Missouri to Oregon City, Oregon in 1847 your family of five will cover the 2040 mile Oregon Trail in 5-6 months --- if you make it alive.\n"
"You had saved $900 to spend for the trip, and you've just paid $200 for a wagon. You will need to spend the rest of your money on the following items:\n"
"     Oxen - you can spend $200-$300 on your team the more you spend, the faster you'll go because you'll have better animals\n"
"     Food - the more you have, the less chance there is of getting sick\n"
"     Ammunition - $1 buys a belt of 50 bullets you will need bullets for attacks by animals and bandits, and for hunting food\n"
"     Clothing - this is especially important for the cold weather you will encounter when crossing the mountains\n"
"     Miscellaneous supplies - this includes medicine and other things you will need for sickness and emergency repairs\n\n"
"You can spend all your money before you start your trip - or you can save some of your cash to spend at forts along the way when you run low. However, items cost more at the forts. You can also go hunting along the way to get more food.\n"
"When asked to enter money amounts, don't use a '$'.\n"
"good luck!!!"
)

GAME_WEEK_DATES = [
    "March 29", "April 12", "April 26", "May 10", "May 24", "June 7", "June 21", "July 5", 
    "July 19", "August 2", "August 16", "August 31", "September 13", "September 27", 
    "October 11",  "October 25", "November 8", "November 22", "December 6", "December 20"
]

class OregonTrail(Environment):
    """
    An environment that represents oregon trail.
    """

    def __init__(self):
        pass

    def fetch_state(self, agent):
        return
    
    def update_state(self, agent, action):
        return