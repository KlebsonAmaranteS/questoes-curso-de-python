import time 
import emoji

for c in range(10,-1,-1):
    time.sleep(1)
    print(c)
print(emoji.emojize(':fireworks: '*10, language='en'))