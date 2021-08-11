#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import pandas as pd
import os
import time


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36',
           'Authorization': None}
#token申请教程:https://www.jianshu.com/p/d0643008f5a9
#token规范{'Authorization':'token ghp_abcdefghijklmnopqrstuvw'}



datas_name=[]
datas_url=[]


def get_github_api(keyword): 
  if os.path.exists('output.csv'):
        s=pd.read_csv('output.csv',usecols=[0,1])
        response1=requests.get('https://api.github.com/search/repositories?q='+str(keyword)+'&sort=updated&order=desc&per_page=30',headers=headers)
        result=json.loads(response1.text)
        #print(response1.headers)
        for  k in result['items']:
            print('name: '+str(k['name'])+' url: '+str(k['html_url']))
            datas_name.append(k['name'])
            datas_url.append(k['html_url'])
        df = pd.DataFrame({'name':datas_name,'url':datas_url })
        df.to_csv('output.csv',mode='a',header=False,index=None) #save to file
        return result
        

  else:
        response2=requests.get('https://api.github.com/search/repositories?q='+str(keyword)+'&sort=updated&order=desc&per_page=100',headers=headers)
        result=json.loads(response2.text)
        #print(response2.headers)
        for i in result['items']:
            print('name: '+str(i['name'])+' url: '+str(i['html_url']))
            datas_name.append(i['name'])
            datas_url.append(i['html_url'])
        df = pd.DataFrame({'name':datas_name,'url':datas_url })
        df.to_csv('output.csv',header=['name','url'],index=None) #save to file
        return result
    


def get_server(result):
    token=None
    server_url='https://sctapi.ftqq.com/{}.send'.format(token)
    for data in result['items']:
        datas = {
           "text":data['name'],
           "desp":data['html_url']
            }
        requests.post(server_url,data = datas)
    

if __name__=='__main__':
    keyword=input('输入你要监控的github资产:')
    while True:
      result=get_github_api(keyword)
      #get_server(result)#server酱推送微信可选
      result=[]
      datas_name=[]
      datas_url=[]
      time.sleep(3600)#每一天请求一次















