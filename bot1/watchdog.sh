#!/bin/bash

SCRIPT='python3 /home/cedric/bot1/send.py'
LOG=/home/cedric/bot1.log

STEST=spaces/AAAAhdssx6Y
SCGD=spaces/sCD2iwAAAAE
SCORRES=spaces/AAAAm-1QFBM



ps aux |grep [b]ot1/run.py > /dev/null
if [ $? -ne 0 ]; then
	$SCRIPT $SCGD 'daemon bot1 planté' >> $LOG
fi
