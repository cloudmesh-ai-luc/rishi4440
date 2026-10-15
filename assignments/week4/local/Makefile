# VMware Workstation Makefile
# change this path to your existing VM's .vmx file

VMRUN = "/c/Program Files (x86)/VMware/VMware Workstation/vmrun.exe"
#VMX = "/d/VM/New folder/Ubuntu 64-bit-3.vmx"

VM1 := "/d/VM/New folder/Ubuntu 64-bit-3.vmx"
VM2 := "/d/VM/Ubuntu/Ubuntu 64-bit.vmx"

# SSH usernames
VM1_USER := sam
VM2_USER := tony


#SSH_USER := ubuntu


help:
	@echo "VMware VM Management"
	@echo ""
	@echo "Default VM Commands (VM1)"
	@echo "make list         - List running VMware VMs"
	@echo "make start        - Start VM1"
	@echo "make stop         - Stop VM1"
	@echo "make suspend      - Suspend VM1"
	@echo "make reset        - Restart VM1"
	@echo "make status       - Check VM1 status"
	@echo "make ip           - Show VM1 IP address"
	@echo "make ssh          - SSH into VM1"
	@echo ""
	@echo "VM1 Commands"
	@echo "make start1       - Start VM1"
	@echo "make stop1        - Stop VM1"
	@echo "make suspend1     - Suspend VM1"
	@echo "make reset1       - Restart VM1"
	@echo "make status1      - Check VM1 status"
	@echo "make ip1          - Show VM1 IP address"
	@echo "make ssh1         - SSH into VM1"
	@echo ""
	@echo "VM2 Commands"
	@echo "make start2       - Start VM2"
	@echo "make stop2        - Stop VM2"
	@echo "make suspend2     - Suspend VM2"
	@echo "make reset2       - Restart VM2"
	@echo "make status2      - Check VM2 status"
	@echo "make ip2          - Show VM2 IP address"
	@echo "make ssh2         - SSH into VM2"
	@echo ""
	@echo "Multiple VM Commands"
	@echo "make start-all    - Start both VMs"
	@echo "make stop-all     - Stop both VMs"
	@echo "make status-all   - Show status of both VMs"


# --------------------------------------------------
# LIST
# --------------------------------------------------

list:
	$(VMRUN) list


# --------------------------------------------------
# DEFAULT COMMANDS - VM1
# Allows: make start, make stop, make status, etc.
# --------------------------------------------------

start: start1

stop: stop1

suspend: suspend1

reset: reset1

status: status1

ip: ip1

ssh: ssh1


# --------------------------------------------------
# VM1
# --------------------------------------------------

start1:
	$(VMRUN) start $(VM1)


stop1:
	-$(VMRUN) stop $(VM1) soft


suspend1:
	-$(VMRUN) suspend $(VM1) soft


reset1:
	$(VMRUN) reset $(VM1) soft


status1:
	@$(VMRUN) list | grep -F "Ubuntu 64-bit-3.vmx" > /dev/null \
	&& echo "VM1 is running" \
	|| echo "VM1 is stopped or suspended"


ip1:
	$(VMRUN) getGuestIPAddress $(VM1) -wait


ssh1:
	@IP=$$($(VMRUN) getGuestIPAddress $(VM1) -wait); \
	echo "Connecting to $(VM1_USER)@$$IP"; \
	ssh $(VM1_USER)@$$IP


# --------------------------------------------------
# VM2
# --------------------------------------------------

start2:
	$(VMRUN) start $(VM2)


stop2:
	-$(VMRUN) stop $(VM2) soft


suspend2:
	-$(VMRUN) suspend $(VM2) soft


reset2:
	$(VMRUN) reset $(VM2) soft


status2:
	@$(VMRUN) list | grep -F "Ubuntu 64-bit.vmx" > /dev/null \
	&& echo "VM2 is running" \
	|| echo "VM2 is stopped or suspended"


ip2:
	$(VMRUN) getGuestIPAddress $(VM2) -wait


ssh2:
	@IP=$$($(VMRUN) getGuestIPAddress $(VM2) -wait); \
	echo "Connecting to $(VM2_USER)@$$IP"; \
	ssh $(VM2_USER)@$$IP


# --------------------------------------------------
# MULTIPLE VMs
# --------------------------------------------------

start-all: start1 start2


stop-all: stop1 stop2


status-all:
	@echo "VM1:"
	@$(VMRUN) list | grep -F "Ubuntu 64-bit-3.vmx" > /dev/null \
	&& echo "  running" \
	|| echo "  stopped or suspended"
	@echo "VM2:"
	@$(VMRUN) list | grep -F "Ubuntu 64-bit.vmx" > /dev/null \
	&& echo "  running" \
	|| echo "  stopped or suspended"