# breizhcamp_2023
RPI project for Breizhcamp 2023


## Installation du service Breizhcamp. 


```shell

# Dépendance nécessaire pour l'utilisation des ports GPIO
sudo apt-get install -y python3-gpiozero
sudo cp ~/breizhcamp_2023/breizhcamp.service /etc/systemd/system/breizhcamp.service
sudo systemctl enable breizhcamp.service
sudo systemctl start breizhcamp.service

```