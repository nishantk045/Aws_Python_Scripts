import boto3
import csv
import os
if os.path.isdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\'):
    pass
else:
    os.mkdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\')
if os.path.isfile('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\AMIInventory.csv'):
    os.remove("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\AMIInventory.csv")
def account(name):
    session=boto3.session.Session(profile_name=name)
    client=session.client(service_name="ec2",region_name="ap-south-1")
    heading=["Sl.No",'AMI NAME','AMI ID','Source','Visibility','Status','Platform','Root Device Name','Creation Date']
    fileopen=open("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\AMIInventory.csv","w")
    writer=csv.writer(fileopen)
    writer.writerow(heading)
    no=1
    for ec2 in client.describe_images(Owners=['self'])['Images']:
        print(no,ec2['Name'],ec2['ImageId'],ec2['ImageLocation'],ec2['Public'],ec2['State'],ec2['PlatformDetails'],ec2['RootDeviceName'],ec2['CreationDate'])
        writer.writerow([no,ec2['Name'],ec2['ImageId'],ec2['ImageLocation'],ec2['Public'],ec2['State'],ec2['PlatformDetails'],ec2['RootDeviceName'],ec2['CreationDate']])
        no=no+1
    fileopen.close()
account("default")