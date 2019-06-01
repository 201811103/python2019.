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
    gu = input('한눈에 보고 싶은 구를 입력하세요')
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