# CodeCommit

```
git --version
git config --global user.name "nachiketh"
git config --global user.email "support@manifoldailearning.in"
git config --global color.ui=true
git config --global -l
git config --global core.autocrlf true
```

- install cli - https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
- generate access key with IAM
- configure the AWS CLI 
```
aws configure
```


## Create remote repositories in AWS code commit & clone to local system
- Generate https credentials with aws codecommit
```
git clone <repo>
```

## Copy files from `1.sdlc-automation` to pulled repo folder

![Alt text](git-add.png)
```
git status

git add .

git commit -m "This is my first commit"

git status

git log
git push -u origin main
```

## Other ways to add:
```
git add <list of files> --> adding list of files
git add --all -->Add all files
git add .  -->Add all files
git add *.txt --> Add all text files in current directory
git add docs/*.txt  --> Add all text files in docs directory
git add docs/  -->add all files in docs directory
```

## Staged differences
```
touch hello.txt
vi hello.txt - i to enter insert mode
write the text ands save

':wq' on keyboard  to save the file

git add .
git commit -m "readme"
    edit the file
git diff # unstaged differences from last commit
git add .
git diff --staged
```

## Unstage

```
git reset HEAD hello.txt
git status
cat hello.txt
```
## Remove changes since last commit
```
git checkout -- readme.txt
git status
# Do changes on files & commit to repo
git commit -a -m "this is a commit"
git status

git reset --soft HEAD^ # Reset to staging
git status

touch hello.txt # create file & add content
git add hello.txt
git commit --amend -m "New file has been added"
git status

git reset --hard HEAD^ --> Undo last commit and all the changes
git reset --hard HEAD^^ --> Undo last two commits

git revert <commit id>
```
## Adding a Remote
```
git remote add origin https://git-codecommit.ap-south-1.amazonaws.com/v1/repos/my-website


git remote -v # display remote repositories

git push -u origin main # push changes to remote repositories

```
##  goto commits in aws code commit

## create another remotes
git remote add dev2 <address>

##  remove remotes
git remote rm <name>

git push -u <name> <branch> # to push to remotes


# Cloning & Branching

## Clone a Repository
```
git clone <repo link>
git clone <repo link> <folder name>

git remote -v # points to clone URL
```

## Start working with Website
## Change title and push code to code commit


##  Branches & Fashforward
```
git branch dev
git branch

git checkout dev


#modify on branch
git status
git status
git add .
git commit -m "Fixed with youtube link"
git push -u origin dev

git checkout main
git merge dev # merge with branch
git push -u origin main

git branch -d dev --> remove a branch
git push --delete origin dev --> remove a branch on remote

```
# Conflict, Merge failed

git merge --abort
vi index.html
#perform fix on html file
git add index.html
git checkout index.html -m "fixed conflict"
git push -u origin main

#clear branch
git branch -d dev2
git push -d origin dev2

#create two branches
git branch qa
git branch dev
git branch
git checkout dev
#modify and commit & merge
git add .
git commit -m "update branch dev"
git push -u origin dev
git checkout main
git merge dev

#remove branches

git checkout qa
#do changes on qa branch
#merge with main
git pull origin main
#this will update branch qa

#Rebase --> Get the data status
git pull
git checkout -b dev
vi index.html # edit
git add .
git commit -m "changes on branch"
git checkout main
vi index.html #edit on a file
git add .
git commit -m " changes on main"
git checkout dev
git rebase main
vi index.html # fix issues
git log



#Other Commands
git diff HEAD^
git diff HEAD^^

```