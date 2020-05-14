read -p "Enter a number" num
start=$(date +"%T")
echo $start
read -p "Enter a number" num
endtime=$(date +"%T")
echo $endtime
timeElapsed=$(($endtime-$start))
echo "Time elapsed from Start to Stop is:" $timeElapsed
