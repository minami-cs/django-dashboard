import csv

import numpy as np

from config.settings import DATA_DIRS


class MyAnalysis:
    def kidsnum(self):
        f = open(DATA_DIRS[0] + '\\age3.csv')
        data = csv.reader(f)
        next(data)
        data = list(data)
        num_kids = []
        for row in data:
            kids = np.array(row[3:9], dtype=int)
            sum_kids = np.sum(kids)
            num_kids.append([row[0].split()[1], int(sum_kids)])
        data = num_kids;
        print(data)
        return data

    def shindorim(self, loc):
        f = open(DATA_DIRS[0] + '\\age2.csv')
        data = csv.reader(f)
        next(data)
        data = list(data)
        
        home_name = ''
        home = None
        home2 = None
        # 신도림의 연령별 비율
        for row in data:
            if (loc in row[0]):
                home = np.array(row[3:], dtype=int)
                home2 = (home / int(row[2]))*100
                home_name = row[0]
        print(home_name)
        print(home2.tolist())
        # 모든 지역의 연령별 비율 구하기
        away = []
        min = 999
        result_name = '';
        result = None;
        for row in data:
            away = np.array(row[3:], dtype=int)
            away2 = (away / int(row[2]))*100
            # 나누기할 때 유효하지 않은 값이 발견되었다는 경고문 없애는 코드
            np.seterr(divide='ignore', invalid='ignore')
            # 절대값의 합
            s = np.sum(np.abs(home2 - away2))
            if loc not in row[0] and s < min:
                min = s;
                result_name = row[0]
                result = away2
        print(result_name)
        print(result.tolist())
        data_result = [{
            'name': home_name.split('(')[0],
            'data': home2.tolist()
        }, {
            'name': result_name.split('(')[0],
            'data': result.tolist()
        }]
        print(data_result)
        return data_result

    def fiveyears(self):
        #2020년
        f = open(DATA_DIRS[0] + '\\age4.csv')
        data = csv.reader(f)
        next(data)
        data = list(data)

        #2015년
        f2 = open(DATA_DIRS[0] + '\\age5.csv')
        data2 = csv.reader(f2)
        next(data2)
        data2 = list(data2)

        locations = []
        plusminus = []
        for i in range(len(data)):
            pm = (int(data[i][1]) - int(data2[i][1])) / int(data2[i][1]) * 100
            plusminus.append(pm)
            locations.append(data[i][0].split('(')[0])
        print(locations)
        print(plusminus)
        return locations, plusminus



if __name__ == '__main__':
    # MyAnalysis().kidsnum()
    # MyAnalysis().shindorim('신도림')
    MyAnalysis().fiveyears()