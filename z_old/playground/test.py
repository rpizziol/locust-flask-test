import requests
import time
import numpy as np

out = []
for i in range(10):
    st = time.time()
    requests.get("http://spring-test-app-tier3")
    rt = time.time() - st
    print(f"rt = {rt}")
    out.append(rt)

print(np.mean(out))
