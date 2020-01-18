import requests
flag=True
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}


def getMovielist(pageStart):
    r = requests.get('https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=20&page_start=' +
                     str(pageStart), headers=headers)
    for item in r.json()['subjects']:
        getMovieInfo(item['id'])


def getMovieInfo(subjectId):
    r = requests.get('https://movie.douban.com/j/subject_abstract?subject_id=' +
                     str(subjectId), headers=headers)
    subject = r.json()['subject']
    if int(subject['release_year']) < 2019 :
        global flag
        flag=False
        return

    if float(subject['rate'])<8:
        return

    print(subject['title']+':'+subject['rate'])
    # insertData = {
    #     "id": subject['id'],
    #     "title": subject['title'],
    #     "rate": subject['rate'],
    #     "short_comment"：subject['short_comment']['content'],
    #     "duration": subject['duration'],
    #     "subtype": subject['subtype'],
    #     "region": subject['region'],
    #     "release_year": subject['release_year']
    # }

    # print(inserData)

def main():
    num = 0
    while(flag):
        getMovielist(num)
        num +=20
   

if __name__ == '__main__':
    main()
