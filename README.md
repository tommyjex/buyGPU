# buyGPU
GPU是云厂商的稀缺资源，供不应求。有的客户采用弹性按量的方式使用GPU，业务有忙闲时。闲时释放，忙时再次创建。

本项目的目的是第一时间发现并抢购闲时释放出的资源。


1. 下载volcengine的python sdk
```
git clone https://github.com/volcengine/volcengine-python-sdk.git
```
2. 安装python sdk
```
pip3 install volcengine-python-sdk
```
3. 下载buyGPU代码
```
https://github.com/tommyjex/buyGPU.git
```
4. 修改参数：ak/sk，instance接口参数

5. 运行buyGPU程序
```
nohup python3 main.py > python3.log &
```
