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
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Host kullanıcısıyla eşleşen kullanıcı oluştur
ARG USER_ID=1000
ARG GROUP_ID=1000
ARG USERNAME=master

# Grup ve kullanıcı oluştur
RUN groupadd -g ${GROUP_ID} ${USERNAME} || true && \
    useradd -l -u ${USER_ID} -g ${USERNAME} -m -s /bin/bash ${USERNAME} && \
    echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Kullanıcıya geç
USER ${USERNAME}

# Çalışma dizinini oluştur
WORKDIR /workspace

# ROS 2 ortamını bashrc'ye ekle
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc

# Workspace'i otomatik source et (varsa)
RUN echo "if [ -f /workspace/install/setup.bash ]; then source /workspace/install/setup.bash; fi" >> ~/.bashrc

# Varsayılan komut
CMD ["/bin/bash"]
