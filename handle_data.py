import csv
import datetime
dict_len = {}
dict_data = {}
all_len = 0
def hande_name(name):
    if name =='interest1'or name == 'interest2' or name == 'interest3'or name == 'interest4' or name == 'interest5':
        return 'interest'
    elif name == 'kw1' or name == 'kw2' or name == 'kw3':
        return 'kw'
    elif name == 'topic1' or name == 'topic2' or name == 'topic3':
        return 'topic'
    else:
        return name
def write_time(explain):
    f_time = open('time.txt', 'a')
    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f_time.write(explain+time_now)
    f_time.write('\n')
    f_time.close()

def diminish(str_a):
    str_b = ''
    count_0 = 0
    for i in range(len(str_a)):
        if str_a[i] == '1':
            if count_0 != 0:
                tmp_b = '%da' % count_0
                # print(tmp_b)
                str_b += tmp_b
                count_0 = 0
            str_b += 'b'
        else:
            count_0 += 1

    if count_0 != 0:
        tmp_b = '%da' % count_0
        # print(tmp_b)
        str_b += tmp_b
    #print(str_b)
    return str_b

#with open('I:\preliminary_contest_data\\userFeature.data') as f:
with open('/media/candela/段光强/preliminary_contest_data/userFeature.data') as f:

    write_time(explain='start:')
    f_csv = csv.reader(f)
    headers = next(f_csv)
    dict_data['age'] = set()
    dict_data['gender'] = set()
    dict_data['marriageStatus'] = set()
    dict_data['education'] = set()
    dict_data['consumptionAbility'] = set()
    dict_data['LBS'] = set()
    # dict_data['interest1'] = set()
    # dict_data['interest2'] = set()
    # dict_data['interest5'] = set()
    # dict_data['interest3'] = set()
    # dict_data['interest4'] = set()
    dict_data['interest'] = set()
    # dict_data['kw1'] = set()
    # dict_data['kw2'] = set()
    # dict_data['kw3'] = set()
    dict_data['kw'] = set()
    # dict_data['topic1'] = set()
    # dict_data['topic2'] = set()
    # dict_data['topic3'] = set()
    dict_data['topic'] = set()
    dict_data['appIdInstall'] = set()
    dict_data['appIdAction'] = set()
    dict_data['ct'] = set()
    dict_data['os'] = set()
    dict_data['carrier'] = set()
    dict_data['house'] = set()
    i = 0
    for row in f_csv:
        #print(row)
        list_row = row[0].split('|')
        uid=list_row[0].split(' ')
        for k in range(1, len(list_row)):
            tmp = list_row[k].split(' ')
            tmp[0] = hande_name(tmp[0])
            dict_data[tmp[0]].update(tmp[1:])
        #print(len(list_row))
        i+=1
        if i%1000==0:
            print(i)
        # if i == 1000:
        #     break
    print(dict_data)
    fw = open('dictdata.txt', 'w')
    #fw.write(dict_data)
    fwl = open('data_len.txt', 'w')
    for key in dict_data.keys():
         #print(key)
         #print(list(dict_data[key]))
         all_len += len(dict_data[key])
         dict_len[key] = len(dict_data[key])
         list_v = list(dict_data[key])
         dict_data[key]=list_v
         line = key+':'
         line_l = line+str(len(list_v))+'\n'
         fwl.write(line_l)
         for num_k in range(len(list_v)):
             line = line + list_v[num_k]+ ','
         line = line + '\n'
         #print(line)
         fw.write(line)
    fw.close()
    fwl.close()
    #print(dict_len)
    #print(dict_data)
    print(i)
#预处理
list_key = list(dict_len.keys())
print(all_len)
#
write_time(explain='statistics:')
#with open('I:\preliminary_contest_data\\userFeature.data') as fa:
with open('/media/candela/段光强/preliminary_contest_data/userFeature.data') as fa:
    f_csv = csv.reader(fa)
    headers = next(f_csv)
    i = 0
    line = ''
    for row in f_csv:
        f_u = open('user.data', 'a')
        list_row = row[0].split('|')
        uid = list_row[0].split(' ')
        #head_id =
        line = ''
        count = 1
        for key_num in range(len(list_key)):
            tmp_key = list_key[key_num]
            #print('11111')
            #print(tmp_key)
            str_num = '0'*dict_len[tmp_key]
            tmp = list_row[count].split(' ')
            tmp[0] = hande_name(tmp[0])
            #print(tmp[0])
            #print(count)
            if tmp[0] == tmp_key:
                for j in range(1, len(tmp)):
                    index = dict_data[tmp[0]].index(tmp[j])
                    list_num = list(str_num)
                    list_num[index] = '1'
                    str_num = ''.join(list_num)
                count += 1
            if count == len(list_row):
                break
            line = line + str_num
        line = diminish(str_a=line)
        line = uid[1]+':'+line + '\n'
        f_u.write(line)
        print(line[:-1])
        i += 1
        # if i == 1000:
        #     break
        f_u.close()
write_time(explain='finish:')
