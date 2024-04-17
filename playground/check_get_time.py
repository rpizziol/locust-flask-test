import requests
import time
import numpy as np

out = []
for i in range(100):
    st = time.time()
    requests.get("http://34.47.11.78/")
    rt = time.time() - st
    print(f"rt = {rt}")
    out.append(rt)

print(np.mean(out))
