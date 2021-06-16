import numpy as np
import csv

kwd_list = ['나이키','원피스', '운동화']
arr=np.array(kwd_list)
result = np.where(arr == '나이키')

kwd_list = []

kwd_list.append("keyword_list[i]")
kwd_list.append("ad")
kwd_list.append("qgw")
kwd_list.append("qgwasAASd")

print(".".join(kwd_list[0:3]))
print("ASD".lower())
print(list(map(lambda x: x.lower(), kwd_list)))
