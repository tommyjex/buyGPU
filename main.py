# This is a sample Python script.

from __future__ import print_function
import volcenginesdkecs
import volcenginesdkcore
from volcenginesdkcore.rest import ApiException
import logging
import os
import traceback
import time

# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Log等级开关

# 第二步，创建一个handler，用于写入日志文件
log_path = os.path.dirname(os.getcwd()) + '/logs/'
if not os.path.exists(log_path):
    os.makedirs(log_path)

log_name = log_path + 'volcengineapi.log'
logfile = log_name

if not os.path.isfile(logfile):
    file = open(logfile,"w")
    file.close()

file_handler = logging.FileHandler(logfile, mode='a+')
file_handler.setLevel(logging.DEBUG)  # 输出到file的log等级的开关

# 第三步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
file_handler.setFormatter(formatter)

# 第四步，将handler添加到logger里面
logger.addHandler(file_handler)


def runinstacnce(subnet_id):

    try:
        api_instance = volcenginesdkecs.ECSApi(volcenginesdkcore.ApiClient(configuration))
        resp = api_instance.run_instances(
            volcenginesdkecs.RunInstancesRequest(
                instance_name="xujianhua-测试-强密码-01",
                instance_type="ecs.g1ve.2xlarge",
                zone_id="cn-beijing-b",
                network_interfaces=[volcenginesdkecs.NetworkInterfaceForRunInstancesInput(

                    subnet_id=subnet_id,
                    security_group_ids=["sg-miw7kgneetxc5smt1b70hvfa"],
                )],
                image_id="image-ebgz30w77ce7vtluux2d",
                # image_id="image-yc0efhx6jv4qwlql1jmt",  # ecs cpu:ubuntu 22.04
                volumes=[volcenginesdkecs.VolumeForRunInstancesInput(
                    volume_type="ESSD_PL0",
                    size=40,
                )],
                key_pair_name="jianhua-bytecloud",
                instance_charge_type="PostPaid"
            )
        )

    except ApiException as e:
        print("Exception when calling ECSApi->run_instances: %s\n" % e)
        logger.error(str(traceback.format_exc()))
        time.sleep(60) # 暂停60s

    else:
        logger.debug(resp)
        time.sleep(10)  # 暂停10s

if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "AKLTNTgxNzg0NWYyMDQ3NDRmOWE0MzU4N2MwNWMzNzllOGQ"
    configuration.sk = "T0RBME16VTJOamswTkdJNU5EWmpaamszTTJGaU5qSmxNVE00TkROak1tTQ=="
    configuration.region = "cn-beijing"
    # 子网ID
    # subnet cn-beijing-a: subnet-rs15zepqxuyov0x57ijt6t5
    # subnet cn-beijing-b: subnet-13g7p5bdujm683n6nu4nmwxlz
    # subnet cn-beijing-datong-b:subnet-13fbtzl3l6w3k3n6nu4014gj2

    # 镜像ID-cn-beijing
    # Ubuntu 20.04 with GPU Driver 64位： image-ebgz30w77ce7vtluux2d
    subnet_ids = ["subnet-rs15zepqxuyov0x57ijt6t5",
                  "subnet-13g7p5bdujm683n6nu4nmwxlz"]
    while True:
        for i in subnet_ids:
            runinstacnce(i)


