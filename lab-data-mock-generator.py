#!/usr/bin/env pynthon3

import pandas as pd
list = []
# It will create 100k records
for i in range(0,100000):

    email = 'tester{i}@aeturnum.com'.replace("{i}",str(i))

    phone = "0000000000"
    phone = str(i) + phone[len(str(i)):] 

    fname = "test" + str(i)
    lname = "test" + str(i)

    dob = "199{a}-{a}-0{a}".replace("{a}",str(len(str(i))))

    list.append((fname, lname, email, phone, dob, str(i)))

    columns = ['First Name', 'Last Name', 'Email Address', 'Phone Number','Date Of Birth','Current Loyalty Point Total']

    df = pd.DataFrame(list, columns = columns)

    df.to_csv('user_data_100k.csv', index = False)

