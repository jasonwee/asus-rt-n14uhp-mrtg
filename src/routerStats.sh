#!/bin/bash

. /etc/asus-rt-n14uhp-mrtg/n14uhp.conf

INFO="`curl -s -m 30 'http://'$ROUTER_IP'/update.cgi' -X POST -H "Host: $ROUTER_IP" -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/2010001 Firefox/28.0 Iceweasel/28.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Referer: http://'$ROUTER_IP'/Main_TrafficMonitor_realtime.asp' -H 'Content-Type: text/plain; charset=UTF-8' -H 'Cookie: dm_install=no; dm_enable=no; hwaddr='$ROUTER_HWADDR'; apps_last=; bw_rtab=WIRELESS0; bw_24tab=WIRELESS0; bw_24refresh=1; daily=1; ymd=1' -H "Authorization: Basic $HTTP_BASIC_AUTHORIZATION" -H 'Connection: keep-alive' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' --data \"output=netdev&_http_id=$HTTP_ID\"`"

# Get transmit and receive bytes.
#
#INFO="netdev = { 'WIRED':{rx:0x125274fb,tx:0x9451055} ,'BRIDGE':{rx:0x143b0a2a,tx:0x9d31e51} ,'INTERNET':{rx:0xb85e6d4,tx:0x73c4fde1} ,'WIRELESS0':{rx:0x38242577,tx:0xc56292cd} }"

# make data easy to parse later.
INFO=${INFO#*\{}
INFO=${INFO%*\}}
#echo $INFO


# wired traffic
wired="`echo $INFO | awk -F\" ,\" '{print $1}'`"
#echo $wired
wired_rx="`echo $wired | sed -E 's/.*rx:(0x[0-9a-f]+).*/\1/'`"
wired_tx="`echo $wired | sed -E 's/.*tx:(0x[0-9a-f]+).*/\1/'`"

# bridge traffic
bridge="`echo $INFO | awk -F\" ,\" '{print $2}'`"
#echo $bridge
bridge_rx="`echo $bridge | sed -E 's/.*rx:(0x[0-9a-f]+).*/\1/'`"
bridge_tx="`echo $bridge | sed -E 's/.*tx:(0x[0-9a-f]+).*/\1/'`"

# internet traffic
internet="`echo $INFO | awk -F\" ,\" '{print $3}'`"
#echo $internet
internet_rx="`echo $internet | sed -E 's/.*rx:(0x[0-9a-f]+).*/\1/'`"
internet_tx="`echo $internet | sed -E 's/.*tx:(0x[0-9a-f]+).*/\1/'`"

# wireless traffic
wireless="`echo $INFO | awk -F\" ,\" '{print $4}'`"
#echo $wireless
wireless_rx="`echo $wireless | sed -E 's/.*rx:(0x[0-9a-f]+).*/\1/'`"
wireless_tx="`echo $wireless | sed -E 's/.*tx:(0x[0-9a-f]+).*/\1/'`"

output=$1
# Final output to MRTG
#
if [ "$output" = "-wired" ]; then
  printf "%d\n" $wired_rx
  printf "%d\n" $wired_tx
  echo 0
  echo 0
elif [ "$output" = "-bridge" ]; then
  printf "%d\n" $bridge_rx
  printf "%d\n" $bridge_tx
  echo 0
  echo 0
elif [ "$output" = "-wireless" ]; then
  printf "%d\n" $wireless_rx
  printf "%d\n" $wireless_tx
  echo 0
  echo 0
elif [ "" = "-cpu" ]; then
  printf "%d\n" $wireless_rx
  printf "%d\n" $wireless_tx
  echo 0
  echo 0
elif [ "" = "-mem" ]; then
  printf "%d\n" $wireless_rx
  printf "%d\n" $wireless_tx
  echo 0
  echo 0
else
  printf "%d\n" $internet_rx
  printf "%d\n" $internet_tx
  echo 0
  echo 0
fi
