
# Agri-IoT-for-Africa



DHT22 Setup

sudo apt-get install git
DHT22 configuration steps


1.wget https://github.com/adafruit/Adafruit_Python_DHT/archive/master.zip
2  unzip master.zip
3.  cd Adafruit_Python_DHT-master

4. sudo apt-get update && sudo apt-get upgrade
5. sudo apt-get install build-essential python-dev
6. sudo python(3.7 or 2.7) setup.py install
7. cd examples/
8. vim  simpletest.py (to write the event measurement codes)
9. python simpletest.py (to start measurement)


Server-client code link: Bluetooth Programming with Python 3 - Kevin Doran

Python Socket Programming - Server, Client Example - JournalDev

 python3.7 -m pip install pybluez  (Helps to define BLE package that calls the RFCOMM fxn)
sudo apt-get update && sudo apt-get upgrade

Create client-server or master-slave architecture using the code in the above link
Reinstalled Adafruit with 3.7 modules: sudo python(3.7 or 2.7) setup.py install
Develop code for BT comm. We had data type exception today to be corrected tomorrow: bad file descriptor

System response to external thresholds.

CH socket to accept multiple communication

Connected multiple SNs to the CH and transmitted sensory data packets from each SN. Cluster formation is possible in BLE.
To implement crontab: crontab -e
Assign period and task
Generate a database of periodic sensory data and save in .csv file
If s RPi is used as a BS, then the blueman library should be installed to communicate the crontab-scheduled data sample.
run-parts /etc/cron.daily for immediate testing of the cron



Using git clone and the git link, we pushed the code into github

Command: Git clone https://github.com/eeffah-agri-iot/Agri-IoT-for-Africa.git

git clone https://github.com/WiLab/agri-iot.git (it creates a clone repository from github to the local machine e.g. on the pi directory 
cd agri-iot/ (to relocate to the locally cloned directory/repository) 
Copy the server  files into this local repository
git config --global user.email "you@example.com" (after installation of git, you must configure it using your credentials) 
  git config --global user.name "Your Name" (and then your username)
git commit -m "The server code of the CH (accepts multiple clients)" (puts the changes in your local repository that want to push to the github repository)
git push origin main (this command will require your email and github password to upload your local content/changes to github repository)




Some important links
https://stackabuse.com/scheduling-jobs-with-python-crontab/
Python Socket Multiple Clients - Stack Overflow
Python Socket Programming - Server, Client Example - JournalDev
Bluetooth Programming with Python 3 - Kevin Doran
https://microchipdeveloper.com/wireless:ble-link-layer-channels
https://realpython.com/python-sockets/#multi-connection-server


