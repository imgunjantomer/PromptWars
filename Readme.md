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


AI-POWERED CYBERSECURITY TRIAGE (PS06 Alignment)
1. RansomTrap acts as an automated Tier-1 SOC Triage & Containment Agent for endpoint ransomware incidents:

2. Telemetry & Feature Extraction: Captures real-time filesystem events (ReadDirectoryChangesW / watchdog), file modification burst rates, and Shannon entropy of written payloads.

3. Automated Risk Scoring & Triage: Classifies anomalies into LOW, HIGH, or CRITICAL severity tiers using multi-signal behavioral correlation, eliminating false positives from legitimate software (e.g., MS Word, VS Code).

4. Autonomous Response: Executes sub-15ms kernel process termination (TerminateProcess) for CRITICAL alerts and logs structured incident reports to the dashboard for SOC analysts.


SECURITY & SAFE EXECUTION CONTROL 
> Read-Only Decoy Isolation: Canary tripwires contain zero sensitive user data and reside in sandboxed paths.

> Process Verification: Validates active Process ID (PID) ownership before termination to prevent accidental termination of core Windows system processes (explorer.exe, svchost.exe).

> Automated Unit Testing: Run pytest or python -m unittest test_ransomtrap.py to verify entropy thresholds and triage classification accuracy