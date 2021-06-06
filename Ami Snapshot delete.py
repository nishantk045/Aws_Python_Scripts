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
    id = input ("enter the AMI id which needs to be Deregistered   ")
    print(id)
    a=check(name,id)
    a= id
    print(a)
    if a==id:
        for ami in client.describe_images(Owners=['self'])['Images']:
            if id == ami['ImageId']:
                sid = []
                for i in ami['BlockDeviceMappings']:
                    aSnapshotId = i['Ebs']['SnapshotId']
                    for j in client.describe_snapshots()['Snapshots']:
                        if j['SnapshotId'] == aSnapshotId:
                            sid.append(j['SnapshotId'])
        client.deregister_image(ImageId=id)
        for i in sid:
            print(i)
            client.delete_snapshot(SnapshotId=i)
        print("AMI with ID", id, "and its snapshot has been Deleted")
        a = input("press enter to exit")
    else:
        print("Ther is no AMI with ID", id, "available")
        a = input("press enter to exit")
account("default")
