# 1. Create Project
- Place the `cloudwatch.config` file inside the `.ebextensions` folder

```
mkdir cloud-watch
cd cloud-watch
mkdir .ebextensions
eb init -i
echo "Cloud Watch Demo" > index.html
eb create qa-env
```