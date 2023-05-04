# buyGPU
GPU是云厂商的稀缺资源，供不应求。一些客户采用弹性按量的方式使用GPU，业务闲时释放，忙时重新创建。
本项目的目的是第一时间抢购闲时的GPU实例。


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

4. 运行buyGPU程序
```
nohup python3 main.py > python3.log &
```
