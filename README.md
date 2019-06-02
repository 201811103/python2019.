# 부산광역시 내의 공공기관

학과 | 학번 | 성명
---- | ---- | ---- 
수학과 |201811103 |김나영


## 프로젝트 개요

부산광역시 내의 각 행정구관에 위치한 공공기관의 종류, 위치, 연락처를 제공하는 프로그램으로써 부산광역시에 여행을 온 여행객들과 거주하고 있는 부산시민들에게 본인이 알고자 하는 공공기관에 관련된 정보를 제공할 수 있어 일상생활에 유용하게 쓰일 수 있는 프로그램입니다.
## 사용한 공공데이터 
[데이터 - 금정구](https://github.com/201811103/python2019./blob/master/금정구.csv)\
[데이터 - 금정구병원](https://github.com/201811103/python2019./blob/master/금정구병원.csv)\
[데이터 - 기장군](https://github.com/201811103/python2019./blob/master/기장군.csv)\
[데이터 - 기장군병원](https://github.com/201811103/python2019./blob/master/기장군병원.csv)\
[데이터 - 남구](https://github.com/201811103/python2019./blob/master/남구.csv)\
[데이터 - 북구](https://github.com/201811103/python2019./blob/master/북구.csv)\
[데이터 - 서구](https://github.com/201811103/python2019./blob/master/서구.csv)\
[데이터 - 수영구](https://github.com/201811103/python2019./blob/master/수영구.csv)\
[데이터 - 수영구병원](https://github.com/201811103/python2019./blob/master/수영구병원.csv)\
[데이터 - 연제구](https://github.com/201811103/python2019./blob/master/연제구.csv)\
[데이터 - 연제구병원](https://github.com/201811103/python2019./blob/master/연제구병원.csv)\
[데이터 - 영도구](https://github.com/201811103/python2019./blob/master/영도구.csv)\
[데이터 - 영도구병원](https://github.com/201811103/python2019./blob/master/영도구.csv)

## 소스
* [링크로 소스 내용 보기](https://github.com/201811103/python2019./blob/master/201811103.py) 
* 코드 삽입

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)


def region():
    gu = input('구/군을 입력하세요\n(Ex. 금정구, 연제구, 영도구, 기장군, 남구, 북구, 서구, 수영구)')
    gufile = pd.read_csv(gu+".csv", engine = 'python')
    return gufile


def office():
    hang = input('행정기관 입력을 입려하세요\n(Ex.우체국, 경찰서, 병원, 소방서, 시청, 주민센터,보건소)')
    gulist = ['금정구','연제구','영도구','기장군','남구','북구','서구','수영구']
    namelist = []

    for gu in gulist:
        hangfile = pd.read_csv(gu + ".csv",engine='python')
        existoffice = list(hangfile['기관명'])
        for i in existoffice :
            if i.find(hang)!=-1 :
                namelist.append(gu)

    return list(set(namelist))

def graph():
    gu = input('한눈에 보고 싶은 구를 입력하세요\n(Ex. 금정구, 연제구, 영도구, 기장군, 남구, 북구, 서구, 수영구)')
    filelist = ['금정구','금정구병원', '연제구', '연제구병원','영도구', '영도구병원','기장군','기장군병원' '남구',
              '북구', '서구', '수영구','수영구병원']
    operationlist = ['보건소','주민센터','경찰서','소방서','우체국','군청','구청','시청','병원']
    gulist = []

    for f in filelist:
        if f.find(gu) != -1 :
            gulist.append(f)
    cntlist = [0]*len(operationlist)

    for g in gulist:
        df = pd.read_csv(g + ".csv", engine='python')
        existoffice = list(df['기관명'])
        for i in range(len(operationlist)):
            for exist in existoffice :
                if exist.find(operationlist[i]) != -1:
                    cntlist[i] = cntlist[i] + 1

    x = operationlist
    y = cntlist

    plt.bar(x, y, label = '행정기관')
    plt.title(gu+' 공공기관의 유무')
    plt.show()

    return cntlist

data1 = region()
print(data1)

data2 = office()
print(data2)

data3 = graph()
print(data3)
