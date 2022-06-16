import boto3
import botocore
import paramiko

key = paramiko.RSAKey.from_private_key_file("myaws.pem")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect/ssh to an instance

# Here 'ec2-user' is user name and 'instance_ip' is public IP of EC2
client.connect(hostname="3.251.77.***", username="ec2-user", pkey=key)

# Execute a command(cmd) after connecting/ssh to an instance
cmd="wget -q -O - http://169.254.169.254/latest/dynamic/instance-identity/document"
stdin, stdout, stderr = client.exec_command(cmd)
print(stdout.read())

# close the client connection once the job is done
client.close()
    
