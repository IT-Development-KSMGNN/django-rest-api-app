from ubuntu:18.04

maintainer Dockerfiles

run apt-get update
run apt-get install -y python3 python3-dev python3-setuptools
run apt-get install -y nginx supervisor
run apt-get install -y python3-pip
run apt-get install -y python3-venv
run pip3 install uwsgi
run apt-get install nginx
run apt-get install -y libpq-dev
run apt install -y unixodbc-dev

#Copy code to docker image
add . /home/docker/code/

#Create venv for project
run python3 -m venv /home/docker/code/env

#Config files
run echo "daemon off;" >> /etc/nginx/nginx.conf
run rm /etc/nginx/sites-enabled/default
run ln -s /home/docker/code/nginx-app.conf /etc/nginx/sites-enabled/
run ln -s /home/docker/code/supervisor-app.conf /etc/supervisor/conf.d/
run /home/docker/code/env/bin/pip install wheel

# run pip install
run /home/docker/code/env/bin/pip install -r /home/docker/code/app/requirements.txt
run echo "yes" | /home/docker/code/env/bin/python /home/docker/code/app/manage.py collectstatic

expose 80
cmd ["supervisord", "-n"]
