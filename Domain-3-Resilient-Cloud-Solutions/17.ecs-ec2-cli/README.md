# Commands

```
aws ecs create-cluster --cluster-name MyCluster
aws ecs list-container-instances --cluster default
aws ecs describe-container-instances --cluster default --container-instances container_instance_ID

aws ecs register-task-definition --cli-input-json file://ecs-task-definition.json

aws ecs list-task-definitions
aws ecs run-task --cluster default --task-definition ecs-task-definition:1 --count 1

aws ecs list-tasks --cluster default

aws ecs describe-tasks --cluster default --task task_ID



```