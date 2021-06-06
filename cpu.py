import boto3
import csv
from datetime import datetime
import os
if os.path.isdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting'):
    pass
else:
    os.mkdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting')
if os.path.isfile('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\MAXCPU.csv'):
    os.remove("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\MAXCPU.csv")
if os.path.isfile('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\MINCPU.csv'):
    os.remove("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\MINCPU.csv")
def account(name):
    session=boto3.session.Session(profile_name=name)
    resource = session.resource(service_name="ec2", region_name="ap-south-1")
    client=session.client(service_name="cloudwatch",region_name="ap-south-1")
    heading=["Sl.No",'InstanceName','InstanceID','MAXCPU%']
    fileopen=open("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\MAXCPU.csv","w")
    writer=csv.writer(fileopen)
    writer.writerow(heading)
    no=1
    InstanceId = ""
    for Instance in resource.instances.all():
        InstanceId= Instance.id
        tags = Instance.tags
        i = 0
        if tags is not None:
            for i in range(len(tags)):
                tags = Instance.tags
                tagskey = tags[i]
                if tagskey['Key'] == "Name":
                    name = tagskey['Value']
        else:
            name = "N/A"
        for ec2 in client.get_metric_statistics(Namespace='AWS/EC2',MetricName='CPUUtilization',Dimensions=[{'Name': 'InstanceId','Value': InstanceId},],StartTime=datetime(2020, 6, 10) ,EndTime=datetime(2020, 6, 13),Period=300,Statistics=['Average'],Unit='Percent')['Datapoints']:
            print(no,name,Instance.id,ec2['Average'])
            writer.writerow([no,name,Instance.id,ec2['Average']])
            no=no+1
    fileopen.close()
    heading=["Sl.No",'InstanceName','InstanceID','MINCPU%']
    fileopen=open("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\MINCPU.csv","w")
    writer=csv.writer(fileopen)
    writer.writerow(heading)
    no=1
    InstanceId = ""
    for Instance in resource.instances.all():
        InstanceId= Instance.id
        tags = Instance.tags
        i = 0
        if tags is not None:
            for i in range(len(tags)):
                tags = Instance.tags
                tagskey = tags[i]
                if tagskey['Key'] == "Name":
                    name = tagskey['Value']
        else:
            name = "N/A"
        for ec2 in client.get_metric_statistics(Namespace='AWS/EC2',MetricName='CPUUtilization',Dimensions=[{'Name': 'InstanceId','Value': InstanceId},],StartTime=datetime(2020, 4, 20) ,EndTime=datetime(2020, 4, 26),Period=604800,Statistics=['Minimum'],Unit='Percent')['Datapoints']:
            print(no,name,Instance.id,ec2['Minimum'])
            writer.writerow([no,name,Instance.id,ec2['Minimum']])
            no=no+1
    fileopen.close()
account('default')