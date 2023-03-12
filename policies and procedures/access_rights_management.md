# Access right management policy

Access control is a method that enables an administrator to give permissions to a user within a specified scope, whether it is an asset or information. Access control requirements should be incorporated into all business plans, as well as system and application design.

## Identity and access management

### Credentials

It is important to maintain a record of all individuals who have access to a system or application, along with their associated credentials. Credentials typically consist of a user identifier and one or more factors such as:

* Knowledge factor, such as a password or secret key
* Physical factor, such as a paired smartphone or YubiKey
* Inherence factor, such as a fingerprint

Sensitive assets, as defined in the information security policy, must require at least two factors from users to access them. Any exceptions to this rule should be communicated to the security and risk departments and approved by all stakeholders.

### User access rights

Access granted to users must be reviewed periodically to ensure that they are appropriate. Privileged accounts should only be allocated to users who require them for their work on a need-to-use basis and following the least privilege principle. The least privilege principle requires that users are granted the minimum rights required to perform their job.

Any request for access should follow the process outlined below:

* An employee should request access to an application on the Slack channel of the team responsible for the application.
* They should explain why they need access to the application and specify the requested privileges. If the asset is sensitive, they should copy their manager.
* If the team regularly receives such requests, a ticket can be created on a central tool to track operations.

### New employees

When a new employee or contractor joins the company, access to the required resources and systems should be granted based on their job function and department. The HR team is responsible for communicating this information to the IT and infrastructure teams, who will implement the access rights accordingly.

### Movers and outgoing employees

Whenever an employee undergoes a change in work duties, such as termination, transfer, promotion, or long-term absence (more than 6 months), their accesses must be revoked by the IT manager and the infrastructure team.

When an IT administrator leaves X_COMPANY, all passwords for the accounts they had access to must be reset. The use of shared accounts should be limited and properly documented.

### Third party access

Before assigning access to third parties, a risk assessment must be conducted to evaluate potential security risks. Access to X_COMPANY's information granted to external organizations must be managed and assessed regularly. Access rights must be limited and reviewed periodically, and authentication requirements must comply with the Information Security Policy (ISP).

Third parties are responsible for managing their end user identities, including ensuring that access granted matches the appropriate end users. Any changes to access granted, such as an outgoing end user, must be promptly reported to X_COMPANY.

## Passwords and API keys

X_COMPANY mandates that all employees accessing its networks and systems must have an individual user credential. Employees must create and manage their passwords according to the following standards:

* Standard accounts require passwords to be at least 10 characters long, while privileged accounts require passwords to be at least 12 characters long.
* Service account passwords must be at least 26 characters long.
* Passwords should not contain easily guessable words from a dictionary.
* User IDs will be disabled after 10 unsuccessful login attempts.
* Accounts and API keys that have been inactive for more than 6 months will be disabled.
* Default passwords must be changed upon installation and configuration.

Access to sensitive assets will require multiple factor authentication (MFA), along with the use of a security bastion where applicable.

In the event of a suspected account takeover or a security incident, potentially compromised accounts should be changed as soon as possible during the incident resolution process.

## Password storage

X_COMPANY provides a corporate password manager to all employees for securely storing passwords, API keys, and other confidential information. The password manager can also be used for sharing secrets among feature teams. It is mandatory for all employees to use this password manager to exchange secrets.

Sharing of secrets via open channels such as email, Slack, Jira, etc. is strongly discouraged as it undermines the security of X_COMPANY.

## Storage of passwords and application secrets

It is important that applications do not store user passwords in plain text within their databases. Instead, these passwords should be securely hashed using current, industry-standard cryptographic functions such as bcrypt or sha-512, utilizing a unique random salt for each user and multiple iterations for added security.

In addition, any secrets or API keys contained within configuration files should be retrieved dynamically using a central secret manager. It is imperative that clear-text secrets not be present within code repositories to prevent unauthorized access.

## Secret generation and default values

Passwords, including default and new ones, must comply with the password policy even if the end-user is prompted to change them upon login. Password reset procedures should never send passwords in clear-text to users. Instead, users should receive a link to generate a new password.