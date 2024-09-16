An example appserver image
==========================

**Note:** this project has not been updated in a while (and now marked read-only) but the techniques still illustrate the workflow.

This Packer build example is intended to illustrate building a simple appserver image from a corporate base image, and provisioning it using Packer's [ansible Provisioner](https://www.packer.io/docs/provisioners/ansible.html). The build AMI is then launched and tested with [TestInfra](https://testinfra.readthedocs.io).

This is the sibling repository of the Ansible role [ansible-example-appserver](https://github.com/jharley/ansible-example-appserver)

This repository was created as part of a presentation given to the DevOps Toronto monthly meetup on Nov. 7, 2017.  Slides from the talk are available [here](https://www.slideshare.net/JasonHarley3/building-immutable-machine-images-with-packer-and-ansible).
