import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

#Two  lines to make our compiler able to draw:
from matplotlib import pyplot as plt
plt.savefig('foo.png')
plt.savefig('foo.pdf')
# plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
