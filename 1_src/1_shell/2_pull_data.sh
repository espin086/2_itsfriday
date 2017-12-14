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
    echo "Commands:                               Info:"
    echo "./2_pull_data.sh --h		        Help Menu"
    echo "./2_pull_data.sh --topmovies [month]	Pulls box office revenue per month[month]"
    echo "./2_pull_data.sh --mojofilm           Pulls film metadata from box office mojo"
    echo "./2_pull_data.sh --mojoactor          Pulls actor metadata from box office mojo"
    echo "./2_pull_data.sh --stocks             Pulls stock market data for entertainment companies"
    echo "./2_pull_data.sh --feds               Pulls economic data from US Federal Reserve Bank"
    echo "./2_pull_data.sh --linkedin [jobtitle] Pulls job data from Linkedin API"
    echo ""
    echo "Current Directory is: "
    pwd
    echo ""
    echo "---------------------------------------"

fi

