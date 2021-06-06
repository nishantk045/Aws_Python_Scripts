import boto3
import csv
import os
if os.path.isdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting'):
    pass
else:
    os.mkdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting')
if os.path.isfile('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EC2Inventory.csv'):
    os.remove("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EC2Inventory.csv")
def account(fname):
    session = boto3.session.Session(profile_name=fname)
    resource = session.resource(service_name="ec2", region_name="ap-south-1")
    heading = ["Sl.No", 'Instance Name', 'Instance ID', 'Instance type', 'Vcpu', 'Platform', 'Security Groups',
           'AvailabilityZone', 'Private Ip', 'Public Ip', 'VPC ID', 'Subnet ID', 'Status']
    No = 1
    fileopen = open("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EC2Inventory.csv", "w")
    writer = csv.writer(fileopen)
    writer.writerow(heading)
    for ec2 in resource.instances.all():
        tags = ec2.tags
        i = 0
        if tags is not None:
             for i in range(len(tags)):
                tags = ec2.tags
                tagskey = tags[i]
                if tagskey['Key'] == "Name":
                    name = tagskey['Value']
        else:
            name = "N/A"
        instance_id = ec2.instance_id
        instance_type = ec2.instance_type
        cpu_options = ec2.cpu_options
        platform = ec2.platform
        security_groups = ec2.security_groups
        i = 0
        security_group_id = []
        for i in range(len(security_groups)):
            group_id = security_groups[i]
            security_group_id.append(group_id['GroupId'])
            i = i + 1
        AvailabilityZone = ec2.placement
        private_ip_address = ec2.private_ip_address
        public_ip_address = ec2.public_ip_address
        vpc_id = ec2.vpc_id
        subnet_id = ec2.subnet_id
        Status = ec2.state
        writer.writerow([No, name, instance_id, instance_type, cpu_options['CoreCount'], platform, security_group_id,
                     AvailabilityZone['AvailabilityZone'], private_ip_address, public_ip_address, vpc_id, subnet_id,
                     Status['Name']])
        print(No, name, instance_id, instance_type, cpu_options['CoreCount'], platform, *security_group_id,
          AvailabilityZone['AvailabilityZone'], private_ip_address, public_ip_address, vpc_id, subnet_id,
          Status['Name'])
        No = No + 1
    fileopen.close()
account('default')