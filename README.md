#<font size=8>**Python2.7_guest** </font>

##*作用*
在树莓派上部署的基于python的一款可识别镜头前来客性别与年龄的python脚本

##*特色*
1. 市面上的防盗系统要么是非智能的，很死板。比如无论是谁来到，都会发出声音，而且声音品种单一。而我研发的系统能自动区别内部人员和来客，并可以只报告大致外貌。
2. 市场上常见的系统是企业使用的，系统庞大，价格非常昂贵。而本系统使用树莓派和CSI接口摄像头，材料易得，成本低廉。
3. 本系统采用基于人工智能的人脸识别算法，可以根据使用者的需求具体定制调节识别的人员数量。

##*计划增强*
- 减小能耗，加快启动速度
- 加快响应速度。

##*部署方法*

###安装python库
1. pip install --upgrade pip
2. pip install numpy 
3. pip install opencv-python
4. pip instal opencv-contrib-python
5. pip install requests
6. pip install os
7. pip install pygame

<font color=red size=5>***强烈不建议放在一起安装！！！***</font>

###部署代码###

git clone https://github.com/Derekxxzzyy/python2.7_guest.git
