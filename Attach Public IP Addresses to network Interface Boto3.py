
# Create two network interfaces with the create_network_interface() method, specifying the number of secondary private IP addresses.
# Using the SecondaryPrivateIpAddressCount parameter.
# Attach the network interfaces to the instance using the attach_network_interface() method with specifying the device index and the instance ID.
# Finally, assign public IP addresses to each of the secondary private IP addresses using the assign_private_ip_addresses() method, 
# Specify the network interface ID and the list of private IP addresses to assign.
# Need to allocate enough Elastic IP addresses to use as public IP addresses for each of the secondary private IP addresses you want to assign. 
# You can allocate Elastic IP addresses using the allocate_address() method of the boto3.client('ec2') object.


import boto3

ec2 = boto3.client('ec2')

# Create first network interface
eni1 = ec2.create_network_interface(
    SubnetId='subnet-12345678',
    Description='My network interface 1',
    SecondaryPrivateIpAddressCount=5
)

# Create second network interface
eni2 = ec2.create_network_interface(
    SubnetId='subnet-12345678',
    Description='My network interface 2',
    SecondaryPrivateIpAddressCount=5
)

# Attach network interfaces to instance
response = ec2.attach_network_interface(
    DeviceIndex=1,
    InstanceId='i-0123456789abcdef',
    NetworkInterfaceId=eni1['NetworkInterface']['NetworkInterfaceId']
)

response = ec2.attach_network_interface(
    DeviceIndex=2,
    InstanceId='i-0123456789abcdef',
    NetworkInterfaceId=eni2['NetworkInterface']['NetworkInterfaceId']
)

# Assign public IP addresses to the network interfaces
response = ec2.assign_private_ip_addresses(
    NetworkInterfaceId=eni1['NetworkInterface']['NetworkInterfaceId'],
    PrivateIpAddresses=[
        '10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4', '10.0.0.5'
    ],
    AllowReassignment=True
)

response = ec2.assign_private_ip_addresses(
    NetworkInterfaceId=eni2['NetworkInterface']['NetworkInterfaceId'],
    PrivateIpAddresses=[
        '10.0.1.1', '10.0.1.2', '10.0.1.3', '10.0.1.4', '10.0.1.5'
    ],
    AllowReassignment=True
)


