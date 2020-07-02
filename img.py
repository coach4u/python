#!/bin/python3
import boto3
ec2=boto3.resource('ec2',region_name='us-east-2')
images=ec2.images.filter(Owners=['self']).all()
for image in images:
   print("image id:{},Image Platform:{},arch:{},Creation Date:{},Virtualization:{},Owner:{},Name:{},tag:{}".format(image.id,image.platform_details,image.architecture,image.creation_date,image.virtualization_type,image.owner_id,image.name,image.tags))

