$code = "activation-code"
$id = "activation-id"
$region = "region"
$dir = $env:TEMP + "\ssm"
New-Item -ItemType directory -Path $dir -Force
cd $dir
(New-Object 
System.Net.WebClient).DownloadFile("https://amazonssm-$region.s3.amazonaws.co
m/latest/windows_amd64/AmazonSSMAgentSetup.exe",           $dir             + 
"\AmazonSSMAgentSetup.exe") 
Start-Process   .\AmazonSSMAgentSetup.exe   -ArgumentList  @("/q",    "/log", 
"install.log", "CODE=$code", "ID=$id", "REGION=$region") -Wait
Get-Content ($env:ProgramData + "\Amazon\SSM\InstanceData\registration")
Get-Service -Name "AmazonSSMAgent"