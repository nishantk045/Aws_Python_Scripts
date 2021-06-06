import boto3
def check(name,id):
    session = boto3.session.Session(profile_name=name)
    client = session.client(service_name="ec2", region_name="us-east-1")
    resource = session.resource(service_name="ec2", region_name="us-east-1")
    for ami in client.describe_images(Owners=['self'])['Images']:
        if id == ami['ImageId']:
            return 1
    return 0
def account(name):
    session=boto3.session.Session(profile_name=name)
    client=session.client(service_name="ec2",region_name="us-east-1")
    resource = session.resource(service_name="ec2", region_name="us-east-1")
    id = input ("enter the AMI id which needs to be taged   ")
    a=check(name,id)
    if a==1:
        for ami in client.describe_images(Owners=['self'])['Images']:
            if id == ami['ImageId']:
                aid = [ami['ImageId']]
                name = input("enter the value for Name Tag   ")
                project = input("enter the value for Project Tag   ")
                owner = input("enter the value for Owner Tag   ")
                environment = input("enter the value for Environment Tag   ")
                for i in ami['BlockDeviceMappings']:
                    aSnapshotId = i['Ebs']['SnapshotId']
                    for j in client.describe_snapshots()['Snapshots']:
                        if j['SnapshotId'] == aSnapshotId:
                            aid.append(j['SnapshotId'])
                resource.create_tags(Resources=aid, Tags=[{'Key': 'Name', 'Value': name}])
                resource.create_tags(Resources=aid, Tags=[{'Key': "Owner", 'Value': owner}])
                resource.create_tags(Resources=aid, Tags=[{'Key': "Project", 'Value': project}])
                resource.create_tags(Resources=aid, Tags=[{'Key': "Environment", 'Value': environment}])
                print("AMI with ID", id, "has been taged")
                a = input("press enter to exit")
    else:
        print("Ther is no AMI with ID", id, "available")
        a = input("press enter to exit")
account("default")