# ROS 2 Humble Geliştirme Ortamı

Bu proje ROS 2 Humble ile uygulama geliştirmek için Docker tabanlı bir geliştirme ortamı sağlar.

## Gereksinimler

- Docker
- Docker Compose
- X11 (GUI uygulamaları için)

## Kurulum ve Çalıştırma

### 1. Docker imajını oluşturun:
```bash
docker-compose build
```

### 2. Konteyneri başlatın:
```bash
docker-compose up -d
```

### 3. Konteynere bağlanın:
```bash
docker exec -it ros2-humble-dev bash
```

### 4. Workspace klasöründe ROS 2 workspace'i oluşturun:
```bash
cd /workspace
mkdir -p src
```

### 5. Paket oluşturma örneği:
```bash
cd /workspace
ros2 pkg create --build-type ament_python my_package
# veya C++ için:
ros2 pkg create --build-type ament_cmake my_cpp_package
```

### 6. Workspace'i derleyin:
```bash
cd /workspace
colcon build
source install/setup.bash
```

## Kullanışlı Komutlar

### Konteyneri durdurma:
```bash
docker-compose down
```

### Konteyneri yeniden başlatma:
```bash
docker-compose restart
```

### ROS 2 komutları kontrol etme:
```bash
ros2 --help
```

### Mevcut node'ları listeleme:
```bash
ros2 node list
```

### Topic'leri listeleme:
```bash
ros2 topic list
```

## GUI Uygulamaları

Docker konteyneri X11 forwarding ile yapılandırılmıştır. RViz, Gazebo gibi GUI uygulamalarını çalıştırabilirsiniz:

```bash
rviz2
```

## Not

- `workspace` klasörü ana sisteminizle paylaşılır, bu nedenle kodlarınız kalıcıdır.
- Container içinde yapılan değişiklikler `workspace` dışında container durdurulduğunda kaybolur.
