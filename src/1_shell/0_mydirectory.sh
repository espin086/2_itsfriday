1#!/bin/bash


#This is the help menu
if [ $1 = "--h" ]
then
	echo ""
    echo "************** HELP FILE **************"
    echo ""
    echo "Author: JJ Espinoza"
    echo "Description: Creates standardized folder structure"
    echo ""
    echo "---------------------------------------"
    echo ""
    echo "Commands:                               Info:"
    echo "./0_mydirectory.sh --h		        Help Menu"
    echo "./0_mydirectory.sh --create [path]	Creates files located in [path]"
    echo "Current Directory is: "
    pwd
    echo ""
    echo "---------------------------------------"

fi

#This command crates the folders
if [ $1 = "--create" ]
	then
		DIRECTORY=$2
		mkdir $DIRECTORY
	    cd $DIRECTORY

	#CREATING source code directory
	cp -r /Users/jje/Documents/00__mytools/1_starterkit/1_src $DIRECTORY
	mkdir $DIRECTORY/2_data
	mkdir $DIRECTORY/2_data/1_raw
	mkdir $DIRECTORY/2_data/2_clean

fi



