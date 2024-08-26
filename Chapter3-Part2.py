# Equilateral Triangle



# Do not alter the two lines below.

import euclid

from colors import *



# Now we create the page on which pens will draw.

# Set its size to 400 by 400, set its colors to PALETURQUOISE,

# set the tracer to 0 (increase the value of the tracer to increase the animation speed).

# Do not delete this line, but change if you like.

euclid.createPage(size = (400, 400), color = PALETURQUOISE, tracer = 0)



# Next we create a pen name logos.

# Its color is VIOLETRED, it begins at position (160, 240)

# and direction 0 (which is directly right).

# The delay of 6 slows it down a bit; decrease delay to increase animation speed.

# Do not  delete, but but change if you like.

# You may also create additional pens.

logos = euclid.Pen(color = VIOLETRED, position = (160, 240), direction = 0, delay = 6)



# Now we draw with logos.

# The result will be an equilateral triangle.

for i in range(3):

   logos.forward(96)

   logos.turn(120)



euclid.finish() # only necessary if tracer isn't 0



euclid.wait()  # keep window open