#! bin/bash
echo "Enter the number: "
read num
i = 1
while [$i -lt 10]
do 
	prd = $(($num*$i))
	echo "$num * $i = $prd"
	((i++))
done
