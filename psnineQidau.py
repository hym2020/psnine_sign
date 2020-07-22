import requests, os

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
        }
u = 'http://psnine.com/'


def logger(usr,pw):
    session = requests.Session()
    
    login = session.post(u+'/sign/'+'signin'+'/ajax', headers=headers ,
                         data={'psnid': usr , 'pass': pw})

    if login.status_code == 404:
        return 'Login Error'
    else:
        return session

def qidaoer(session):
    if isinstance(session , str):
        return session

    s = ''
    cookieDict = dict(session.cookies)
    for k in cookieDict:
        s+='%s=%s;' % (k , cookieDict[k])
    cookieStr = s.rstrip(';')

    headers['Cookie'] = cookieStr

    res = session.get(u+'/set/qidao/ajax' , headers=headers)

    if res.status_code == 404:
        return res.text
    else:
        return 'Signed Success'

if __name__ == '__main__':
    users = os.environ['USR'].split('\n')
    passes = os.environ['PASS'].split('\n')
    
    if not len(users) == len(passes):
        exit()
        
    for i in range(len(users)):
        status = qidaoer(logger(users[i], passes[i]))
        print('%s的簽到結果為:%s' % (users[i], status))