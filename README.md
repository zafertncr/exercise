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
#yaml-cpp Kurulumu:
```
sudo apt install libyaml-cpp-dev
```
