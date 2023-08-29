## Description
This repository contains everything needed to build the bionic64-kind vagrant box.This box is based on the hashicorp/bionic64, a standard Ubuntu 18.04 LTS 64-bit provided by Hashicorp.

The next tools are included in the box:

* kind
* docker
* kubectl

The cluster created by kind will have an ingres controller (nginx) and a local docker registry.
Also, in the nginx-app-example are the manifests required to deploy an application on top of kubernetes.



