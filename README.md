<h1 align="center">Cisco Appdynamics Collector</h1>  

<br/>  
<div align="center" style="display:flex;">  
  <img width="245" src="https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/appdynamics-icon.svg">
  <p> 
    <br>
    <img alt="Version"  src="https://img.shields.io/badge/version-0.1.0-blue.svg?cacheSeconds=2592000"  />    
    <a href="https://www.apache.org/licenses/LICENSE-2.0"  target="_blank"><img alt="License: Apache 2.0"  src="https://img.shields.io/badge/License-Apache 2.0-yellow.svg" /></a> 
  </p> 
</div> 

#### Plugin to collect Cisco Appdynamics Cloud Services


> Cloudforet's [plugin-appdynamics-cloud-services](https://github.com/cloudforet-io/plugin-appdynamics-inven-collector) is a convenient tool to 
get cloud service data from Appdynamics Cloud Services. 


Find us also at [Dockerhub](https://hub.docker.com/r/spaceone/plugin-appdynamics-inven-collector)
> Latest stable version : 0.1.0

Please contact us if you need any further information. 
<admin@cloudforet.io>


## Contents

| Cloud Service Type | Cloud Service                                       |
|--------------------|-----------------------------------------------------|
| Application        | [Application](#application)                         |
   
---
## SETTING
You should insert information about account in Cloudforet's **Service Account** initially.
* Base Information
	* `account_name`

* Credentials
	* `Client ID`
	* `Client Secret`
	* `Controller`
---

## Service list

The following is a list of services being collected and service code information.

| No. | Service name            | Service Code                         |
|-----|-------------------------|--------------------------------------|
| 1   | Application             | Cisco.Application/applicaiton        |
---

## Authentication Overview
Registered service account on Cloudforet must have certain permissions to collect cloud service data 
Please, set authentication privilege for followings:

### Custom roles for collecting Appdynamics cloud resources 
Cloudforet Appdynamics collector requires several privileges for collecting resources. <br>
Please create custom roles in Appdynamics portal, and assign following roles to Cloudforet Appdynamics collector apps before collect resources.

## Options

### Cloud Service Type : Specify what to collect

If cloud_service_types is added to the list elements in options, only the specified cloud service type is collected.
By default, if cloud_service_types is not specified in options, all services are collected.

The cloud_service_types items that can be specified are as follows.

<pre>
<code>
{
    "cloud_service_types": [
        'Application',
    ]
}
</code>
</pre>

How to update plugin information using spacectl is as follows.
First, create a yaml file to set options.

<pre>
<code>
> cat update_collector.yaml
---
collector_id: collector-xxxxxxx
options:
  cloud_service_types:
    - Application
</code>
</pre>

Update plugin through spacectl command with the created yaml file.

<pre><code>
> spacectl exec update_plugin inventory.Collector -f update_collector.yaml
</code></pre>

---

## Release Note
### Ver 0.1.0
* Add ```Application```


