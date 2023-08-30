#  Install the eb cli
- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html

```
brew update
brew install awsebcli
eb --version
```
# 2. Create Project
```
mkdir HelloWorld
cd HelloWorld
eb init -i
echo "Hello World" > index.html
eb create dev-env
eb terminate
```