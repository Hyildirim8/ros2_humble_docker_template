#!/bin/bash

# X11 erişimi için izin ver
xhost +local:docker

# Docker Compose ile başlat
docker-compose up -d

echo "ROS 2 Humble geliştirme ortamı başlatıldı!"
echo "Konteynere bağlanmak için:"
echo "  docker exec -it ros2-humble-dev bash"
