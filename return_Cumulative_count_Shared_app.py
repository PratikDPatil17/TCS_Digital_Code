import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    for i in range(1,n+1):
        if i == 1:
            liked = math.floor(5/2)
            cum = liked
            
        else:
            shared = liked * 3
            liked = math.floor(shared / 2)
            cum = cum + liked 
            print("cum 3=",cum)
        
    return cum
