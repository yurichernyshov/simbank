#!/bin/sh

git clone https://github.com/yurichernyshov/simbank.git

cd ./simbank/project

docker-compose build

docker-compose up -d

status=0

while [ 1 ]
do
echo "---------------------------------------------------"
echo "|                                                 |"
echo "| simbank application is started                  |"
echo "| options:                                        |"
echo "| 1): createsuperuser                             |"
echo "| 2): start simbank                               |"
echo "| 3): stop simbank                                |"
echo "| 4): status                                      |"
echo "| x): exit                                        |"
echo "|                                                 |"
echo "---------------------------------------------------"

read status

case $status in
 "1" )
   docker-compose exec web python manage.py createsuperuser
 ;;
 "2" )
   docker-compose start
 ;;
 "3" )
   docker-compose stop
 ;;
 "4" )
   docker info
 ;;
 "x" )
   docker-compose stop
   exit 0
 ;;
esac

done
