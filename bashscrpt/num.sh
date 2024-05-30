#! /bin/bash
echo "Enter the number: "
read num
for ((i=1; i<=$num; i++))
do
	sum=$(($sum+$i)) 
	echo "$i"
done
echo "Sum of above numbers: $sum"
