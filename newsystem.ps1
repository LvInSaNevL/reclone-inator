# The list of packages installed with Chocolatey
$packages = @("adobereader",
              "git",
              "poshgit",
              "git-lfs",
              "7zip",
              "notepadplusplus",
              "vlc",
              "nodejs",
              "autohotkey",
              "flashplayerppapi",
              "gimp",
              "python3",
              "virtualbox",
              "windirstat",
              "audacity",
              "vscode",
              "steam"
              "spotify",
              "cpu-z",
              "obs-studio",
              "everything")

# The list of software installed from installers              
$software = @(("https://discordapp.com/api/download/canary?platform=win", "Discord Canary", "discordcanary"),
              ("https://cdn-fastly.obsproject.com/downloads/OBS-Studio-22.0.2-Full-Installer-x64.exe", "OBS", "obs"),
              ("https://download.microsoft.com/download/1/3/F/13F19BF0-17CF-4D0F-938C-41D0489C3FE6/KB3133719-x64.msu.msu", "Microsoft Media Pack", "microsoft_media_pack"))
              
# Sets permissions and methods for the rest of the scripts
Invoke-Expression "& Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass"
[Net.ServicePointManager]::SecurityProtocol = "Tls12, Tls11, Tls, Ssl3"

# Sets up the system
Invoke-Expression "& cd 'HKCU:\Control Panel\Desktop'"
Invoke-Expression "& Set-ItemProperty -Path . -Name LogPixels -Value 125"

# Installs Chocolatey if it's not already installed              
If(-Not (Test-Path -Path "$env:ProgramData\Chocolatey")) {
    Invoke-Expression "& ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
}

# Install .NET CLI environment
#Invoke-Expression "& .\dotnet-install.ps1"

# Installs each package in Chocolatey
Foreach ($p in $packages)
{
    $command = "choco install " + $p + " -y"
    Write-Host $command
    Invoke-Expression "& $command"
}

# Installs the rest of the software
Foreach ($s in $software)
{
    $start_time = Get-Date
    $filename = $s[2]
    $output = "C:\Users\mwollam\Downloads\$filename.exe"

    Write-Host "Downloading" $s[1]
    Invoke-WebRequest -Uri $s[0] -OutFile $output

    Write-Host "Installing" $s[1]
    Start-Process $output "/S"

    Write-Output "Time taken: $((Get-Date).Subtract($start_time).Seconds) second(s)"
}

# Finally, restarts the computer so changes take effect
Restart-Computer    