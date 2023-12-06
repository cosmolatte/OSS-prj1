import numpy as np
import pandas as pd

data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

# DataFrame 생성
df = pd.DataFrame(data_df)

# 필요한 년도 범위 설정
years = range(2015, 2019)# n to n-1 까지 니까 2019. 실제 출력은 2018까지

#1번문제
for year in years:
    # 해당 년도의 데이터 추출
    year_data = df[df['year'] == year]

    # 상위 10명의 선수 출력
    top_hit = year_data.sort_values('H', ascending=False).head(10)[['batter_name', 'H']].reset_index(drop=True)
    top_hit.index += 1
    top_avg = year_data.sort_values('avg', ascending=False).head(10)[['batter_name', 'avg']].reset_index(drop=True)
    top_avg.index += 1
    top_hr = year_data.sort_values('HR', ascending=False).head(10)[['batter_name', 'HR']].reset_index(drop=True)
    top_hr.index += 1
    top_obp = year_data.sort_values('OBP', ascending=False).head(10)[['batter_name', 'OBP']].reset_index(drop=True)
    top_obp.index += 1

    print("\nTop 10 Players in Hits for", year)
    print(top_hit)

    print("\nTop 10 Players in Batting Average for", year)
    print(top_avg)

    print("\nTop 10 Players in HomeRun for", year)
    print(top_hr)

    print("\nTop 10 Players in On-Base Percentage for", year,)
    print(top_obp)

#2번문제
year = 2018
best_player_in_2018 = year_data.sort_values('war', ascending=False)[['batter_name', 'cp', 'war']]
best_player_in_2018_edit = best_player_in_2018.drop_duplicates(['cp'], keep='first').reset_index(drop=True)
best_player_in_2018_edit.index += 1
print("\n Top Players for each position in 2018")
print(best_player_in_2018_edit)
#...지명타자도 cp라고 생각하고 포함시킴, 야알못이라...

#3번문제
correlations = df[['R', 'H', 'HR', 'RBI', 'SB', 'war', 'avg', 'OBP', 'SLG', 'salary']].corr()
# correlations 는 상관관계 행렬이다 .corr()이 각 '..'을 받고 상관관계 행렬로 return 한다.
highest_correlation = correlations['salary'].sort_values(ascending=False).index[1]
#ascending = false로 내림차순정렬하고, index[0]은 salary를 가리키기에 index[1]을 선택해준다(자기자신을제외하고 가장 상관있는거 추출).
print("\nThe highest correlation with 'salary' is: ", highest_correlation)



