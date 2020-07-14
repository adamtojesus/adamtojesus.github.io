f = open('ipfb.txt')
raw = f.read()
raw = raw.replace("\n",'')
raw = raw.replace(" ",'')
ot_ls = raw.split("|")

ot_str= ""
for each in range(1, len(ot_ls)-1):
    ot_str = ot_str + '{"id": "'+str(each+1)+'","labels": ["Human"],"properties": {"Name": "'+ot_ls[each]+'", "Father of": "'+ot_ls[each+1]+'", "Son of": "'+ot_ls[each-1]+'"}},'
    # ot_str = ot_str + '{"id": "'+str(each+1)+'","type": "FATHER_OF","startNode": "'+str(each+1)+'","endNode": "'+str(each+2)+'","properties": {"from": 1473581532586}}'
    # ot_str = ot_str + '{"id": "'+str(each+1)+'","type": "FATHER_OF","startNode": "'+str(each+1)+'","endNode": "'+str(each+2)+'", "properties": {}},'

print(ot_str)