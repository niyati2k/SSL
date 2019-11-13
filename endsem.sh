# echo $((7+RANDOM%100))

#Q7*******************************
# cd $1
# find . -type f -name manage.py
# c=0
# cd ~
# for i in *
# do 
# 	((c++))
# done
# echo ${c}



# **********************************************************
#brace exp
#touch  {a,b,c}{d,e,f}.c

#cd $1
# find . -type f -name '*.c' -exec rm {} \;
# find . -type f -size 0 -exec rm {} \;

# *************************************************


# cp $1 ninew.cpp
# ********************

numload()
{
	grep "num" t.txt g.txt >> hh.txt
}
numload





#*****************************************************

# if [ $2 ]
# then
# 	echo "$1 + $2"|bc -l
# elif [ $1 ]
# then
# 	echo " one missing"
# else
# 	echo "both missing"
# fi


# n=$#
# sum=0
# c=1
# for i in $*
# do
# 	if [ $i%2 -eq 0 ]
# 	then
# 		sum=`echo "$sum + $i " | bc -l`
# 	fi
# done
# echo $sum	


n=`echo $((7 + RANDOM % 1))`
a=23
s=`echo "$n + $a"|bc -l`
echo $s
