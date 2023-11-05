#!/bin/bash


echo "
User Name: shinnayun
Student Number: 12201071
[ MENU ]
1. Get the data of the movie identified by a specific 'movie id' from 'u.item'
2. Get the data of action genre movies from 'u.item'
3. Get the average 'rating' of the movie identified by specific 'movie id' from 'u.data'
4. Delete the 'IMDb URL' from 'u.user'
5. Get the data about users from 'u.user'
6. Modify the format of 'release data' in 'u.item'
7. Get the data of movies rated by a specific 'user id' from 'u.data'
8. Get the average 'rating' of movies rated by users with 'age' between 20 and 29 and 'occupation' as 'programer'
9. Exit
--------------------------------
"
fitem="./$1"
fdata="./$2"
fuser="./$3"

while true
do

read -p "Enter your choice [ 1-9 ] " inputnum
echo ""


case $inputnum in
1) read -p "please enter the 'movie id'(1~1682) :" choice
echo ""
cat "$fitem" | awk -F\| -v choicemovie="$choice" '$1 == choicemovie {print $0}'  

;;

2) read -p "Do you want to get the data of 'action' genre ovies from 'u.item'?(y/n) :" choice
echo ""-F
if [ "$choice" = "y" ]
then
cat "$fitem" | awk -F\| '$7 == 1 {print $1" "$2; count++} count == 10 {exit}'
fi
echo ""

;;

3) read -p "Please enter the 'movie id' (1~1682) :" choice
echo ""
cat "$fdata" | awk -F"\t" -v choicemovie="$choice" '$2 == choicemovie {sum+=$3; count++} END {print "average rating of " choicemovie ": " sum/count}'
echo ""

;; 

4) read -p "Do you want to delete the 'IMDb URL' from 'u.ite'? (y/n) " choice
echo "" 
if [ "$choice" = "y" ]
then 
cat "$fitem" | sed -E 's/http:[^\)]*\)//' | awk -F\| '{print $0; count++} count == 10 {exit}'
echo ""     
fi

;;

5) read -p "Do you want to get the data about users from 'u.user'? (y/n) :" choice
echo ""
if [ "$choice" = "y" ]
then
cat "$fuser" | sed  -e 's/M/male/g' -e 's/F/female/g' | awk -F\| '{print "user " $1 " is " $2 " years old " $3 " " $4; count++} count == 10 {exit}'
echo ""
fi

;;

6) read -p "Do you want to Modify the format of 'release data' in 'u.item'?(y/n) :" choice
echo ""
if [ "$choice" = "y" ]
then
cat "$fitem" | tail -n 10 | sed -E -e 's/([0-9]{2})-([A-Za-z]{3})-([0-9]{4})/\3\2\1/g' -e 's/Jan/01/g' -e 's/Feb/02/g' -e 's/Mar/03/g' -e 's/Apr/04/g' -e 's/May/05/g' -e 's/Jun/06/g' -e 's/Jul/07/g' -e 's/Aug/08/g' -e 's/Sep/09/g' -e 's/Oct/10/g' -e 's/Nov/11/g' -e 's/Dec/12/g'  
echo ""
fi
;;

7) read -p "please enter the 'user id' (1~943) :" choice
echo "" 
movieidset=$(cat "$fdata" | awk -F"\t" -v userid="$choice" '$1 == userid {print $2}' | sort -n | tr '\n' '|')
echo "$movieidset"
echo ""

for var in $(seq 1 10)
	do

	seqmovieid=$(echo "$movieidset" |awk -F"|" -v var="$var" '{print $var}')
	cat "$fitem" | awk -F\| -v mid="$seqmovieid" '$1 == mid {print $1 "|" $2}' | sort -t"|" -n

	done   
	echo""
	;;

	8) read -p "Do you want to get the average 'rating' of movies rated by users with 'age' between 20 and 29 and 'occupation' as 'programmer'?(y/n) :" choice
	if [ $choice = "y" ]
	then

	uidset=$(cat "$fuser" | awk -F\| -v mid="$choice" '$2 >= 20 && $2<=29 && $4 == "programmer"{print $1}')


	cat "$fdata" | awk -F"\t" -v uids="$uidset" 'BEGIN {split(uids, arr, " "); for (i in arr) u[arr[i]] = 1}
	$1 in u {movies[$2]+=$3; count[$2]++}
	END {for (movie in movies) {average = movies[movie] / count[movie]; print movie, average}}' | sort -n 


	fi
	;;
	9) echo "Bye !"
	break
	;;

	esac
	done
