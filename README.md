
(1) Running the App

	(a) Use the below command to create database tables
		This is a one time step

		rm -rf build
		rm -rf dist
		rm -rf bin
		rm -rf entry_point_test
		rm -rf entry_point
		virtualenv entry_point
		source entry_point/Scripts/activate
		pip install -e .
		python entry_point/Scripts/activate_this.py
		python entry_point/Scripts/vehicles-run-script.py
		# virtualenv entry_point_test
		# source entry_point_test/Scripts/activate
		python setup.py build
		python setup.py install
		python db.py


	(b) Build the npm packages
		cd vehicles/
		npm run build

	(c) Python Flask App  -- Start the python server

		python vehicle_app.py

(2) Use the application using the browser

		http://127.0.0.1:53000/

(3) Pre-requisites:

	(a) Make sure you have the following installed

		(a.1) Python
		(a.2) MySQL
		(a.3) Flask

	  You may use the following command for the python module 
			installations

		Install Flask using Pip pip install Flask. The following command can be used.
			pip install -r requirements.txt

				This command will install the following python modules
					Flask==0.10.1
					PyMySQL
					requests
					configparser
					GoogleAppEngineCloudStorageClient
					Flask-Migrate
					Flask-SQLAlchemy
					mom
					suds-jurko
					boto
					httplib2
					oauth2client>=1.5.2
					pyOpenSSL>=0.13
					SocksiPy-branch==1.01
					retry_decorator>=1.0.0
					six>=1.6.1
					gcs-oauth2-boto-plugin
					google-api-python-client
					lib
					virtualenv
					flask-cors

    (b) Install the npm dependencies
    		You may use the following steps

			npm install

		(c) configuration information:

			config.py contains database user information
			it can take config data from environment variables
				as well

		(d) get an account from 
			https://cloud.google.com/storage/docs/json_api/

		(e) Google Cloud SDK

				install https://cloud.google.com/sdk/docs/

				https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe

				gcloud components install --help
				gcloud components list
				gcloud auth login
				gsutil config -a
				gcloud components install app-engine-python
				gcloud components install app-engine-python-extras

		(f) DO one of the following
   		(f.1) add/edit the below to .boto file
   			under section [Credentials]

		   	export gs_access_key_id=*
				export gs_secret_access_key=*

   			or

   		(f.2) 

   			(1) Update the configuration data in config.py

   			or

   			(2) define OS ( operating system ) environment variable
   		using export in a shell

   			or in the OS environment options

				export gs_access_key_id = *
				export gs_secret_access_key = *
				export LFileData_UPLOAD_IMAGE_LOCAL_DIR=static/upimages
				export ENV_VEHICLE_SERVICE_PORT

				(3) Note: If the OS's environment variable exists,
					the OS environment variable value will be used instead of data from config.py
					
