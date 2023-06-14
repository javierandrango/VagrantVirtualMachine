# Vagrant Virtual Machine (VM)
The virtual machine is a Linux server system (`Ubuntu 16.04.7 LTS (Xenial Xerus)`) that runs on top of my computer (`Windows 11`). You can share files easily between the computer and the VM and run a web services inside the VM which is able to access from the regular browser.

# Installation
## Prerequisites:

### 1. Git Bash

On `Windows` users is recommended the `Git Bash` terminal that comes with the `Git` software. Download `Git` from: https://git-scm.com/downloads 

### 2. Virtual Box

Virtual Box is the software that actually runs the virtual machine. At the moment I made this project I download the latest stable version (`VirtualBox 6.1.44`). Download the latest or the version I use here: https://www.virtualbox.org/wiki/Downloads

### 3. Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. At the moment I made this project I download the latest stable version (`Vagrant 2.3.6`). Download the latest or the version I use here: https://developer.hashicorp.com/vagrant/downloads

If vagrant is successfully installed, you will be able to run in the Bash terminal:
```bash
vagrant --version
```

## Run the Virtual Machine
Download the Virtual Machine configuration, cloning this repository into a directory in your computer:
```bash
git clone xxxxxxx.git
```
change the directory to the vagrant subdirectory. Use the comand `ls` to show the files inside the subdirectory.
```bash
cd vagrant/
ls 
```
Inside the vagrant subdirecctory there is a file `Vagrantfile` that contains all the necesary information, postgresql and python packages to run properly the VM. Run the command:
```bash
vagrant up
```
When the `vagrant up` command is finished running, you will get your shell propmpt back.
At this point you are able to log in to the newly Linux virtual Machine. Use the command:
```bash
vagrant ssh
```
**NOTE:** You can use as many terminal as you want, using the command `vagrant ssh` in the proper directory to make multiple operations inside the virtual machine 


