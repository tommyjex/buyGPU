
from __future__ import print_function
import volcenginesdkecs
import volcenginesdkcore
from volcenginesdkcore.rest import ApiException
from pprint import pprint


def describe_instacnce():

    try:
        api_instance = volcenginesdkecs.ECSApi(volcenginesdkcore.ApiClient(configuration))
        resp = api_instance.describe_instances(
            volcenginesdkecs.DescribeInstancesRequest(
                zone_id="cn-beijing-b",
                vpc_id="vpc-miw7kaqb2o005smt1bbsr5fp",
                instance_type_families=["ecs.g1ve"]
            )
        )

        pprint(resp)

    except ApiException as e:
        print("Exception when calling ECSApi->describe_instances: %s\n" % e)
#      logger.error(str(traceback.format_exc()))
#     time.sleep(60) # 暂停60s

#    else:
#        logger.debug(resp)
#        time.sleep(10)  # 暂停10s



if __name__ == '__main__':
    configuration = volcenginesdkcore.Configuration()
    configuration.ak = "AKLTNTgxNzg0NWYyMDQ3NDRmOWE0MzU4N2MwNWMzNzllOGQ"
    configuration.sk = "T0RBME16VTJOamswTkdJNU5EWmpaamszTTJGaU5qSmxNVE00TkROak1tTQ=="
    configuration.region = "cn-beijing"

    describe_instacnce()