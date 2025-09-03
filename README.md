# FitnessApp
Python Application to journal workouts and their durations.

# Deliverables for Assignment
 
1.	Application Development -- Using Flask (app.py) 
2.	Version Control System (VCS) Implementation -- GIT Repository (This Repo) 
3.	Unit Testing Framework Integration (All the test are present under test folder) 
4.	Automated Testing Configuration. (created pytest workflow)
5.	Containerization with Docker. (Dockerfile created for run the application as an image from local)
6.	CI/CD Pipeline with GitHub Actions (pytest and docker workflow created)

----------------
To run the application with the help of python ; follow below steps

Move to directory where you want to clone the git repo 
```
git clone https://github.com/2024ht66047/FitnessApp.git
```
then to change directory to move to desiried folder
```
cd FitnessApp
```
if python is already installed ; run
```
python app.py 
```
below message pops-up 
```
* Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
```
open any browser and run the mentioned localhost url hosted on port 5000 -- http://127.0.0.1:5000

you should be able to see below window in your browser;

<img width="668" height="390" alt="image" src="https://github.com/user-attachments/assets/9fbbbe1d-db85-4058-88bc-6e3a8feee549" />

Enter workout and duration details, to log your workouts into the App. 

whenever there is a entry you should be seeing below POST messages in the app logs;

<img width="657" height="461" alt="image" src="https://github.com/user-attachments/assets/d2d1e081-ffa6-4b21-9ea5-31cbc7e6643b" />


```
127.0.0.1 - - [03/Sep/2025 08:51:57] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/Sep/2025 08:51:57] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [03/Sep/2025 08:53:23] "POST / HTTP/1.1" 302 -
127.0.0.1 - - [03/Sep/2025 08:53:23] "GET / HTTP/1.1" 200 -
```

To run pytests from your local ; make sure that pytest is already installed or you can install all the pre-requistes using the requirements.txt file 

```
pytest -v
```

output:
```
collected 7 items

tests/test_add_valid_workout.py::test_add_valid_workout PASSED                                                                                                      [ 14%]
tests/test_add_workout_invalid_duration.py::test_add_workout_with_invalid_duration PASSED                                                                           [ 28%]
tests/test_add_workout_with_empty_fields.py::test_add_workout_with_empty_fields PASSED                                                                              [ 42%]
tests/test_home_page_loads.py::test_home_page_loads PASSED                                                                                                          [ 57%]
tests/test_post_to_home_redirects.py::test_post_to_home_redirects PASSED                                                                                            [ 71%]
tests/test_view_empty_workouts.py::test_view_empty_workouts PASSED                                                                                                  [ 85%]
tests/test_view_multiple_workouts.py::test_view_multiple_workouts PASSED                                                                                            [100%]

============================================================================ 7 passed in 0.10s ============================================================================
```
----------

To run the application as a docker container ; follow below steps

Once you have Docker / Podman / Rancer installed,  use below commands to run the application as a containerised application  --

```
docker pull 2024ht66047/my-image:latest
```
Below images pull will be seen 
```
Trying to pull docker.io/2024ht66047/my-image:latest...
Getting image source signatures
Copying blob sha256:72e8e193aa94d19c7f1bcbc00737a83d1906bcc1e51965c2873f081eb87bd3a0
Copying blob sha256:396b1da7636e2dcd10565cb4f2f952cbb4a8a38b58d3b86a2cacb172fb70117c
Copying blob sha256:7732878f45d9e71f91ce50493915297cca1bde392445d9ddcc0f378a200967bf
Copying blob sha256:f72aeea8e497e9ef39ebf37ed3823292cc2f742719b26c39aeeafc4013c2f6ea
Copying blob sha256:3a195ff1e16155a2ca71eee2cc2c4e467119c644d0360b7c2f6e6d9633f9358b
Copying blob sha256:e705832ee37c7c589441bb1923a72a691a23bb5cca131c1fe06d840d5c45e31f
Copying blob sha256:9e99d352528f7f8348363d754f4119ef8624062f7ff8f81cb4e965b824268147
Copying blob sha256:d4392dc686131edcc583dc2ec422c5379a8a69d1b2aab40f0274aaffdaa88602
Copying config sha256:d218c24bf892b1028d738978a420ceabb21b0f2b526db2e2b14f1c4b1017c15c
Writing manifest to image destination
```
Run the pulled docker images in detached mode , re-directing the port 5000

```
docker run -it -d -p 5000:5000 --name DevOps_Assignment d218c24bf892  #last hexa code is the image ID
```
run docker ps command to see the status and docker logs command to see the POST requests reaching the application
use http://127.0.0.1:5000 address to view the application in the browser.

```
docker ps

CONTAINER ID  IMAGE                                        COMMAND               CREATED         STATUS         PORTS                   NAMES
1dd2ba13cc57  docker.io/2024ht66047/my-image:latest        flask run --host=...  13 seconds ago  Up 13 seconds  0.0.0.0:5000->5000/tcp  DevOps_Assignment


docker logs -f 1dd2ba13cc57

* Serving Flask app 'app.py'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [03/Sep/2025 03:32:55] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/Sep/2025 03:32:56] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [03/Sep/2025 03:36:29] "POST / HTTP/1.1" 302 -
127.0.0.1 - - [03/Sep/2025 03:36:29] "GET / HTTP/1.1" 200 -
```



