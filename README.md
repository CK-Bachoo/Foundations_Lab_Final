# 🛡️ foundations_final_project | C. K. Bachoo

**Author:** Chad K. Bachoo, A+ Innovation Fellow, Navy Veteran 🎖️  
**Institution:** The Knowledge House, New York  
**Cohort:** NY-IF-CS-26 (February 2026)  
**Lead Instructor:** George Robbins  

---

## 🚀 Project Overview
This repository serves as the primary technical staging environment for the **Cybersecurity Foundations Intensive**. It is established to manage version-controlled documentation and lab configurations that reflect a rigorous **Purple Team** methodology—integrating defensive posture with offensive insight.

## 🏁 Core Learning Objectives
* **Network Defense:** Implementing robust firewalls and rule-based access controls.
* **Traffic Analysis:** Monitoring packet-level data with Wireshark to identify signature-based anomalies.
* **Security Automation:** Utilizing Python for rapid deployment of security tasks and log management.
* **Infrastructure Scaling:** Managing hybrid virtual environments via **VMware**, **Termux**, and **GitHub Codespaces**.

---

## 🛠️ Night 1: Mission Statement & Methodology
The following lab milestones were executed using a **"Security-First"** approach, ensuring all configurations meet industry standards for hardening and resilience.

1. **Environment Staging:** Configured a virtualized laboratory environment utilizing an Ubuntu Server instance and Kali Linux nodes.
2. **Network Surveillance:** Deployed Wireshark to intercept and analyze local network traffic for potential lateral movement and intrusion vectors.
3. **Task Automation:** Developed custom Python scripts to automate system health telemetry and security log rotation.
4. **Validation & Audit:** Verified firewall integrity and user permissions to enforce the **Principle of Least Privilege (PoLP)**.

---

## 🏛️ Night 2: Security Philosophy & Governance
**Current Phase:** Strategy Room Mapping (NIST CSF 2.0 & CIS Controls)

### **1. The CIA Triad Mapping**
* **Confidentiality:** Access is restricted via **CIS Control #5** (Account Management) using GitHub MFA and private SSH keys to prevent unauthorized data exposure.
* **Integrity:** We utilize Git's cryptographic hashing to ensure **Non-repudiation**. Any unauthorized changes to the system configuration are detectable via version history.
* **Availability:** Resiliency is maintained through the **GitHub Codespaces** deployment strategy, ensuring the workbench is accessible regardless of local hardware status.

### **2. AAA Implementation**
* **Authentication:** Enforced via phishing-resistant MFA on the GitHub platform.
* **Authorization:** I apply the **Principle of Least Privilege (PoLP)** by restricting write permissions to the main branch.
* **Accounting:** All technical actions and script executions are logged via the GitHub Audit Log for traceability and compliance.

---

## 📚 References
*The following resources provided the foundational frameworks for this project:*

Bachoo, C. K. (2026). *foundations_final_project: Technical infrastructure summary* [Unpublished laboratory manual]. GitHub Repository.

Center for Internet Security. (2024). *CIS Controls v8.1: Critical security controls for effective cyber defense*.

CompTIA. (2025). *A+ core 1 & core 2 certification study guide*. CompTIA Press.

National Institute of Standards and Technology. (2024). *The NIST cybersecurity framework (CSF) 2.0*. U.S. Department of Commerce.

Robbins, G. (2026). *Cybersecurity foundations intensive: Unit 3 - Network defense and firewalls* [Lecture notes]. The Knowledge House.

The Knowledge House. (n.d.). *Foundations lab workbook: Version-controlled documentation and configurations*. 

---

`[ Status: Night 1 & 2 Verified ✅ | Logic: Analytical | Focus: Purple Team 🛡️ ]`
