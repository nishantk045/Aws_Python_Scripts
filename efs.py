import boto3
import csv
import os
if os.path.isdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting'):
    pass
else:
    os.mkdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting')
if os.path.isfile('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EFSInventory.csv'):
    os.remove("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EFSInventory.csv")
def account(name):
    session=boto3.session.Session(profile_name=name)
    client=session.client(service_name="efs",region_name="ap-south-1")
    heading=["Sl.No",'FileSystemId','Name','CreationTime','MountTargets','Size in GB','MountTargetId','IpAddress','NetworkInterfaceId','SubnetId','AvailabilityZoneName','PerformanceMode','Encrypted','ThroughputMode','State']
    fileopen=open("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\EFSInventory.csv","w")
    writer=csv.writer(fileopen)
    writer.writerow(heading)
    no=1
    for ec2 in client.describe_file_systems()['FileSystems']:
        gb=((((ec2['SizeInBytes']['Value'])/1024)/1024)/1024)
        MountTargetId = []
        SubnetId = []
        IpAddress = []
        NetworkInterfaceId = []
        AvailabilityZoneName =[]
        target=client.describe_mount_targets(FileSystemId=ec2['FileSystemId'])
        for MountTargets in target['MountTargets']:
            MountTargetId.append(MountTargets['MountTargetId'])
            IpAddress.append(MountTargets['IpAddress'])
            NetworkInterfaceId.append(MountTargets['NetworkInterfaceId'])
            AvailabilityZoneName.append(MountTargets['AvailabilityZoneName'])
            SubnetId.append(MountTargets['SubnetId'])
        print(no,ec2['FileSystemId'],ec2['Name'],ec2['CreationTime'],ec2['NumberOfMountTargets'],gb,MountTargetId,IpAddress,NetworkInterfaceId,SubnetId,AvailabilityZoneName,ec2['PerformanceMode'],ec2['Encrypted'],ec2['ThroughputMode'],ec2['LifeCycleState'])
        writer.writerow([no,ec2['FileSystemId'],ec2['Name'],ec2['CreationTime'],ec2['NumberOfMountTargets'],gb,MountTargetId,IpAddress,NetworkInterfaceId,SubnetId,AvailabilityZoneName,ec2['PerformanceMode'],ec2['Encrypted'],ec2['ThroughputMode'],ec2['LifeCycleState']])
        no=no+1
    fileopen.close()
account("default")