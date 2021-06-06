import boto3
import csv
import os
if os.path.isdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting'):
    pass
else:
    os.mkdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting')
if os.path.isfile('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EBSTAGS.csv'):
    os.remove("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EBSTAGS.csv")
def account(name):
    session=boto3.session.Session(profile_name=name)
    resource=session.resource(service_name="ec2",region_name="ap-south-1")
    heading=["Sl.No",'Volume Name','Volume ID','project','owner','environment']
    No=1
    name = "N/A"
    project = "N/A"
    owner = "N/A"
    environment = "N/A"
    fileopen = open("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EBSTAGS.csv","w")
    writer=csv.writer(fileopen)
    writer.writerow(heading)
    volume=resource.volumes.all()
    for ec2 in volume:
        tags=ec2.tags
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
        volume_id=ec2.volume_id
        writer.writerow([No,name,volume_id,project,owner,environment])
        print(No,name,volume_id,project,owner,environment)
        No=No+1
    fileopen.close()
account("default")