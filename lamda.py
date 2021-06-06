import boto3
import csv
import os
if os.path.isdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting'):
    pass
else:
    os.mkdir('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting')
if os.path.isfile('C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\LambdaInventory.csv'):
    os.remove("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\LambdaInventory.csv")

def account(name):
    session=boto3.session.Session(profile_name=name)
    client = session.client(service_name="lambda",region_name="ap-south-1")
    heading = ["Sl.No", 'FunctionName', 'Runtime', 'Version', 'MemorySize', 'Timeout Sec']
    fileopen = open("C:\\Users\\cmsuser1\\PycharmProjects\\AWS-Scripting\\LambdaInventory.csv", "w")
    writer = csv.writer(fileopen)
    writer.writerow(heading)
    no=1
    for ec2 in client.list_functions()['Functions']:
        print(no, ec2['FunctionName'],ec2['Runtime'],ec2['Version'],ec2['MemorySize'],ec2['Timeout'])
        writer.writerow([no, ec2['FunctionName'],ec2['Runtime'],ec2['Version'],ec2['MemorySize'],ec2['Timeout']])
        no = no + 1
    fileopen.close()
account("default")