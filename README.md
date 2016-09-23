#CPSC 223P - Python Programming

__Author Name:__ Kathy Saad<br>
__Project Title:__ Assignment 8 - My Django Site<br>
__Project Status:__ Working<br>

**********************************************************************************************************************

__Instructions:__  
In this assignment we will build upon our knowledge of how to use virtualenv and pip to create a virtual environment to craft a development environment for our Python software to create an environment for developing a naïve web application. The tool will use to create our web application is Django (as you already know, the 'd' is silent).  

Django is a framework that helps software developers rapidly create applications by automating as much as possible and adhering to the DRY Principle. Therefore, installing Django into your virtual environment will introduce new programs and tools to help you generate parts of your application which you can then customize to meet your specific needs.  

The second part of these exercises is to get comfortable using Google Cloud Services. After creating your web application, the way to deliver the application to your friends and family is by publishing the application. Google provides two services for hosting web applications. The first is Google App Engine. This service is one where you can take your software, send it to Google, and they will provide computers to execute your software. You can access your software by visiting a url like http://your-app-id.appspot.com/. The other service is Google Compute Engine which is a service that enables you to create and provision virtual computers on Google's network. We will be using Google Compute Engine.  

The services provided by Google are commercial services. This exercise is not meant to be an endorsement of Google or its services but to serve as an introductory exercise in using Python to do something more interesting. Google has many competitors such as Amazon, Rackspace, Microsoft, IBM, and many others.  

Our goal with this exercise is to learn the basics of using Django to make a web application and then to publish our web application to Google App Engine. If time permits, we will look at using Google Compute Engine as well.  

1.	Do not submit - Create a virtual environment in a directory named django-tutorial. Install django using pip, pip install django. Read and follow every step in the Django tutorial. (You are recommended to follow the steps of the tutorial no less than two times.)  

2.	Do not submit - Create a virtual environment in a directory named FirstnameLastnameSiteEnv, where Firstname is your firstname and Lastname is your lastname. For example, if your name is Peter Parker, then the directory is named PeterParkerSiteEnv. In that directory create a Python virtual environment for Python and install Django using pip. Next, use django-admin to create a new Django project named FirstnameLastnameSite, where Firstname is your firstname and Lastname is your lastname. Next create a Django application using python manage.py named fortune.  

The application fortune must do the following:
-	The URL /fortune will return a random aphorism.
-	The URL /fortune/\d+ will return the aphorism with the id that matches the \d+ regular expression.
-	The URL /fortune/short will return an aphorism that is shorter than 140 characters
-	The URL /fortune/startrek will return a random aphorism that is from the startrek file.  

In order to complete this exercise you will need to import the data from our previous exercise into your Django site's database. You can do this by downloading the file fortunes_dump.sql.zip, unzipping it, and using the following command sqlite3 db.sqlite4 < fortunes_dump.sql. Make sure that you are in the same directory as your Django site's database.  

3.	Do not submit - Modify the site you developed in the previous exercise and add to it the ability to show a random image using flickr.com's feed API. You will need to use an XML parser to extract the image link information out of the XML feed data flickr.com provides. You are recommended to use BeautifulSoup 4 which can trivially be added to your Python virtual environment using pip.  

4.	Do not submit - Modify/Add the static templates of the site such that the root page of the site introduces you and provides a link to your resume, a link to your fortune application and links to any other relevant pages (such as your GitHub account, StackOverflow profile, LinkedIn profile, etc.). (If you do not have a resume, make one)  

5.	Use a new or an existing Google Account to sign up for Google's cloud services. Using the configuration file provided by the instructor (forthcoming), configure a virtual machine (VM) within Google Compute Engine (GCE) to host your web application. Configure the firewall, webserver and upload your web application. Test your VM instance to verify that you can view your site from your home network and from CSUF's network. Submit the contents of FirstnameLastnameSiteEnv to the course drop box and complete the online form (forthcoming) with the URL of your Django site (this is the IP of your GCE VM).  

6.	Prepare your application to be copied to your GCE VM by following these steps.  
  	-	Verify that your project works, i.e. python manage.py runserver  
    	-	Freeze the environment's requirements, i.e. pip freeze > requirements.txt  
      	-	Remove the virtual environment, i.e. rm -r env  
        -	Zip your project, i.e. zip -r FirstnameLastnameSiteEnv.zip FirstnameLastnameSiteEnv  
7.	With your Google Account, perform the following steps:  
	-	Create a project via the Google Developer's Console  
	-	Enable the Google Compute Engine API for the project  
	-	Add a Debian GCE VM to the project, i.e. gcloud compute instances create djangovm --image debian-7 --zone us-central1-a  
	-	Add a firewall rule to allow HTTP traffic, i.e. gcloud compute firewall-rules create allow-http --description "Incoming http allowed." --allow tcp:80  
	-	Copy your project over to the VM, i.e. gcloud compute copy-files FirstnameLastnameSiteEnv.zip djangovm:FirstnameLastnameSiteEnv.zip --zone us-central1-a where djangovm is the instance name of your VM.  
	-	Log into your VM, i.e. gcloud compute ssh djangovm --zone us-central1-a; then do the following on the VM:  
		+	curl -O http://delaunay.ecs.fullerton.edu/debian_gceconf.sh  
		+	curl -O http://delaunay.ecs.fullerton.edu/debian_djangopostconf.sh  
		+	sudo sh ./debian_gceconf.sh  
		+	unzip FirstnameLastnameSiteEnv.zip  
		+	cd FirstnameLastnameSiteEnv  
		+	virtualenv -p python3 env  
		+	source env/bin/activate  
		+	pip install -r requirements.txt  
		+	cd  
		+	sudo sh ./debian_djangopostconf.sh  
	-	Visit http://xx.xx.xx.xx/, where xx.xx.xx.xx is your VMs IP address, to confirm that everything worked. If you forgot your VMs IP address you can easily get it with the command gcloud compute instances list.  

Enter your VMs IP address into the course's online form. Make sure your VM is running between Saturday, December 13 2014 and Tuesday, December 16, 2014.  

Your entry in the form must be submitted by December 12, 2014. Submit a zip file of your project (the file you copied onto your GCE VM) to the course drop box system. The zip file submission is due by December 12, 2014 as well.

