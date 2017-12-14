#!/bin/bash
clear
if [ $1 = "--h" ]
then
	echo ""
    echo "************** HELP FILE **************"
    echo ""
    echo "Author: JJ Espinoza"
    echo "Description: Creates and Manages Github Repository"
    echo ""
    echo "---------------------------------------"
    echo ""
    echo "Commands:                                                 Info:"
    echo "./1_github.sh --h		                          Help Menu"
    echo "./1_github.sh --create [localpath] [github_url]	          Creates Github folder"
    echo "./1_github.sh --pull [localpath]	                  Refreshes local repository"
    echo "./1_github.sh --push [localpath]	                  Updates remote repository"
    echo ""
    echo "Current Directory is: "
    pwd
    echo ""
    echo "---------------------------------------"

fi

if [ $1 = "--create" ]
then
	echo ""
    echo "************** Creating Github Repository **************"
    echo ""
    echo "---------------------------------------"
    echo "Creating Repository in:"
    echo "---------------------------------------"
    echo ""
    cd $2
    git init
    echo ""
    echo "---------------------------------------"
    echo "Status of Repository:"
    echo "---------------------------------------"
    git status
    echo ""
    echo "---------------------------------------"
    echo "Modifications in Local Repository:"
    echo "---------------------------------------"
    echo ""
    git add .
    echo ""
    git status
        echo ""
    echo "---------------------------------------"
    echo "Changes to be Committed:"
    echo "---------------------------------------"
    echo ""
    git commit -m "first commit"
    git status
    #git remote add origin https://github.com/espin086/0__mytools.git/
    git remote add origin $3
    git remote -v
    echo "---------------------------------------"
    echo "Pulling Remote Changes:"
    echo "---------------------------------------"
    echo ""
    git pull
    echo "---------------------------------------"
    echo "Pushing Local Changes:"
    echo "---------------------------------------"
    echo ""
    git push -u origin master
    git push
    git status
    echo ""
    echo "New Repository Created in:"
    echo "---------------------------------------"
    echo $2
    echo "---------------------------------------"

fi

if [ $1 = "--pull" ]
then
	echo ""
    echo "************** Pulling from Github Repository **************"
    echo ""
    echo "---------------------------------------"
    echo "Pulling Repository"
    echo ""
    echo "Local repository has been refreshed:"
    echo "---------------------------------------"

fi

if [ $1 = "--push" ]
then
	echo ""
    echo "************** Updating Remote Github **************"
    echo ""
    echo "---------------------------------------"
    echo "Pushing to Remote Repository"
    echo ""
    echo "Remote repository has been updated:"
    echo ""
    echo $2
    echo "---------------------------------------"

fi


