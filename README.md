# OSS-prj1
Bash Shell Programming

OSS project1 - Bash Shell Programming

컴퓨터공학과 3학년 12201071 신나윤
 개요
1	프로젝트 소개
2	프로젝트 설명
3	프로젝트 중 겪은 어려움이나 차후 개선할 부분
   
1.	프로젝트 소개
-	강의를 통해 배운 Bash Shell Script 문법에 익숙해지는 것이 이 프로젝트의 목적입니다.
-	Linux 환경에서 Bash 기능을 사용하여 다양한 데이터 처리 기능을 적재적소에 활용할 수 있습니다.
-	u.item u.data u.user 파일은 모두 현재 디스크립터에 존재함을 가정하고 파일을 사용합니다. 

2.	프로젝트 설명
-	해당 프로젝트는 총 9개의 선택지를 가지고 있습니다.
9번 exit 선택지를 고르지 않는 한, 사용자로부터 계속 선택지를 입력 받습니다.
특정 조건과 일치하는 필드를 선택하는 문제에서는 주로 awk 문법을 사용하고, 원하는 데이터로 가공을 필요로 하는 경우, sed문법을 사용하여 다음 선택지를 수행하였습니다. 

-	1번 선택을 한 경우, 사용자로부터 movie id를 입력 받고, u.item에서 해당 movie 의 정보를 출력합니다.
사용자의 입력값을 $choice로 저장하고, u.item의 $1(movie id) == $choice인 필드만 출력하기 위해 awk 문법을 사용하였습니다.
-	2번 선택을 한 경우, 사용자로부터 action 장르의 영화의 출력을 원하는지를 묻고, 사용자가 y를 입력하여 출력을 요구하는 경우, u.item파일에서 action 장르 영화의 movie id와 movie title을 오름차순으로 10개만 출력합니다.
1번과 마찬가지로, $7(action) ==action 인 필드만 출력하기 위해 awk 문법을 사용했습니다.
-	3번 선택을 한 경우, 사용자로부터 movie id를 입력받고, u.data 파일에서
해당 영화의 평균평점을 소수점 5자리까지 계산하여 출력합니다.
이때 소수점이 6번째 이상인경우, 6번째에서 반올림하여 5번째까지만 출력합니다. 
u.data 파일에서 마찬가지로 필드가 원하는 조건과 일치하는지 확인합니다.
이문제의 경우, sum을 반복적으로 수행한후 평균은 한번만 계산하기에, END를 사용했습니다.
-	4번 선택을 한 경우, 사용자로부터 IMDd URL의 삭제를 원하는지 묻고, 사용자가 y를 입력하여 출력을 요구하는 경우, u.item에서 IMDd URL을 삭제하여 오름차순으로 10개만 출력합니다.
이 경우 URL의 삭제가 필요하기에, sed를 이용하여 해당 필드의 범위를 지정하고 공백으로 비워줍니다.
-	5번 선택을 한 경우, 사용자로부터 출력양식을 변경하고 싶은지를 묻고, y를 입력한 경우 u.user 파일의 성별부분을 sed ‘s/F/female/g’로 문자열을 치환하고 (F ->female, M -> male) 출력양식을 awk 로 변경했습니다.
-	6번 선택을 한 경우, u.item의 출력양식을 변경하고 싶은지를 묻고, y를 입력한 경우 01-Jan-1995 를 19950101 처럼 변형시켰습니다.
이때 필드값을 지정하는 것이 아닌, 문자열을 레퍼런싱 하여 Jan과 같은 월을 나타내는 부분을 -s 커맨드로 치환하고, -e 커맨드로 1~12월 별 치환 문자열을 모두 기입하였고,  출력양식을 변경했습니다.
-	7번 선택의 경우, u.item과 u.data 파일 두개 모두 사용해야 하는 문제입니다. 사용자에게서 user id 를 입력받아 u.item에서 해당 uid가 평가한 movie id를 awk – F\| 구분자를 사용하여 추리고, sort -n으로 정렬, 이후 tr 문법을 사용하여 불필요한 줄 바꿈을 삭제하고, 4|15|28 *** 처럼 양식을 지정한 뒤, movieidset변수에 저장합니다. 그리고 u.data파일에서 반복문을 통해 movieidset의 movid id를 한 개씩 mid로할당한 뒤, $1==mid 인 데이터들을 오름차순으로 10개만 출력하였습니다. 

-	8번 선택의 경우, 20~29살인 프로그래머들의 uid를 u.data로부터 출력하여 uidset에 저장합니다. 그리고 BEGIN에는 uidset의 문자열을 공백으로 구분하는 split과 for문의 반복으로 u배열에 나눈 문자열을 넣고, 영화 평점을 movies 배열에 합계를 누적합니다 END에서는 BEGIN에서 계산한 합을 average로 나타내기 위해 count로 평가한 인원을 나눠, 소수점 다섯자리까지 반올림 하여 나타냅니다.

3.	프로젝트 중 겪은 어려움이나 차후 개선할 부분
-	8번 문제를 구현하는데 있어서 많은 어려움을 겪었다. 
7번문제와 3번문제가 섞여있는 느낌이 들어서 그 두가지를 사용해서 구현하려 했으나, 번번이 실패했다. 그중에서 특히 아쉬운 부분은, u.data를 1부터 오름차순으로 정렬해서 movie id = 1이고, $1 == uid[i]처럼 해서 순차적으로 덧셈을 하면 시간소모가 적을 것 같아 이렇게 구현하고 싶었는데, 계속 오류가 발생해서 u.data로 정렬하여 구현하는 방법을포기하고 그냥 sum 을 구하는 방법을 택했다.
리눅스 문법을 좀더 공부하여 이부분에서 왜 계속 오류가 났는지 알아 내고 싶다.
