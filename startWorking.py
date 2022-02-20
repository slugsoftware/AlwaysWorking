import mouse
import time
from loguru import logger

logger.info("Let's work!")
logger.info("Work server started")

counter = 0

while( True ):
	# We move the mouse 1px to the left
	mouse.move(x = 1, y = 0, absolute = False, duration = 0.1)
	time.sleep(240)
	counter = counter + 1
	logger.debug("Iteration # : " + str(counter) )


