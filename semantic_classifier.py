def strip_punctuation(x):
    for i in x:
        if i in punctuation_chars:
            x=x.replace(i,'')
            
    return x
    
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def get_pos(x):
    x=strip_punctuation(x)
    a=x.split()
    cnt=0
    for i in a:
        if i in positive_words:
            cnt+=1
    return cnt

def get_neg(x):
    x=strip_punctuation(x)
    a=x.split()
    cnt=0
    for i in a:
        if i in negative_words:
            cnt+=1
    return cnt

handle=open('project_twitter_data.csv','r')
hp=open('resulting_data.csv','w')
lp=handle.readlines()
hp.write('Number of Retweets')
hp.write(', ')
hp.write('Number of Replies')
hp.write(', ')
hp.write('Positive Score')
hp.write(', ')
hp.write('Negative Score')
hp.write(', ')
hp.write('Net Score')
hp.write('\n')
for i in lp[1:]:
    arr=i.split(',')
    ar=arr[2][:-1]
    posi=get_pos(arr[0])
    negi=get_neg(arr[0])
    hp.write(arr[1])
    hp.write(',')
    hp.write(ar)
    hp.write(',')
    hp.write(str(posi))
    hp.write(',')
    hp.write(str(negi))
    hp.write(',')
    hp.write(str(posi-negi))
    hp.write('\n')
hp.close()
handle.close()
    

