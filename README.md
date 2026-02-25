# 🛡️ foundations_final_project | C. K. Bachoo

**Author:** Chad K. Bachoo, A+ Innovation Fellow, Navy Veteran 🎖️  
**Institution:** The Knowledge House, New York  
**Cohort:** NY-IF-CS-26 (February 2026)  
**Lead Instructor:** George Robbins  

---

## Project Overview
This repository serves as the primary technical staging environment for the Cybersecurity Foundations Intensive. It reflects a rigorous **Purple Team methodology**, integrating defensive posture with offensive insight to ensure mission readiness regardless of hardware limitations [1, 3].

## Core Learning Objectives
*   **Network Defense:** Implementing robust firewalls and rule-based access controls.
*   **Security Automation:** Utilizing Python for rapid deployment of security tasks.
*   **Infrastructure Scaling:** Managing hybrid virtual environments via Termux and GitHub Codespaces.

## Security Philosophy & Governance

### 1. The CIA Triad Mapping
*   **Confidentiality:** Access is restricted using **Multi-Factor Authentication (MFA)** and private SSH keys, adhering to **CIS Control #5** [4, 5]. Personally Identifiable Information (PII) is sanitized to protect identity.
*   **Integrity:** The use of **Git cryptographic hashing** ensures configuration tracking and **Non-repudiation** [4, 6]. Every commit provides a verifiable audit trail of technical actions.
*   **Availability:** Resiliency is maintained through **GitHub Codespaces** deployment, providing hardware-agnostic, cloud-native access to the workstation [7, 8].

### 2. AAA Implementation
*   **Authentication:** Phishing-resistant MFA on the GitHub platform [7].
*   **Authorization:** Principle of Least Privilege (PoLP) applied to branch permissions [7].
*   **Accounting:** All technical actions are logged via the **GitHub Audit Log** for full traceability [7, 9].

### 3. Infrastructure Hardening (The Mobile Security Stack)
This project utilizes a specialized security stack to ensure environment integrity while working from a mobile device:
*   **Local Environment:** **Termux** (Android Linux Virtualization) provides the local engine for initial staging and script testing.
*   **Cloud Environment:** **GitHub Codespaces** (Ubuntu-based Linux) provides the primary workstation, ensuring high availability.
*   **DNS Security:** **Quad9** (Encrypted DNS/Threat Blocking) acts as the shield, blocking malicious domains and preventing traffic sniffing [User Query].
*   **Software Provenance:** **F-Droid** (Verified Open-Source Repository) ensures the integrity of mobile security tools [User Query].
*   **Documentation:** **Linux Command Library** serves as the primary reference for POSIX-compliant syntax [User Query].

## Technical Proof (LAB_AUDIT.PY)
The environment is verified using an automated Python script that audits the OS platform and Git status. A successful audit confirms:
*   **OS Platform:** linux
*   **Git Status:** Operational ✅
*   **Mission Status:** Verified & Ready ✅

## Project Narrative: The "Mission-First" Pivot
Faced with hardware limitations while awaiting equipment, this workstation was engineered to prove that a cybersecurity professional's value lies in their **methodology**, not their hardware. By pivoting from local mobile virtualization to cloud-native Ubuntu environments, this project serves as a case study in **infrastructure scaling** and **resilient engineering** [1, 9].

# Foundations Lab Final - Security Environment

## Mission Objective
To establish a structured, automated security workstation for auditing and evidence collection. 

## Technical Mapping
* **Termux**: Handheld Linux (Sandboxed Android Environment)
* **Codespaces**: Virtualized VMware/Linux Workstation
* **Packet Tracer**: Network Simulation & Traffic Generation

## Environment Architecture
* **scripts/**: Contains `lab_audit.py` for automated environment verification.
* **pcap/**: Directory staged for network traffic capture (Packet Tracer Exports).
* **slack/**: Directory staged for incident response logs and alerts.

## Verification Status
- [x] Linux Environment: **Operational** (Termux/Codespaces)
- [x] Python Security Script: **Verified**
- [x] Git/GitHub Integration: **Mission Ready**

---

## References
*   Center for Internet Security. (2024). *CIS Controls v8.1*. [10].
*   CompTIA. (2025). *A+ Core Certification Study Guide*. [10].
*   National Institute of Standards and Technology. (2024). *NIST Cybersecurity Framework (CSF) 2.0*. [10, 11].
