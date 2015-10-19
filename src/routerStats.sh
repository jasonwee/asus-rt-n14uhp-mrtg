#!/bin/bash

. /etc/asus-rt-n14uhp-mrtg/n14uhp.conf

INFO="`curl -s -m 30 'http://'$ROUTER_IP'/update.cgi' -X POST -H "Host: $ROUTER_IP" -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/2010001 Firefox/38.0 Iceweasel/38.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Referer: http://'$ROUTER_IP'/Main_TrafficMonitor_realtime.asp' -H 'Content-Type: text/plain; charset=UTF-8' -H 'Cookie: dm_install=no; dm_enable=no; hwaddr='$ROUTER_HWADDR'; apps_last=; bw_rtab=WIRELESS0; bw_24tab=WIRELESS0; bw_24refresh=1; daily=1; ymd=1' -H "Authorization: Basic $HTTP_BASIC_AUTHORIZATION" -H 'Connection: keep-alive' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' --data \"output=netdev&_http_id=$HTTP_ID\"`"

INFO_MEM="`curl -s -m 30 'http://'$ROUTER_IP'/ram_status.asp?_=1445270625000' -X POST -H "Authorization: Basic $HTTP_BASIC_AUTHORIZATION" -H 'Accept-Encoding: gzip, deflate, sdch' -H 'Accept-Language: en-US,en;q=0.8,ms;q=0.6,de-AT;q=0.4,de;q=0.2' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' -H 'Accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01' -H 'Referer: http://'$ROUTER_IP'/device-map/router_status.asp' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed`"

INFO_CPU="`curl -s -m 30 'http://'$ROUTER_IP'/cpu_status.asp?_=1445270625000' -X POST -H "Authorization: Basic $HTTP_BASIC_AUTHORIZATION" -H 'Accept-Encoding: gzip, deflate, sdch' -H 'Accept-Language: en-US,en;q=0.8,ms;q=0.6,de-AT;q=0.4,de;q=0.2' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' -H 'Accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01' -H 'Referer: http://'$ROUTER_IP'/device-map/router_status.asp' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --compressed `"

# Get transmit and receive bytes.
#
#INFO="netdev = { 'WIRED':{rx:0x125274fb,tx:0x9451055} ,'BRIDGE':{rx:0x143b0a2a,tx:0x9d31e51} ,'INTERNET':{rx:0xb85e6d4,tx:0x73c4fde1} ,'WIRELESS0':{rx:0x38242577,tx:0xc56292cd} }"

# make data easy to parse later.
INFO=${INFO#*\{}
INFO=${INFO%*\}}
#echo $INFO
#echo $INFO_MEM
#echo $INFO_CPU

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

mem_total="`echo $INFO_MEM | awk -F= '{print $2}' | awk '{print $1}'`"
mem_free="`echo $INFO_MEM | awk -F= '{print $3}' | awk '{print $1}'`"
mem_used="`echo $INFO_MEM | awk -F= '{print $4}' | awk '{print $1}'`"

cpu="`echo $INFO_CPU | awk '{print $8}' | tr -d ';' `"

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
elif [ "$output" = "-cpu" ]; then
  printf "%d\n" $cpu
  echo 0
  echo 0
  echo 0
elif [ "$output" = "-mem" ]; then
  printf "%d\n" $mem_free
  printf "%d\n" $mem_used
  echo 0
  echo 0
else
  printf "%d\n" $internet_rx
  printf "%d\n" $internet_tx
  echo 0
  echo 0
fi
