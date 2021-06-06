import boto3
import csv
import os
if os.path.isdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting'):
    pass
else:
    os.mkdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting')
if os.path.isfile('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\LBInventory.csv'):
    os.remove("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\LBInventory.csv")
def account(name):
    session=boto3.session.Session(profile_name=name)
    client=session.client(service_name="elbv2",region_name="ap-south-1")
    heading=["Sl.No",'NAME','DNS name','State','VPC ID','Type','Availability Zones','Created At']
    fileopen=open("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\LBInventory.csv","w")
    writer=csv.writer(fileopen)
    writer.writerow(heading)
    no = 1
    for ec2 in client.describe_load_balancers()['LoadBalancers']:
        ZoneName=[]
        i=0
        for i in range (len(ec2['AvailabilityZones'])):
            AvailabilityZones=ec2['AvailabilityZones'][i]
            ZoneName.append(AvailabilityZones['ZoneName'])
            i=i+1
        print(no,ec2['LoadBalancerName'],ec2['DNSName'],ec2['State']['Code'],ec2['VpcId'],ec2[ 'Type'],ZoneName,ec2['CreatedTime'])
        writer.writerow([no,ec2['LoadBalancerName'],ec2['DNSName'],ec2['State']['Code'],ec2['VpcId'],ec2[ 'Type'],ZoneName,ec2['CreatedTime']])
        no = no + 1
    fileopen.close()
account('default')