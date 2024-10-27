import matplotlib
print(matplotlib.get_backend())
#或者 matplotlib.pyplot.get_backend()

import matplotlib;matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
line_up, = plt.plot([1,2,3], label='Line 2')
line_down, = plt.plot([3,2,1], label='Line 1')
plt.legend(handles=[line_up, line_down])  # 放置图例
plt.show()





line, = plt.plot([1, 2, 3])

line.set_label("Label via method")

plt.legend()

plt.show()

