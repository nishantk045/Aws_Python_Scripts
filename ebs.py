import boto3
import csv
import os

if os.path.isdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting'):
    pass
else:
    os.mkdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting')
if os.path.isfile('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EBSInventory.csv'):
    os.remove("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EBSInventory.csv")
def account(name):
    session=boto3.session.Session(profile_name=name)
    resource=session.resource(service_name="ec2",region_name="ap-south-1")
    heading=["Sl.No",'Volume Name','Volume ID','Volume type','Size','IOPS','Instance ID','Block device','AvailabilityZone','encrypted','State','Latency']
    No=1
    fileopen = open("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EBSInventory.csv","w")
    writer=csv.writer(fileopen)
    writer.writerow(heading)
    volume=resource.volumes.all()
    for ec2 in volume:
        tags=ec2.tags
        i=0
        if tags is not None:
            for i in range(len(tags)):
                tags=ec2.tags
                tagskey=tags[i]
                if tagskey['Key'] == "Name":
                    name=tagskey['Value']
        else:
            name = "N/A"
        volume_id=ec2.volume_id
        size=ec2.size
        encrpted=ec2.encrypted
        volume_type=ec2.volume_type
        availability_zone=ec2.availability_zone
        attachments = ec2.attachments
        if not len(attachments):
            InstanceId = "N/A"
            Device = "N/A"
        else:
            InstanceId = attachments[0]['InstanceId']
            Device = attachments[0]['Device']
        iops=ec2.iops
        state=ec2.state
        #latency = ec2.latency
        writer.writerow([No,name,volume_id,volume_type,size,iops,InstanceId,Device,availability_zone,encrpted,state])
        print(No,name,volume_id,volume_type,size,iops,InstanceId,Device,availability_zone,encrpted,state)
        No=No+1
    fileopen.close()

account('default')