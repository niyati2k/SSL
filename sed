1) sed 's/t/T/'
--change t to T (first occurence in each line)

2) sed 's/t/T/g'
--change all lower case t to T

3) sed -i 's/t/T/g' text
--modified the text file 
  (in 1,2 file not changed, t remains t in the file)

4) sed '' BSD
--file reader, w/o passing any commands

5) sed 'p' BSD
--'p' explicitly prints, and naturally also, thus 2 times each line is printed

6) sed -n 'p' BSD
--suppresses the automatic printing

7) sed -n '1,5p' BSD or sed -n '1,+4p' BSD
--told sed to print line 1 through line 5 or told sed to start at line 1 and then operate on the next 4 lines as well.

8)sed -n '1~2p' BSD
--skips 2 lines i.e prints alternate lines

9)sed '1~2d' BSD
--delete every other line starting with the first

10)echo "http://www.example.com/index.html" | sed 's_com/index_org/home_'
--output will be 
  http://www.example.org/home.html
  replaces com/index with org/home

11)sed 's/on/forward/2'
--change only 2nd occurence on to forward

12)sed -n 's/on/forward/2p'
--print where substitution took place

13)sed 's/^.*at/REPLACED/'
--this is the song that never ends
--REPLACED never ends

14)sed 's/^.*at/(&)/' 
--this is the song that never ends
--(this is the song that) never ends

15)sed 's/\([a-zA-Z0-9][a-zA-Z0-9]*\) \([a-zA-Z0-9][a-zA-Z0-9]*\)/\2 \1/'
--Every group of search text marked with parentheses can be referenced by an escaped reference number. For instance, the first parentheses group can be referenced with "\1", the second with "\2" and so on. 
--this is the song that never ends
--o/p--is this the song that never ends
--yes, it goes on and on, my friend
--o/p--yes, goes it on and on, my friend
--escape ( helps making it a group

16)sed 's/\([^ ][^ ]*\) \([^ ][^ ]*\)/\2 \1/'
--this is the song that never ends
--o/p--is this the song that never ends
--yes, it goes on and on, my friend
--o/p--it yes, goes on and on, my friend

17)

































