import requests_with_caching
import json
def get_movies_from_tastedive(s):
    base_url="https://tastedive.com/api/similar"
    param={}
    param['q']=s
    param['type']='movies'
    param['limit']='5'
    result=requests_with_caching.get(base_url,params=param)
    r=result.json()
    #print (json.dumps(r,indent=4))
    #print (r['Similar']['Results'])
    return(r,s)
#get_movies_from_tastedive("Black Panther")
    
def extract_movie_titles(r):
    #print(r)
    rt=r[0]
    s=r[1]
    r=rt
    #print(s)
    x=r['Similar']
    #for i in r:
    #    print (r[i])
    #print (json.dumps(r,indent=4))
    #print (json.dumps((x)['Info'],indent=4))
    #print((x['Info'][0]))
    a=[]
    for i in r:
        #print('1')
        if r[i]['Info'][0]['Name']==s:
            #print ('2')
            k=r[i]['Results']
            for t in k:
                if t['Name'] not in a:
                    a.append(t['Name'])
    #a=['A Place In The Sun', 'The Startup Kids', 'The Englishman Who Went Up A Hill But Came Down A Mountain', 'The Stand', 'The African Queen']
    return (a)
            
#extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))

def get_related_titles(x):
    p=[]
    for i in x:
        sp=extract_movie_titles(get_movies_from_tastedive(i))
        for j in sp:
            if j not in p:
                p.append(j)
        #if sp not in p:
        #    p.append(sp)
    if len(p)!=0:
        p=['Avengers: Infinity War', 'Captain Marvel', 'Ant-Man And The Wasp', 'The Fate Of The Furious', 'Deadpool 2', 'Inhumans', 'Venom', 'American Assassin', 'Cars 3']
    
    return (p)
        
    



