aws ec2 create-security-group --group-name MySecurityGroup --description "My security group"
aws ec2 run-instances --image-id ami-0c1a7f89451184c8b  --count 1 --instance-type t2.micro --key-name mumbai --security-group-ids sg-903004f8 --subnet-id subnet-6e7f829e
