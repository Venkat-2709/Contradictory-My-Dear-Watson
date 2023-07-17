# Contradictory, My Dear Watson

This project focused on Natural Language Inference (NLI), a subfield of Natural Language Processing (NLP). The goal was to develop an accurate NLI model capable of determining the logical relationship between pairs of sentences in multiple languages. The dataset consisted of premise-hypothesis pairs in fifteen different languages, labeled as entailment, contradiction, or neutral. Advanced NLP techniques, such as transformer-based models like XLM-RoBERTa, were utilized to handle the complexity and diversity of the dataset. The project also involved preprocessing techniques, model building, evaluation, and deployment through a Django web app and Docker containerization.

## Creating Virtual Environment (Recommended)

To create a virtual environment before starting the application, you can follow these instructions:

Open a terminal or command prompt.

Navigate to the project directory where you have the application files. In this go to main directory.

ou can install it using pip by running the following command: 
```
pip install virtualenv
````
Create a new virtual environment by running the following command:
```
virtualenv venv
```
Activate the virtual environment by running the appropriate command based on your operating system:

For Windows:
```
venv\Scripts\activate
```
For macOS and Linux:
```
source venv/bin/activate
```
After activating the virtual environment, you will see the virtual environment name in your terminal prompt.

Install the required dependencies by running the following command:
```
pip install -r Contradictory_django\requirements.txt
```
This will install all the necessary packages and dependencies specified in the requirements.txt file. Now you run the application.

## Download the dataset

Install the Kaggle API by running the command pip install kaggle in your terminal or command prompt.

Go to the Kaggle website (www.kaggle.com) and sign in to your account.

Open the dataset page for **Contradictory, My Dear Watson** on Kaggle.

Click on the **Copy API command** button, which looks like a clipboard. This will copy the API command to your clipboard.

Paste the username and key in python notebook/

Wait for the download to complete. The dataset will be saved as a compressed file (e.g., .zip or .tar).

Extract the files from the compressed file if necessary, using appropriate software or commands.

You now have access to the **Contradictory, My Dear Watson** dataset and can use it for your NLP project.

Or, You can also use the files provided in the Project.zip folder

## Running the notebook

You can run the notebook in Google Colob or Locally (Need to use GPU). It will take sometime to run the notebook fully and get the results. Once you run the notebook **large_model.h5** wil be created and then copy the saved model and store it in 
```
Contradictory_django/
┣ content/
``` 
In this folder, then you can start running the application by following instructions.

## Running the application 

There are 3 ways to run the applications:

First, You can go the **Contradictory_django** directory and make sure you have the files in content folder and run the following command.

```
Contradictory_django/
┣ content/
┣ Contradictory_django/
┣ django_app/
┣ node_modules/
┣ contradictory-app.tar
┣ db.sqlite3
┣ Dockerfile
┣ manage.py
┣ package-lock.json
┗ requirements.txt
```

```python
python manage.py runserver
```

Open the http://localhost:8000/ webpage on chrome or any browser to access the webpage and use the app.

Second, you can use the **contradictory-app.tar** file located in Contradictory_django folder.

Open a terminal or command prompt. Transfer the contradictory-app.tar file to the desired location on your machine. Navigate to the directory where the contradictory-app.tar file is located. Run the following command to import the Docker image from the tar file:

```
docker load -i contradictory-app.tar
```
Run the Docker container using the command:
```
docker run -p 8000:8000 contradictory-app
```
This will start the container and map port 8000 of the host machine to port 8000 of the container, allowing access to the web app. Open the http://localhost:8000/ webpage on chrome or any browser to access the webpage and use the app.

Third (best option), you can use Docker image in the Docker Hub to load the application for that: 

Download Docker on your comnputer using following information https://docs.docker.com/get-docker/

Sign up for an account on Docker Hub at https://hub.docker.com/. If you do not have it. 

Then open the command prompt and enter the following command
```
docker pull venkat2797/contradictory-app:latest
```

This will take some time to load the Docker image and can run the Docker container using the command:

```
docker run -p 8000:8000 venkat2797/contradictory-app:latest
```
This will start the container and map port 8000 of the host machine to port 8000 of the container, allowing access to the web app. Open the http://localhost:8000/ webpage on chrome or any browser to access the webpage and use the app.