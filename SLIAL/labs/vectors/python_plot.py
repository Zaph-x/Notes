import time
import plotting as plot

def svm(a, v):
    return [a*v[i] for i in range(len(v))]

plot.plot([svm(i/100, [3,2]) for i in range(101)], 5) # plot image
time.sleep(1) # Pause to avoid prematurely deleting file