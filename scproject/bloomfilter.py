from pybloom import BloomFilter
from scproject import config
import os
bf=BloomFilter(capacity=1000*1000*200,error_rate=0.0001)
for f in os.listdir(config.outer_dir):
    if not  f.find(".dat"):
        continue
    for line in open(os.path.join(config.outer_dir,f)):
        if line.strip()!="":
            bf.add(line)

