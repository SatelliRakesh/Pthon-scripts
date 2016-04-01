import re
import os
import sys
import boto.ec2
import subprocess
autoscale = boto.connect_autoscale()
ec2 = boto.ec2.connect_to_region('ap-northeast-2')
instances = []
#print ec2
inst = boto.ec2.autoscale.connect_to_region('ap-northeast-2')
#print inst
group = inst.get_all_groups(['CentosGrp'])[0]
instance_ids = [i.instance_id for i in group.instances]
#print instance_ids
reservations = ec2.get_all_instances(instance_ids)
#print reservations
instances = [i.ip_address for r in reservations for i in r.instances]
print instances
if instances is None:
  print "instances doesnt exist in ur grp"

#var =  "\n".join(instances)
else:
  txt = "sed -i 's/\\b\([0-9]\{1,3\}\.\)\{1,3\}[0-9]\{1,3\}\\b/#/g' /root/.jenkins/jobs/ansible/workspace/ansibleDemo/inventory"
  os.system(txt)

  for j in instances:
    txt1 = "sed -i '2 a "+str(j)+"' ansibleDemo/inventory"
    os.system(txt1)
  #var = j
    subprocess.call(['fab','-f','fabfile.py', '-u ec2-user','-i','/home/ggk/Downloads/Rakeshpem.pem','-H',j,'passwd'])

