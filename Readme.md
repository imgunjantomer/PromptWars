RANSOMTRAP: PROACTIVE DECEPTION-BASED RANSOMWARE DEFENSE

> RansomTrap is a lightweight, real-time endpoint security framework designed to detect, intercept, and terminate algorithmic ransomware attacks before they can encrypt genuine user files.

> Instead of relying on traditional reactive signature matching or CPU-heavy continuous disk scanning, RansomTrap uses strategic canary tripwires paired with low-level OS event hooks to achieve sub-15 millisecond threat termination with zero user data loss.


PROBLEM STATEMENT
Traditional antivirus and EDR tools rely on virus signatures or post-execution behavior analysis. By the time a zero-day ransomware attack is detected, critical user files are already encrypted and lost.


OUR SOLUTION
> Instead of continuously scanning the disk, RansomTrap uses cyber deception:

> Places dummy Canary trap files (e.g., !0_passwords.txt) at strategic directory entry and exit points.

> Because automated ransomware scripts traverse directories systematically (alphabetically or recursively), they hit these trap files before reaching genuine user data.
> The moment a trap is modified, the attacking process is identified and terminated immediately.


HOW IT WORKS?
1. Trap Deployment: Lightweight decoy files are seeded across monitored folders.

2. Event-Driven Monitoring: Uses OS filesystem event hooks (ReadDirectoryChangesW / watchdog) instead of continuous polling, keeping CPU usage negligible.

3. Behavior & Entropy Verification: Checks for unauthorized write/modify bursts and high-entropy encrypted payloads to prevent false positives from legitimate applications.

4. Instant Kernel Termination: Traces the active Process ID (PID) and terminates it via OS-level calls in under 15ms.


KEY HIGHLIGHTS
1. Response Latency: < 15 ms

2. Background CPU Usage: < 0.1%

3. Genuine Data Loss: 0%

4. Zero-Day Ready: Works without needing prior malware signatures


TECH STACK
> Language & Core: Python (watchdog, psutil, os, ctypes)

> Backend & Dashboard: Flask, HTML, CSS, JavaScript

> OS APIs: Win32 ReadDirectoryChangesW & TerminateProcess


FUTURE SCOPE
1. Porting the background engine to C++ OR Rust as a native Windows File-System Minifilter Driver.

2. Adding a centralized dashboard for multi-endpoint monitoring across enterprise networks.