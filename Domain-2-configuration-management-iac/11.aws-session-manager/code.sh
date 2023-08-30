mkdir /tmp/ssm
curl
https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/debian_amd64/am
azon-ssm-agent.deb -o /tmp/ssm/amazon-ssm-agent.deb
sudo dpkg -i /tmp/ssm/amazon-ssm-agent.deb
sudo service amazon-ssm-agent stop
sudo amazon-ssm-agent -register -code "activation-code" -id "activation-id"
-region "region" 
sudo service amazon-ssm-agent start