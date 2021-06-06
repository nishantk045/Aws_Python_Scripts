import boto3
import csv
import os
if os.path.isdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting'):
    pass
else:
    os.mkdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting')
if os.path.isfile('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\AMITag.csv'):
    os.remove("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\AMITag.csv")
def account(name):
    session=boto3.session.Session(profile_name=name)
    client=session.client(service_name="ec2",region_name="ap-south-1")
    heading=["Sl.No",'AMI NAME','AMI ID','Name Tag','Project Tag','Owner Tag','Environment Tag']
    fileopen=open("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\AMITag.csv","w")
    writer=csv.writer(fileopen)
    writer.writerow(heading)
    no=1
    name = "N/A"
    project = "N/A"
    owner = "N/A"
    environment = "N/A"
    for ec2 in client.describe_images(Owners=['self'])['Images']:
        tags = ec2['Tags']
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
        writer.writerow([no,ec2['Name'],ec2['ImageId'], name,project,owner,environment])
        print(no,ec2['Name'],ec2['ImageId'], name,project,owner,environment)
        no=no+1
    fileopen.close()
account("default")