Building an ARP Network Scanner with Scapy (And the Painful Lessons Learned)

This project came out of Zaid Sabih’s "Learn Python & Ethical Hacking From Scratch" course. The objective was straightforward: write a Python script using the scapy library to craft and send ARP requests, effectively discovering devices on a local network.

The final code is barely fifteen lines long. Getting it to run on a modern Kali Linux VM, however, was a masterclass in environment management, dependency hell, and debugging.

Here is what I built. A script called `network_scanner.py` that creates an ARP request packet using `scapy.ARP`. It wraps that packet in an Ethernet broadcast frame via `scapy.Ether`. Then it uses `scapy.srp()` to send the packet and capture replies. Finally, it parses those responses to display a list of IP and MAC addresses.

Getting there was not smooth. Here is every wall I hit and how I climbed over them.

**1. The "Silent Crash"**

The script would run with zero output. No errors. Exit code 0. Just silence.

Diagnosis? Scapy relies on other libraries to interact with network interfaces. Python was crashing instantly before it could even print an error message.

Fix: I installed the missing network library system-wide:

```bash
sudo apt install python3-netifaces
```

**2. The PEP 668 "Externally Managed Environment" Error**

I tried to install Scapy using `pip3 install scapy`. Kali Linux blocked it immediately, warning that the environment is externally managed.

Modern Kali Linux prevents global pip installs to protect the system Python. To bypass this safely, I used the `--break-system-packages` flag. Alternatively, you can install via apt where available.

**3. The PyCharm "Virtual Environment" Trap**

The code worked in my root terminal. But PyCharm kept showing yellow warnings ("Cannot find reference 'ARP' in 'scapy.all'") and refusing to run.

PyCharm creates its own isolated Python environment (`.venv`). Just because I installed Scapy in the system terminal didn’t mean PyCharm’s `.venv` had it.

Fix: I opened PyCharm’s built-in terminal and installed the package directly into its environment:

```bash
pip install scapy
```

**4. The Rogue Indentation (The Final Boss)**

Even after all packages were installed, the script ran but skipped all logic inside the `scan()` function.

The function calls at the bottom of the script (`scan("10.0.2.0/24")`) were indented. Python thought they were part of the function definition. So they never executed.

Fix: Dedented the function calls so they sat flush with the left margin.

**Key Takeaways**

IDEs are not magic. PyCharm handles environments differently than the terminal. You must ensure libraries are installed in the environment your IDE is using.

Silence is a symptom. In Python, a script that does nothing usually means a missing dependency crashed it before it could even print a traceback.

Indentation is king. A single accidental space in Python can change the entire logic of a script without throwing a syntax error.

**How to Run It**

Ensure you are on a Linux system (Kali preferred). Install Scapy: `pip install scapy netifaces`. Run the script with root privileges, required for raw packet sending:

```bash
sudo python3 network_scanner.py
```

Happy Hacking!
