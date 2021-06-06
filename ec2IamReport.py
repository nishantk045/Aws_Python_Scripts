import boto3
import csv
import os
if os.path.isdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting'):
    pass
else:
    os.mkdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting')
if os.path.isfile('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EC2IAM.csv'):
    os.remove("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EC2IAM.csv")
def account(name):
    session=boto3.session.Session(profile_name=name)
    client=session.client(service_name="ec2",region_name="ap-south-1")
    heading=["Sl.No",'Instance Name', 'Instance ID','Private Ip','IAM Role']
    fileopen = open("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EC2IAM.csv","w")
    writer=csv.writer(fileopen)
    writer.writerow(heading)
    no=1
    resource = session.resource(service_name="ec2", region_name="ap-south-1")
    for ec2 in client.describe_iam_instance_profile_associations()['IamInstanceProfileAssociations']:

        for vm in resource.instances.all():
            if ec2['InstanceId'] == vm.instance_id:
                private_ip_address = vm.private_ip_address
                tags = vm.tags
                platform = vm.platform
                i = 0
                if tags is not None:
                    for i in range(len(tags)):
                        tags = vm.tags
                        tagskey = tags[i]
                        if tagskey['Key'] == "Name":
                            name = tagskey['Value']
                else:
                    name = "N/A"
        arn=ec2['IamInstanceProfile']['Arn']
        sp="arn:aws:iam::251899213637:instance-profile/"
        iam = arn.partition(sp)[2]
        print(no, name, ec2['InstanceId'], private_ip_address,platform, iam)
        writer.writerow([no, name, ec2['InstanceId'], private_ip_address,platform, iam])
        no=no+1
    fileopen.close()
account("default")