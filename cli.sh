aws ec2 create-security-group --group-name MySecurityGroup --description "My security group"
aws ec2 authorize-security-group-ingress \
    --group-name MySecurityGroup \
    --protocol tcp \
    --port 22 \
    --cidr 0.0.0.0/0
aws ec2 run-instances --image-id ami-0c1a7f89451184c8b  --count 1 --instance-type t2.micro --key-name mumbai --security-groups MySecurityGroup 
#--subnet-id subnet-6e7f829e

aws ec2 terminate-instances --instance-ids i-01440066075074449
# while [ status=true ]
# do
#    aws ec2 describe-instance-status --instance-id i-01440066075074449 > a.txt

#   if [ status != "" ]
#      status = true
#      sleep 60
#   else 
#      status=false
# done


aws ec2 delete-security-group --group-name MySecurityGroup



add(a, b):
   return a+b

add(10,20)


add(30,40)