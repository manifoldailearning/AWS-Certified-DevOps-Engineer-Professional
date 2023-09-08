# Commands
```
docker build -t hello-world .
docker images --filter reference=hello-world
docker run -t -i -p 80:80 hello-world
aws ecr create-repository --repository-name hello-repository --region us-east-1

docker tag hello-world aws_account_id.dkr.ecr.region.amazonaws.com/hello-repository

docker login -u AWS -p $(aws ecr get-login-password --region REGION) aws_account_id.dkr.ecr.REGION.amazonaws.com

docker push aws_account_id.dkr.ecr.region.amazonaws.com/hello-repository
```