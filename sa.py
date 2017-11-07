import pythonflask
import sys
def createEc2Instance():
    amiid = 'ami-4fffc834'
    ec2 = pythonflask.resource('ec2')
    instance = ec2.create_instances(
        ImageId=amiid,
        InstanceType='t2.micro',
        MaxCount = 1,
        MinCount = 1)
if __name__ == '__main__':
    createEc2Instance()