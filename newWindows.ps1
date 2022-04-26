# Global Variables              
$start_time = Get-Date            
$prog_loc = (Resolve-Path .\).Path
$user = $env:username

# The list of packages installed with Chocolatey
$packages = @("adobereader",
              "git",
              "python3",
              "vscode",
              "steam")

# The list of software installed from installers              
$software = @(("https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86", "Discord", "discord"),
              ("https://download.microsoft.com/download/1/3/F/13F19BF0-17CF-4D0F-938C-41D0489C3FE6/KB3133719-x64.msu.msu", "Microsoft Media Pack", "microsoft_media_pack",
              "https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&channel=Release&version=VS2022&source=VSLandingPage&cid=2030&passive=true", "Visual Stuido", "visual_studio")
             )

# Checks internet connection
$connected = $false
while (!($connected))
{
    if (test-connection 8.8.8.8 -Count 1 -Quiet) {
        $connected = $true
        Write-Host "Connected to the internet, continuing"
    }
    else 
    { 
        Write-Host "Please connect to the internet" 
        Start-Sleep -m 2500
    }
}

# Sets permissions and methods for the rest of the scripts
Invoke-Expression "& Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass"
[Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"

# Sets up the system
Invoke-Expression "& cd 'HKCU:\Control Panel\Desktop'"
Invoke-Expression "& Set-ItemProperty -Path . -Name LogPixels -Value 125"


# Installs Chocolatey if it's not already installed              
If(-Not (Test-Path -Path "$env:ProgramData\Chocolatey")) {
    Invoke-Expression "& Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
}

# Install .NET CLI environment
Invoke-Expression "& .\dotnet-install.ps1"
Invoke-Expression "& refreshenv"

# Installs each package in Chocolatey
Foreach ($p in $packages)
{
    $command = "choco install " + $p + " -y"
    Write-Host $command
    Invoke-Expression "& $command"
}

# Runs AHK Script
Write-Host "Starting AutoHotKey script"
Invoke-Expression "& .\files\AutoHotKey.ahk"

# Installs the rest of the software
Foreach ($s in $software)
{
    $install_start_time = Get-Date
    $filename = $s[2]
    $output = "C:\Users\$user\Downloads\$filename.exe"

    Write-Host "Downloading" $s[1]
    Invoke-WebRequest -Uri $s[0] -OutFile $output

    Write-Host "Installing" $s[1]
    Start-Process $output "/S"

    Write-Output "Time taken: $((Get-Date).Subtract($install_start_time).Seconds) second(s)"    
    Invoke-Expression "& refreshenv"
}

# Installs and updates all needed drivers for the system

# Finally, restarts the computer so changes take effect
Write-Output "Time taken: $((Get-Date).Subtract($start_time).Seconds) second(s)"
Write-Host "Restarting computer to save changes"
Restart-Computer    
