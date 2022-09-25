#!/usr/bin/env bash

# Update the server
# Do the following and reboot before running this script

# apt update
# apt upgrade -y
# Edit /etc/ssh/sshd_config
# PasswordAuthentication no
# UsePAM no
# then reboot




# install python and build tools
apt install -y -q python3-pip python3-dev python3-venv build-essential


# setup firewall and fail2ban
ufw allow 22
ufw allow 80
ufw allow 443
ufw --force enable
apt install -y fail2ban

# prepare app directory
mkdir /apps
chmod 777 /apps
mkdir -p /apps/logs/greencity_api

# adding a dummy user
useradd -M apiuser
usermod -L apiuser

# set permission to user
apt install acl -y
setfacl -m u:apiuser:rwx /apps/logs/greencity_api


# setup the virtual environment for the app
cd /apps
python3 -m venv venv
. /apps/venv/bin/activate
pip install --upgrade pip setuptools wheel


# git clone the project
git clone https://github.com/yongkheng/greencity app_repo
cp /apps/app_repo/settings_dummy.json /apps/app_repo/settings.json

# Install python dependencies
cd /apps/app_repo
pip install -r requirements.txt


# setup nginx
apt install -y nginx
cp /apps/app_repo/server/nginx/greencity.nginx /etc/nginx/sites-enabled/
# do not delete if you are using default
rm /etc/nginx/sites-enabled/default
update-rc.d nginx enable
service nginx restart

# setup gunicorn
pip install --upgrade gunicorn uvloop

# Copy and enable the daemon
cp /apps/app_repo/server/systemd/greencity.service /etc/systemd/system/

systemctl start greencity
systemctl enable greencity


echo
echo "Don't forget to set your external api key in settings.json, then restart service"
