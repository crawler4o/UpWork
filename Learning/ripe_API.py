import requests
# import json

header = {'accept': 'application/json'}  # the second supported option is xml
a = requests.get('http://rest.db.ripe.net/search?query-string=IPACCT', headers=header)
a = a.json()

tst_inf = a['objects']['object'][2]['attributes']['attribute']
own_inf = a['objects']['object']

abuse_mail = 0
seq = 0
for _ in own_inf:
    for atribute in own_inf[seq]['attributes']:
        if 'value' in own_inf[seq]['attributes'][atribute][0].keys() and \
                'Abuse Contact' in own_inf[seq]['attributes'][atribute][0]['value']:
            abuse_mail = own_inf[seq]['attributes'][atribute][2]  # funny, the mail is not provided to public user

    seq += 1
print(abuse_mail)

# This is to nicely print the json
# print(json.dumps(a, indent=4, sort_keys=True))

# This is the initial test to print a phone number.
# for x in tst_inf:
#     if 'name' in x.keys() and x['name'] == 'phone':
#         print('{}\n'.format(x['value']))