# Week 3.4 — VM Comparison


## 1. Local Virtual Machine vs. Cloud VMs

| Category | Local Virtual Machine | Jetstream | Chameleon Cloud |
|---|---|---|---|
| Setup | Configure virtualization software, an OS image, and virtual hardware on the host computer. | Create an instance in the cloud portal and configure access. | Select the class project, create a lease, choose an image and reserved flavor, and configure access. |
| Flexibility | Useful for experiments on the host computer. | Provides remote compute resources without using the host's CPU and RAM for the guest OS. | Provides reserved remote resources for a scheduled period. |
| Resources | Limited by the host computer's CPU, RAM, and storage. | Uses resources provided through a cloud allocation. | My reserved flavor provided 1 vCPU, 2 GB RAM, and 20 GB disk. |
| Access | A local console is available through the virtualization software; SSH can also be configured. | Remote access depends on the portal and instance configuration. | I connected using SSH from Windows PowerShell. |
| Networking | Local access does not require a cloud floating IP. | Remote access requires appropriate network and authentication settings. | SSH access required network configuration and an SSH security group. |
| Resource management | Start or stop the VM and manage its local disk files. | Manage instances and release resources when finished. | Manage the instance and associated resources within the lease window. |


## 2. Experience Using Jetstream

I completed the Jetstream VM task before working on Chameleon. Jetstream introduced the process of creating a VM on remote infrastructure rather than running the guest operating system on my own computer.

Cloud VM creation and access involve separate considerations: the instance needs suitable resources and an OS image, while remote access also depends on networking and authentication. Compared with a local VM, cloud infrastructure requires more attention to project allocations and remote access settings.


## 4. Experience Using Chameleon Cloud

I used the class project provided by my professor on KVM@TACC and configured my preferred timezone. I explored the portal, created a resource lease, and waited for its status to change from `PENDING` to `ACTIVE` before launching the instance.

The reservation was initially longer than the assignment allowed. I shortened it to 56 minutes, from October 8, 2026, at 19:13 UTC to 20:09 UTC. This brought the reservation within the assignment's one-hour limit.

The selected reserved flavor provided 1 vCPU, 2 GB RAM, and 20 GB of disk. The assignment called for the Chameleon Ubuntu 24.04 image. I configured SSH access using a public key and connected from Windows PowerShell. I captured screenshots of the lease page and the SSH terminal as evidence.

The most confusing part was understanding the difference between reserving resources and launching an instance. The lease made the resources available for a specific period; launching the instance was a separate step but found it similar to Jetstrem cloud.

## 5. Local Virtual Machine

A local VM runs on the host computer and uses resources assigned through virtualization software. Basic console access does not require a cloud project, a resource reservation, or a floating IP. This makes a local VM convenient for testing software and experimenting with operating systems.

The main limitation is the host computer's hardware. Allocating more CPU, memory, or storage to a VM leaves fewer resources available to other applications on the host. Unlike the remote Chameleon VM, the local guest depends directly on the host computer's capacity. But I prefer to test and debu my apps localy before pushing them to cloud! 


## 5. Advantages and Disadvantages

### Local VM (VM Ware WorkStation)

**Advantages:**

- Direct console access through local virtualization software.
- No cloud reservation required.
- Convenient for testing and experimentation.
- Can operate without internet access once required software and images are installed, depending on the task.

**Disadvantages:**

- Limited by the host computer's hardware.
- Shares CPU, memory, and storage with other host applications and Requires local virtualization software and disk space.

### Jetstream Cloud

**Advantages:**

- Provides remote compute resources.
- Provides experience with cloud instance management and remote access.

**Disadvantages:**

- Remote access requires network connectivity.
- Authentication and networking may require troubleshooting.
- Resource availability depends on the cloud allocation and capacity.

### Chameleon Cloud

**Advantages:**

- Provides remote resources through a reservation system.
- Offers practical experience with leases, flavors, SSH keys, and networking.
- Makes the allocation period explicit.

**Disadvantages:**

- Requires additional planning before instance launch.
- Depends on an active lease and available resources.
- Requires careful management of reservation times and remote access configuration.

## 6. Overall Comparison

Local virtualization keeps VM creation and basic access on the host computer, but its capacity is limited by that computer system . Jetstream provides remote infrastructure and introduces cloud instance management. Chameleon adds an explicit reservation process, which required me to plan the resource usage period before launching the instance its a bit of over head i belive.

My Chameleon experience showed that an active lease, a selected reserved flavor, and correctly configured SSH access are separate requirements. It also highlighted the importance of checking reservation times: I needed to shorten my initial lease to satisfy the assignment.

## 7. Evidence

- I have added required screenshots in /assignments/week3/ 
