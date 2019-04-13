import time
from plotting import plot

S = [1+0.2j,1+2j,2+1.4j,2-1.2j] # Make set

[print(abs(S[i])) for i in range(len(S))]
# The length from the origin of each element in the set are
# 1.019803902718557
# 2.23606797749979
# 2.4413111231467406
# 2.33238075793812

plot(S, 4) # plot image
time.sleep(1) # Pause to avoid prematurely deleting file