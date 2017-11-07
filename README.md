An example appserver image
==========================

This Packer build example is intended to illustrate building a simple appserver image from a corporate base image, and provisioning it using Packer's [ansible Provisioner](https://www.packer.io/docs/provisioners/ansible.html). The build AMI is then launched and tested with [TestInfra](https://testinfra.readthedocs.io).

This is the sibling repository of the Ansible role [ansible-example-appserver](https://github.com/jharley/ansible-example-appserver)
