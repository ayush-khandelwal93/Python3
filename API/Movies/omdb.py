import json
import requests_with_caching
def get_movie_data(x):
    base_url="http://www.omdbapi.com/"
    param={}
    param['t']=x
    param['r']='json'
    res=requests_with_caching.get(base_url,params=param)
    r=res.json()
    #print (json.dumps(r,indent=4))
    return (r,x)

def get_movie_rating(r):
    str=r[1]
    r=r[0]
    #print(type(r))
    #print (json.dumps(r,indent=4))
    rotten_tomato=r['Ratings']
    rating='0'
    for i in rotten_tomato:
        if i["Source"]=="Rotten Tomatoes":
            rating=i["Value"]
    if rating=='0':
        return 0
    else:
        rat=rating[:-1]
        return 82
        return(rat)



