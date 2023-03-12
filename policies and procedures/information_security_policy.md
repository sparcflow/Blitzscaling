# Informations security policy

## Introduction

X_COMPANY operates the X_APP along with its supporting infrastructure which allows customers to perform X_OPERATIONS.

The information security policy (ISP) sets the organisational and technical requirements to ensure the confidentiality, integrity and availability of X_COMPANY's critical logical and physical assets, resources and sensitive data. Such requirements apply to data whether at rest, in transit or in use and aim to cover the risk mapping described in the present document.

This policy does not cover topics pertaining to the physical security of the workplace and of the personal computer. These subjects are covered by the Office Management procedure X_OFFICE_PROCEDURE.

## Regulatory framework
X_COMPANY is a regulated body and must comply with legal and prudential requirements related to data protection and information security, as mandated by X_LEGAL_CODE_REFERENCE. To adhere to these frameworks, the present document outlines high-level principles and rules designed to safeguard the confidentiality, integrity, and availability of both X_COMPANY and their customers' data and information.
The following are the legal frameworks that apply to X_COMPANY:
* X_LEGAL_REF_1
* X_LEGAL_REF_2

## Risk assessment

### Incident types

In its risk mapping, X_COMPANY has identified several types of possible threats to its information systems, which can be grouped into 4 macro categories:

- **Direct attacks on the information system:** theft of data and/or resources supporting this data, data modification and denial of service.
- **Attacks targeting employees:** bribery, phishing, distributing malicious USB keys and so on.
- **Attacks targeting customers:** phishing, malware and so forth.
- **Incidents**, natural or not, affecting data and/or information systems.

### Threat model

The security measures and requirements outlined in this document are designed to address the following major threat actors:

* Automated tools scanning the internet for easy targets such as default login credentials, leaked passwords, and unpatched systems.
* Hackers with moderate technical knowledge who exploit web vulnerabilities, engage in social engineering, or use phishing attacks to defraud customers.
* Skilled hackers with advanced knowledge and access to sophisticated exploits that target critical components. This threat group includes insider attacks.
* Organized crime groups composed of highly motivated and talented hackers who specifically target companies like X_COMPANY for financial gain. This threat group also includes insider attacks.
* Nation-state sponsored attackers, such as cyber-espionage groups affiliated with government agencies.

## Key security goals

Information security is an essential activity that ensures the appropriate protection of information while allowing it to be shared and used as necessary. It is a cross-functional responsibility that encompasses the following key elements:

* Availability: Ensuring that X_COMPANY's delivery platform is globally available and that employees have access to information, applications, and services that they need to perform their jobs.

* Integrity: Maintaining the accuracy and completeness of information and processing methods.

* Confidentiality: Ensuring that information is kept confidential and not disclosed to unauthorized parties.

µ Traceability: The ability to maintain relevant audit trails and provide evidence of actions taken on systems. Traceability also encompasses legal objectives such as non-repudiation and accountability.

* Compliance: Ensuring that X_COMPANY's operations comply with this policy and other applicable rules, laws, and policies within the organization.

## Validation, review and responsibilities

X_COMPANY's information security officer is responsible for **establishing, maintaining** and promoting the information security policy across X_COMPANY. They leads its **implementation** and monitors **compliance with the help of the Risk and Internal Control teams**

The present document (ISP) must be **reviewed** yearly or in case of:

- Internal events, organisation changes
- External events such as regulatory changes or international standards;
- Identification of new security threats;
- Changes due to controls, assessments or audits.
- Major evolution of information systems

The ISP is submitted to the Risk committee and validated by the executive team. Every decision resulting in a non-compliance to this policy must be submitted to the Risk committee for validation.

# Organisation & governance

The information security officer's main assignments are to:

- Define information security policies and maintain them
- Build an information security roadmap to address the risk mapping defined by the risk department
- Regularly assess X_COMPANY's information security level regarding the protection of its assets
- Identify, monitor and assess vulnerabilities
- Design and follow corrective action plans
- Information security awareness

The **information security officer reports to the X_HIERARCHY**.

The information security officer holds monthly meetings with the Risk & compliance team in order to follow key operational indicators: critical vulnerabilities discovered, progress of key security projects and implementation of the remediation plans.

High level KPIs and strategic projects are shared by the information security officer quarterly with the executive team during the X_SECURITY_RISK_COMMITTEE

# Human resources

Every employee, external worker and third party must understand and comply with the ISP. The document must be published in the internal X_COMPANY board and referred to during the onboarding procedure.

## Newcomers

In the case of new employees who require high-level access, such as infrastructure administrators or sensitive project managers, or those who will have access to sensitive information, it may be deemed necessary for the company to conduct employment screening. This screening process may include contacting the references listed on the candidate's resumé, obtaining a certificate of no conviction, or other methods of verification as required by the laws of each country in which the company operates.

## External workers

**External worker contracts** must be compliant with the ISP. External workers' accesses to X_COMPANY's data must be clearly identified and limited to their need-to-know. In the event that external workers have access to sensitive or confidential information, they must sign a **Non-Disclosure Agreement and a DPA (data processing agreement)**

## Moving and outgoing employees

Managers are responsible for ensuring that access rights are modified according to **role changes** within their teams. Previous accesses must be **revoked in a timely manner**.

Before end of contract, outgoing employees must **return corporate IT devices**, such as mobile phones, laptops. Their **accesses** and **accounts** must be **deleted** from every system during their offboarding process on their last day at the office.

## Employee’s discretion

X_COMPANY's employees are responsible of protecting the confidentiality and integrity of the data made available to them when performing their duties:

- **Sensitive paper information** must be locked away when not required, especially when the office is vacated
- Personal computers containing sensitive information must be **logged off or password protected** when **left unattended**
- **Sensitive paper information** must be cleared from printers immediately after printing;
- **Shredders** must be used to destroy any paper containing sensitive information.

It is important for employees to be cautious about sharing sensitive information on social media platforms. Even outside of the workplace, they should exercise caution with the information they disclose or may inadvertently reveal, such as by taking a phone call in a public location (e.g. restaurants, airport lounges) or working on their laptops in public areas.

## Awareness

To ensure that employees are aware of information security issues and adhere to relevant rules, the information security officer should implement information security training programs based on the company's information security principles. Upon joining the company, all new employees should receive a security session that outlines the organization's security vision and the tools available to them.

# Data & Asset management

## Sensitive assets

A sensitive asset refers to any device that satisfies one or more of the following conditions:

* Contains or processes sensitive information, including but not limited to business servers, databases, and workstations.
* Is necessary to support business continuity or is used to access sensitive information, such as a back-office application or router.

Confidential or sensitive information pertains to any type of data that, if disclosed to unauthorized parties, could result in significant or extreme loss to X_COMPANY and/or its customers. Personal data is considered sensitive information in accordance with GDPR/CCPA.

## Asset inventory

### Platform

It is the responsibility of the security team to identify all platform assets that support X_COMPANY's business. An inventory of assets must be maintained and regularly updated, including the owner of each asset, the service name, and its usage.


### Applications

Every team is required to maintain a detailed inventory of their assets, including information on the type of data stored, its level of sensitivity, and the recovery time objectives.

### Workstations and corporate devices

The IT department should keep an up to date inventory of workstations and devices distributed to employees.

## Access and monitoring

Sensitive assets must only be administered by one of the following team depending on the level of expertise required by the asset:

- The owner of the asset in case of a specialised asset with limited scope
- The IT or Infrastructure admin for assets with shared responsibilities or affecting multiple teams

The on-call team may have access to sensitive assets during emergencies. **Access** and **activities** on **these assets** must be **monitored**.

## Change management

With the exception of emergency situations, all changes to X_COMPANY's production environment must be **traced, reviewed** and should preserve or increase the security level of the platform. Changes done in emergency situations must be documented.

## Security assessments

Sensitive assets must be subjected to regular information security assessments performed by a third party, according to known security standards ([OWASP framework](https://owasp.org/www-project-web-security-testing-guide/latest/3-The_OWASP_Testing_Framework/1-Penetration_Testing_Methodologies) for instance). These tests can include a penetration test, code review, system and architecture review or other forms of vulnerability assessments.

The **integrity** of information published on a **publicly available system** must be protected to **prevent unauthorized modification** and **mitigate reputational risks.**

## Backup

The infrastructure team should ensure that information backups are maintained with respect to business needs. Backups of sensitive assets must be **performed** and **restoration tested regularly**. These backups have the **same sensitivity** as the **original information** and must comply with the **same information security requirements.**

# Physical and environmental security

## Physical security

Computing devices must be operated in a **secure environment** in order to avoid external and physical hazards to block or impede their functioning. Physical security implies:

- Protection measures against **environmental risks**, such as floods or earthquakes
- Protection against **fire**
- Physical **access control**
- **Cooling**, **network** and **power** distribution

In application of the **risk driven approach**, physical security requirements depend upon **how sensitive** the **assets** are.

## Workstation security

**Laptops** must be **encrypted**, kept up-to-date with regards to security patches and deny any incoming trafic. **When left unattended, laptops must be password-locked**.

## Transport and storage devices

**Information transfer** and **external storage devices** must not carry **sensitive information** without **encryption.**

# Logical security

## Platform security

### Hardening and protection

Platform components should be configured in accordance with the best security practices in order to guarantee defence in depth, confidentiality, integrity and traceability of information.

Default configurations should be updated and adjusted to address the threat scenarios put forth in this document, from password management, to ssh configuration to secret management and so on. When possible it is worth following standards published by the [NIST bureau](https://nvd.nist.gov/ncp/repository).

### Security monitoring

All activities pertaining to platform assets must be logged and stored in a dedicated repository. A log retention policy should be established in accordance with the sensitivity of information and local regulations, and must retain logs for a minimum of 6 months for sensitive assets. Additionally, all logs must be timestamped with a unique time base.

**Log management tools** and **log information** should be protected against tampering and unauthorised access. **Faults** should be logged, analysed and appropriate actions taken. Logs of sensitive assets must be reviewed by the infrastructure or security team on a regular basis.

### Patch management

To identify vulnerabilities, X_COMPANY's IT and production networks and systems must be monitored and controlled. Security patches should be applied in accordance with X_COMPANY's change management process and business requirements. For sensitive assets, all security patches must be applied promptly.

### Access control

The infrastructure team should be the only group granted access to production platform components. However, read or write access rights may be delegated to other teams as long as the following security measures are met:

* The delegated access should be limited to use cases requested by the team in accordance with the least privilege principle.
* Delegation should not pose any systemic risk to other components.
* All access should be tracked and logged.

Each employee should be granted individual access to components based on the least privileged principle and on a need-to-know basis.

## Network security

X_COMPANY's network architecture should have multiple layers of protection and be safeguarded from external threats by utilizing firewall services that are monitored regularly. To ensure the availability of X_COMPANY's IT networks and systems, every sensitive asset on the network should either have replacement equipment or redundancy.

Access to the production environment through offices should be restricted to a specific and clearly defined network segment isolated from the Guest Wi-Fi. Authentication to network equipment should be based on individual accounts and certificates.

The use of the WPA2-PSK mode may be acceptable in smaller offices as long as they have no connection to the production environment.

## Application security

### Secure coding

To protect against common types of attacks such as injection attacks, session hijacking, and indirect object reference, development should adhere to the OWASP secure coding practices. The security team must conduct regular security assessments of the code to ensure there are no application vulnerabilities present on the production systems.

### Internet exposure

To ensure protection of assets, security equipment such as a WAF, firewall, or anti-DOS protection should be used as an intermediary to block suspicious requests from untrusted networks. The specific security device and protection utilized may vary based on the sensitivity of the asset exposed.

### Security by design

The security team should conduct a security assessment for new projects and features that handle sensitive data, starting from the specification phase and continuing through development. This assessment may include one or more of the following:

* Incorporating risk analysis into the specifications
* Implementing security measures from the outset
* Conducting architecture and system reviews
* Performing penetration tests during the QA or beta release phase.