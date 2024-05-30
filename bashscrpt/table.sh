#! /bin/bash
echo "Enter the number: "
read num
for ((i=1; i<=10; i++))
do 
	prdct=$(($num*$i))
	echo "$num * $i =  $prdct"
done
