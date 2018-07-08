#自定义模块的 __init__.py
# -*- coding: utf-8 -*-
import requests
import re
def get_ts(m3u8_url,headers):
    res = requests.get(m3u8_url,headers=headers,allow_redirects=False)
    if res.status_code == 200:
        all_ts = re.findall('TxRcCpeN-[0-9]*.ts',res.text)#定义自己的用来匹配ts的正则表达式
        return all_ts
    else:
        return ('m3u8页面访问失败！')
def get_mp4(root_url,ts_list,headers,path,file_name):
    for num in range(len(ts_list)):
        ts_url = root_url + ts_list[num] 
        res=requests.get(ts_url,headers=headers)
        with open (path + file_name +'.mp4','ab') as ts:
            ts.write(res.content)
            print (ts_list[num] + '写入完成！')
#例如:
#import m3u8
#headers = { 'User-Agent': 'Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1)', 'Referer': 'https://www.553cf.com'}
#a = m3u8.get_ts('https://768ii.com/new/wm/2018-06/21/TxRcCpeN/TxRcCpeN.m3u8',headers)
#m3u8.get_mp4('https://768ii.com/new/wm/2018-06/21/TxRcCpeN/',a,headers,'g:/AI/downts/','webmode123')
