# Week 4 - Local VM Management with VMware Workstation

# Rushi's Local Vm

## Overview

This assignment uses VMware Workstation on Windows to manage local virtual machines through a Makefile. The Makefile uses VMware's `vmrun` command-line utility so that common VM management tasks can be performed directly from PowerShell using `make` commands.

Two existing Ubuntu virtual machines were used to verify that the Makefile can manage both a single VM and multiple VMs.

## Environment

- Host operating system: Windows
- Shell: PowerShell
- Local VM framework: VMware Workstation
- Guest operating systems: Ubuntu
- Number of VMs tested: 2
- Automation tool: Make
- VMware command-line utility: `vmrun`

## VM Management

The Makefile provides commands for managing individual VMs as well as both VMs together.

### General Commands

```powershell
make help
make list
```

`make help` displays the available Makefile targets, while `make list` shows the VMware virtual machines that are currently running.

### Single VM Commands

The default commands operate on VM1:

```powershell
make start
make status
make ip
make suspend
make start
make stop
```

Individual VM targets are also available:

```powershell
make start1
make status1
make ip1
make suspend1
make stop1

make start2
make status2
make ip2
make suspend2
make stop2
```

SSH targets are included for connecting to each VM when SSH is available:

```powershell
make ssh1
make ssh2
```

## Managing Multiple VMs

The same Makefile can manage multiple machines by defining separate VM paths and SSH usernames for each VM.

The following commands were used to test management of both Ubuntu VMs:

```powershell
make start-all
make status-all
make list
make ip1
make ip2
make suspend2
make status-all
make stop-all
```

This demonstrates that one Makefile can manage more than one VMware virtual machine without requiring separate Makefiles for each VM.


## Result

The VMware Makefile successfully managed two Ubuntu virtual machines from Windows PowerShell. The tested operations included listing running VMs, starting VMs, checking status, obtaining IP addresses, suspending a VM, restarting it, stopping VMs, and managing both machines together.
