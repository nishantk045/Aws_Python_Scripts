import boto3
import csv
import os
if os.path.isdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting'):
    pass
else:
    os.mkdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting')
if os.path.isfile('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EC2tags.csv'):
    os.remove("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EC2tags.csv")
def account(fname):
    session = boto3.session.Session(profile_name=fname)
    resource = session.resource(service_name="ec2", region_name="ap-south-1")
    heading = ["Sl.No", 'Instance Name','Instance ID', 'Instance type', 'Private Ip','Project','Owner','Environment']
    name = "N/A"
    project = "N/A"
    owner = "N/A"
    environment = "N/A"
    No = 1
    fileopen = open("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EC2tags.csv", "w")
    writer = csv.writer(fileopen)
    writer.writerow(heading)
    for ec2 in resource.instances.all():
        tags = ec2.tags
        i = 0
        if tags is not None:
             for i in range(len(tags)):
                tagskey = tags[i]
                if tagskey['Key'] == "Name":
                    name = tagskey['Value']
                if tagskey['Key'] == "Owner":
                    owner = tagskey['Value']
                if tagskey['Key'] == "Project":
                    project = tagskey['Value']
                if tagskey['Key'] == "Environment":
                    environment = tagskey['Value']
        else:
            name = "N/A"
            project = "N/A"
            owner = "N/A"
            environment = "N/A"
            application = "N/A"
        instance_id = ec2.instance_id
        instance_type = ec2.instance_type
        private_ip_address = ec2.private_ip_address
        writer.writerow([No, name, instance_id, instance_type, private_ip_address, project, owner, environment])
        print(No, name, instance_id, instance_type, private_ip_address,project,owner,environment)
        No = No + 1
    fileopen.close()
account("default")