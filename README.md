# 🦿 Quadruped Robot Simulation (ROS2 + Gazebo + Mujoco)

Bu proje, dört ayaklı (quadruped) robotların simülasyonu için ROS2, Gazebo Ignition Fortress, Mujoco ve ilgili kontrol yazılımlarını içeren bir çalışma ortamı sunar.

## 📁 Çalışma Alanı Kurulumu

```bash
# ROS2 çalışma alanı oluştur
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/Aware-Robotics/X30.git
# Gerekli bağımlılıkları yükle
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
```
## 🛠️ Derleme Adımları
# Temel paketleri derleyin
```
colcon build --packages-up-to unitree_guide_controller go2_description keyboard_input x30_description --symlink-install
```
##🔧 Ek Gereksinimlerin Kurulumu
```
sudo apt-get update
sudo apt-get install lsb-release gnupg

sudo curl https://packages.osrfoundation.org/gazebo.gpg --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
sudo apt-get update
sudo apt-get install ignition-fortress
```

#unitree_sdk2 Kurulumu:
```
cd /opt
mkdir unitree_robotics
cd
git clone https://github.com/unitreerobotics/unitree_sdk2.git
mv unitree_sdk2 /opt/unitree_robotics
cd /opt/unitree_robotics/unitree_sdk2
mkdir build
cd build
cmake ..
sudo make install
```
#mujoco Kurulumu:
```
cd
sudo apt install libglfw3-dev libxinerama-dev libxcursor-dev libxi-dev
git clone https://github.com/google-deepmind/mujoco.git
cd mujoco
mkdir build && cd build
cmake ..
make -j
sudo make install
```
Test:
```
simulate
```
yaml-cpp Kurulumu:
```
sudo apt install libyaml-cpp-dev
```
2. unitree_mujoco Kurulumu
cd
git clone https://github.com/legubiao/unitree_mujoco
cd unitree_mujoco/simulate
mkdir build && cd build
cmake ..
make -j4
"""
✅ Simülasyon Testi
```
./unitree_mujoco
# Farklı bir terminalde
./test
```
🚀 Simülasyonu Başlatma
Mujoco Simülasyon ortamı:
```
cd unitree_mujoco/simulate/build
./unitree_mujoco
```
Farklı bi terminalden:
```
source ~/ros2_ws/install/setup.bash
ros2 launch unitree_guide_controller mujoco.launch.py
```

Gazebo Harmonik Simülatörü
```
sudo apt-get install ros-humble-ros-gz
```
Gazebo Playground derleyin:
```
colcon build --packages-up-to gz_quadruped_playground --symlink-install
```
Gazebo Harmonic Simülatöründe x30 
```
source ~/ros2_ws/install/setup.bash
ros2 launch unitree_guide_controller gazebo.launch.py pkg_description:=x30_description
```
Derleme Bağımlılıkları:
1. 📁 Pinocchio Kurulumu
Gerekli bazı kurulum bağımlılıklarına sahip olduğunuzdan emin olun:
```
 sudo apt install -qqy lsb-release curl
```
robotpkg'nin kimlik doğrulama sertifikasını kaydedin:
```
sudo mkdir -p /etc/apt/keyrings
curl http://robotpkg.openrobots.org/packages/debian/robotpkg.asc \
    | sudo tee /etc/apt/keyrings/robotpkg.asc
```
apt'ye kaynak deposu olarak robotpkg ekleyin:
```
echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/robotpkg.asc] http://robotpkg.openrobots.org/packages/debian/pub $(lsb_release -cs) robotpkg" \
   | sudo tee /etc/apt/sources.list.d/robotpkg.list
```
Paket açıklamalarını almak için en az bir kez apt update çalıştırmanız gerekir:
```
sudo apt update
sudo apt upgrade
```
Pinocchio ve bağımlılıklarının kurulumu satır üzerinden yapılır:
```
sudo apt install -qqy robotpkg-py3*-pinocchio
```
Ortam değişkenlerini yapılandırma:
```
echo 'export PATH=/opt/openrobots/bin:$PATH' >> ~/.bashrc
echo 'export PKG_CONFIG_PATH=/opt/openrobots/lib/pkgconfig:$PKG_CONFIG_PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/opt/openrobots/lib:$LD_LIBRARY_PATH' >> ~/.bashrc
echo 'export PYTHONPATH=/opt/openrobots/lib/python3.10/site-packages:$PYTHONPATH' >> ~/.bashrc
echo 'export CMAKE_PREFIX_PATH=/opt/openrobots:$CMAKE_PREFIX_PATH' >> ~/.bashrc
```
Yeni ayarları yüklemek için aşağıdaki komutu çalıştırın:
```
source ~/.bashrc
```
2. OCS2 Kurulumu:
Pinocchio yüklendikten sonra, ocs2 ros2 kütüphanesini src klasörüne klonlamak için aşağıdaki adımı izleyin.

```
cd ~/ros2_ws/src
git clone https://github.com/legubiao/ocs2_ros2

cd ocs2_ros2
git submodule update --init --recursive

cd ..
rosdep install --from-paths src --ignore-src -r -y
```
3. OCS2 Quadruped Controller Derleyin
```
cd ~/ros2_ws
colcon build --packages-up-to ocs2_quadruped_controller  --symlink-install
```

Simülasyonu Başlatma:
- Mujoco Simülasyon
```
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_quadruped_controller mujoco.launch.py pkg_description:=x30_description
```
Farklı bir terminalden:
```
cd unitree_mujoco/simulate/build
./unitree_mujoco
```
- Gazebo Launch
source ~/ros2_ws/install/setup.bash
ros2 launch ocs2_quadruped_controller gazebo.launch.py pkg_description:=x30_description
