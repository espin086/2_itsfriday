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
    echo "--h                               Help Menu"
    echo "--Oath2SetUp                      Linkedin SetUp Instructions"
    echo "--SearchContacts                  Save Company/Title Email Lists"
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

if [ $1 = "--SearchContacts" ]
then

    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "The Walt Disney Company" "Director"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "The Walt Disney Company" "SVP"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "The Walt Disney Company" "Vice President"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "The Walt Disney Company" "Recruiter"


    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Amazon" "Director"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Amazon" "SVP"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Amazon" "Vice President"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Amazon" "Recruiter"

    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Google" "Director"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Google" "SVP"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Google" "Vice President"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Google" "Recruiter"

    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Facebook" "Director"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Facebook" "SVP"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Facebook" "Vice President"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Facebook" "Recruiter"

    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Netflix" "Director"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Netflix" "SVP"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Netflix" "Vice President"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Netflix" "Recruiter"

    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Apple" "Director"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Apple" "SVP"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Apple" "Vice President"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Apple" "Recruiter"

    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "The Walt Disney Studios" "Director"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "The Walt Disney Studios" "SVP"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "The Walt Disney Studios" "Vice President"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "The Walt Disney Studios" "Recruiter"

    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Warner Bros. Entertainment Group of Companies" "Director"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Warner Bros. Entertainment Group of Companies" "SVP"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Warner Bros. Entertainment Group of Companies" "Vice President"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Warner Bros. Entertainment Group of Companies" "Recruiter"


    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Hulu" "Director"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Hulu" "SVP"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Hulu" "Vice President"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Hulu" "Recruiter"

    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Snap Inc." "Director"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Snap Inc." "SVP"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Snap Inc." "Vice President"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Snap Inc." "Recruiter"

    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Microsoft" "Director"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Microsoft" "SVP"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Microsoft" "Vice President"
    python /Users/jjespinoza/GoogleDrive/2_projects/2_itsfriday/1_src/2_python/2_pull_data.py --SearchContacts "Microsoft" "Recruiter"


fi




