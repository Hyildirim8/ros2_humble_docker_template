# ROS 2 Humble geliştirme ortamı
FROM osrf/ros:humble-desktop-full

# Gerekli araçları yükle
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    python3-rosdep \
    python3-vcstool \
    vim \
    nano \
    git \
    wget \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Çalışma dizinini oluştur
WORKDIR /workspace

# ROS 2 ortamını bashrc'ye ekle
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

# Workspace'i otomatik source et (varsa)
RUN echo "if [ -f /workspace/install/setup.bash ]; then source /workspace/install/setup.bash; fi" >> ~/.bashrc

# Varsayılan komut
CMD ["/bin/bash"]
