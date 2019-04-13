import time
import plotting as plot

def scalar_vec_mult(a, v): # Function to multiply vector
    return [a*v[i] for i in range(len(v))]

plot.plot([scalar_vec_mult(i/100, [3,2]) for i in range(-301,301)], 5) # plot image
time.sleep(1) # Pause to avoid prematurely deleting file