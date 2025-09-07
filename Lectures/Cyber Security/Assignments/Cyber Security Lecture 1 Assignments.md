---
creation date: 2025-09-06 12:53
modification date: Saturday 6th September 2025 12:53:20
tags:
  - Assignments
year: 2025
semester: 5
links: "[[Cyber Security Lecture 1]]"
---

---
# [[Cyber Security Lecture 1 Assignments]]

# Cybersecurity Lab Setup: Complete Step-by-Step Guide

## Prerequisites and System Requirements

### Disk Space Requirements

- **Total needed**: ~44 GB free space
    - Kali Linux with databases: 37 GB
    - Metasploitable 3 Linux: 5.6 GB
- **Space-saving tip**: If disk space is limited, use a plain Kali VM image (much smaller) and pair with someone who has the full setup for Exercise 03

### Important Security Notes

⚠️ **WARNING**: Metasploitable VMs contain intentionally vulnerable software. Keep them isolated in virtual machines and never expose them to external networks.

## Phase 1: Installing VirtualBox

### For Linux Users

```bash
# Use your distribution's package manager
# Ubuntu/Debian example:
sudo apt update
sudo apt install virtualbox virtualbox-ext-pack
```

### For Windows/macOS Users

1. Visit [virtualbox.org](https://virtualbox.org)
2. Download VirtualBox for your platform under "platform packages"
3. Install VirtualBox
4. Download VirtualBox Extension Pack from the same page
5. Look for "Oracle VM VirtualBox Extension Pack" → "All supported platforms"
6. Double-click the downloaded `.vbox-extpack` file to install extensions

## Phase 2: Setting Up Kali Linux VM

### Step 1: Download Kali Linux

Choose one of these options:

**Option A: Pre-configured Image (Recommended)**

- Download from the provided nextcloud share
- Includes GVM fully configured
- GVM admin password stored in Firefox and `~/gvm`

**Option B: Original Image**

- Download from official Kali website
- Select "VirtualBox Image"
- Choose version compatible with your system
- ⚠️ You'll need to install GVM manually (time-consuming and error-prone)

### Step 2: Import Kali VM

1. Open VirtualBox
2. Select "File" → "Import Appliance" OR double-click the downloaded file
3. Follow the import wizard

### Step 3: Configure Kali VM Settings

1. Select your Kali VM → Click "Settings"

**RAM Configuration:**

- Minimum: 1 GB
- Recommended: 2-4 GB (adjust based on your host system)
- Don't allocate so much that your host system becomes slow

**CPU Configuration:**

- Go to "System" → "Processor" tab
- Default: 2 CPUs
- Minimum: 1 CPU
- Increase for better performance if your host has multiple cores

**Network Configuration:**

- Go to "Network" tab
- Set "Attached to" → "NAT Network"
- We'll configure this properly in Phase 4

### Step 4: First Boot and Updates

1. Double-click Kali VM to start
2. Login credentials:
    - Username: `kali`
    - Password: `kali`
3. Update the system:

```bash
sudo apt update
sudo apt full-upgrade -y
```

4. **Security**: Change the default password if you plan to expose VM to network

## Phase 3: Setting Up Metasploitable3 VM

### Step 1: Download Metasploitable3

1. Download the Linux OVA file from:
    - vagrantup.com, OR
    - The provided nextcloud share
2. Unzip the downloaded file
3. Rename the extracted file to end with `.ova` (this helps VirtualBox recognize it)

### Step 2: Import Metasploitable3

1. In VirtualBox: "File" → "Import Appliance"
2. Select your renamed `.ova` file
3. If the file doesn't appear, clear the "filter" combo box at the bottom
4. Complete the import process

### Step 3: Configure Metasploitable3 Network

1. Select Metasploitable3 VM → "Settings"
2. Go to "Network" tab
3. Set "Attached to" → "NAT Network" (same as Kali)
4. Ensure both VMs use the same network configuration

### Step 4: Test Metasploitable3

1. Start the VM
2. Login credentials:
    - Username: `vagrant`
    - Password: `vagrant`

## Phase 4: Setting Up VM-to-VM Communication

You have two networking options. Choose based on your security preferences:

### Option A: NAT Network (Simple - Recommended for Beginners)

**Step 1: Create NAT Network**

1. VirtualBox → "File" → "Preferences"
2. Select "Network" from left panel
3. Click "+" to add new NAT Network
4. Ensure "Enable DHCP" is checked
5. Click "OK"

**Step 2: Configure Both VMs**

1. Shutdown both VMs completely
2. For each VM:
    - Select VM → "Settings" → "Network"
    - Set "Attached to" → "NAT Network"
    - Set "Name" → "NatNetwork" (the one you created)
    - Click "OK"

### Option B: Internal Network (Advanced - Better Isolation)

This option provides better security by isolating VMs from the internet.

**Step 1: Create DHCP Server (Command Line)** Open terminal/command prompt and navigate to VirtualBox installation directory:

```bash
# Check existing networks and DHCP servers
VBoxManage list intnets
VBoxManage list dhcpservers

# Create DHCP server for internal network
VBoxManage dhcpserver add --network=intnet \
--lowerip 10.0.0.2 \
--netmask 255.255.255.0 --upperip 10.0.0.254 \
--ip 10.0.0.1 --enable
```

**Step 2: Configure VM Network Settings** For each VM:

1. Settings → Network
2. Adapter 1: Set to "Internal Network", Name: "intnet"
3. (Optional) Adapter 2: Set to "NAT" for internet access on Kali only

## Phase 5: Testing Your Setup

### Step 1: Start Both VMs

1. Start Metasploitable3 first
2. Start Kali Linux
3. Let both systems fully boot

### Step 2: Find IP Addresses

**On Kali Linux:**

```bash
# Find your IP address
ip addr show
# or
ifconfig
```

**On Metasploitable3:**

```bash
# Find IP address
ip addr show
# or
ifconfig
```

### Step 3: Test Connectivity

**From Kali, ping Metasploitable3:**

```bash
ping [metasploitable3_ip_address]
```

**From Kali, scan Metasploitable3:**

```bash
nmap -sV [metasploitable3_ip_address]
```

If you see open ports and services, congratulations! Your lab is ready.

## Troubleshooting Common Issues

### VMs Can't Communicate

- Ensure both VMs are on the same network type (NAT Network or Internal)
- Check that DHCP is enabled in network settings
- Restart VMs after network changes
- Verify IP addresses are in same subnet

### Kali Linux Performance Issues

- Increase RAM allocation
- Add more CPU cores
- Enable VirtualBox extensions
- Close unnecessary applications on host system

### Metasploitable3 Won't Import

- Ensure file has `.ova` extension
- Try clearing import dialog filter
- Check file isn't corrupted (re-download if needed)

### Platform Compatibility (Apple M1/M2)

- ARM-based Macs need hardware emulation
- Enable older PC hardware emulation (i440FX +PIIX, 1996)
- Disable USB in VM settings
- Consider cloud alternatives (AWS, Azure)

## Security Reminders

1. **Never expose Metasploitable3 to external networks**
2. **Change default passwords** if VMs will be network-accessible
3. **Keep Kali Linux updated** regularly
4. **Use isolated networks** for testing
5. **Keep host system secure** and updated

