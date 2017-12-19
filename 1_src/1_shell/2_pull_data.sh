if [ $1 = "--h" ]
then
	echo ""
    echo "************** HELP FILE **************"
    echo ""
    echo "Author: JJ Espinoza"
    echo "Description: Scrapes data from the web"
    echo ""
    echo "---------------------------------------"
    echo ""
    echo "Commands:                         Info:"
    echo "./2_pull_data.sh --h              Help Menu"
    echo "./2_pull_data.sh --Oath2SetUp     Linkedin SetUp Instructions"
    echo ""
    echo "Current Directory is: "
    pwd
    echo ""
    echo "---------------------------------------"

fi

if [ $1 = "--Oath2SetUp" ]
then
    echo ""
    echo "*** Linkedin Provides Information on How to Authenticate API ***"
    echo ""
    /usr/bin/open -a "/Applications/Google Chrome.app" 'https://developer.linkedin.com/docs/oauth2'

    echo ""
    echo "*** Example of How to Use API ***"
    echo ""
    /usr/bin/open -a "/Applications/Google Chrome.app" 'https://ozgur.github.io/python-linkedin/'



fi
