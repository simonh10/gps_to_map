#!/bin/bash
LOGFILE=${HOME}/gpsdata.log
echo $LOGFILE
while true
do
	ncat -k -l -p 51234| tr "()" "|\n" >> $LOGFILE
done
