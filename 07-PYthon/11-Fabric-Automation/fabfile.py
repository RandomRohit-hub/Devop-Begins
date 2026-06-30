# Module 11: Fabric Automation - Legacy Fabric Task Definitions
# Fabric allows running commands locally or on remote servers via SSH.
# Note: This syntax is for Fabric 1.x (Legacy).

from fabric.api import local, run, sudo, env, lcd, cd

env.user = 'devops'

def greeting(msg):
    print("Good {}".format(msg))

def system_info():
    print("Disk Space:")
    local("df -h")

    print("RAM size:")
    local("free -m")

    print("System uptime:")
    local("uptime")

def remote_exec():
    print("Get Remote System Info:")
    run("hostname")
    run("uptime")
    run("df -h")
    run("free -m")

    # Install and configure MariaDB
    sudo("yum install mariadb-server -y")
    sudo("systemctl start mariadb")
    sudo("systemctl enable mariadb")

def web_setup(WEBURL, DIRNAME):
    print("=" * 80)
    print("Installing local zip utility")
    print("=" * 80)
    local("apt install zip unzip -y")

    print("=" * 80)
    print("Installing Apache HTTPD, wget, and unzip on remote servers")
    print("=" * 80)
    sudo("yum install httpd wget unzip -y")

    print("=" * 80)
    print("Starting Apache Service")
    print("=" * 80)
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")

    print("=" * 80)
    print("Downloading and deploying website content")
    print("=" * 80)
    local("wget -O website.zip {}".format(WEBURL))
    local("unzip -o website.zip")
    
    print("=" * 80)
    with lcd(DIRNAME):
        local("zip -r tooplate.zip * ")
        put("tooplate.zip", "/var/www/html/", use_sudo=True)

    with cd("/var/www/html/"):
        sudo("unzip -o tooplate.zip")

    sudo("systemctl restart httpd")
    print("Website setup is completed successfully.")
