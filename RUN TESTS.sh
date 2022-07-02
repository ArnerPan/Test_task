#!/bin/bash


	Purple='\033[0;35m'
	RED='\033[0;31m'
	GREEN='\033[0;32m'
	NOW=`date +%Y-%m-%d`
	Blue='\033[0;34m'
	Cyan='\033[0;36m'
    NC='\033[0m' # No Color
	
	_user="$(id -u -n)"
	

    printf "${Blue}Todays is ${NC}${Purple} %s${NC} \n" $NOW
	printf "${Blue}Greetings${Cyan} %s ${NC}\n" $_user
	
	
	    str="and..."
	for (( i=0; $i<${#str}; i=$(($i+1)) ))
   do
      printf "${GREEN}${str:$i:1}${NC}";
      sleep 0.3;
   done
   printf "\n"
	    str="WELCOME BACK COMMANDER_";
   for (( i=0; $i<${#str}; i=$(($i+1)) ))
   do
      printf "${GREEN}${str:$i:1}${NC}";
      sleep 0.05;
   done
   printf "\n"
   
   	    str="INITITATING TESTS_";
   for (( i=0; $i<${#str}; i=$(($i+1)) ))
   do
      printf "${GREEN}${str:$i:1}${NC}";
      sleep 0.05;
   done
   printf "\n"
	
	 pytest --alluredir=allure-report/ tests 
	 allure serve allure-report/




