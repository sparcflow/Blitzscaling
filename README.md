# Blitzscaling
The repo containing scripts and documents portraid in the book [Blitzscaling security](https://www.amazon.com/dp/B0BMZFLHZR).

## Cloudtrail to Elastic

This folder contains a lambda written in Golang that gets triggered new files on an S3 bucket containing Cloudtrail logs. It downloads these files, parses them and sends them to an ElasticSearch instance.

The lambda is deployed using the [Serverless framework](https://www.serverless.com/framework/docs/providers/aws/guide/functions).

Customize the file serverless.yml (bucket name, secret name, etc.) and deploy the lambda using:

```bash
$ npm install -g serverless # install serverless
$ make deploy
```

*Todo: rewrite clients using interfaces to ease testing via dependency injection and avoid global variables*

## list domains
A handy script that goes over every hosted zone on AWS Route53 and lists its A, AAAA and CNAME records. It qualifies each record with an attribute "private", reachable only from certain VPCs, or "public", reachable from the Internet.
```bash
$ python -m pip install -r requirements.txt
$ python list_domains.py
```

## list policies
A script to break statements in policies attached to users, roles and groups. It extracts both attached and inlines policies in a CSV format.

It also has a basic qualification logic to determine whether a statement contains dangerous permissions or not. It's a simple example that can be further customzied and polished.
```bash
$ python -m pip install -r requirements.txt
$ python list_policies.py
$ head res.csv
```

## list resources
A simple python script to list every tagged AWS resource in a given region. The output is in CSV
```bash
$ python -m pip install -r requirements.txt
$ python list_resources.py
```

## pinning
A bash script to calculate the TLS certificate's public key digest of a given host
```bash
$ ./display_pinning_hash.sh google.com
```

## policies and procedures
Templates of an information security policy and an access right management policy, two essential documents for any organization.
I used ChatGPT to reword the original documents to avoid accidentally leaking any data. They should give you an idea of what such documents must contain. Don't hesitate to adapt and mold them to your needs.

## windows
* sysmon.xml: the Sysmon config as posted by SwiftOnSecurity [here](https://github.com/SwiftOnSecurity/sysmon-config) with one rule added about lsass.exe access. I might add some more later on.
* winlogbeat.yaml: a quick config that directs Winlogbeat to extract the most important audit events and providers from a Windows machine.