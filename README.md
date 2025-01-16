# Search DuckDuckGo 


## A general idea

This video (click on below image to play) provides a basic idea: 

[![SDG - SMOTE](./img/SDG_SMOTE.png)](https://www.youtube.com/watch?v=iVFv1ewVU20)

----
## Table of Contents
1. [Requirements](#requirements)
2. [Parameters](#parameters)
   1. [Input Parameters](#input-parameters)
   2. [Configuration](#configuration)
   3. [Output Specifications](#output-specifications)
3. [Run-time Control](#run-time-control)
4. [Documentation](#documentation)
5. [SAS Program](#sas-program)
6. [Installation and Usage](#installation--usage)
7. [Created/Contact](#createdcontact)
8. [Change Log](#change-log)
----
## Requirements

1. A SAS Viya 4 environment, preferably monthly stable 2024.12 or later

2. Python is configured for use from within the Viya environment and SAS Studio




-----
## Parameters
----
### Input Parameters

1. 
----
### Configuration 

1. 

----
### Output Specification


1. 

----
## Run-time Control

Note: Run-time control is optional.  You may choose whether to execute the main code of this step or not, based on upstream conditions set by earlier SAS programs.  This includes nodes run prior to this custom step earlier in a SAS Studio Flow, or a previous program in the same session.

Refer this blog (https://communities.sas.com/t5/SAS-Communities-Library/Switch-on-switch-off-run-time-control-of-SAS-Studio-Custom-Steps/ta-p/885526) for more details on the concept.

The following macro variable,
```sas
_ddgs_run_trigger
```

will initialize with a value of 1 by default, indicating an "enabled" status and allowing the custom step to run.

If you wish to control execution of this custom step, include code in an upstream SAS program to set this variable to 0.  This "disables" execution of the custom step.

To "disable" this step, run the following code upstream:

```sas
%global _ddgs_run_trigger;
%let _ddgs_run_trigger =0;
```

To "enable" this step again, run the following (it's assumed that this has already been set as a global variable):

```sas
%let _ddgs_run_trigger =1;
```


IMPORTANT: Be aware that disabling this step means that none of its main execution code will run, and any  downstream code which was dependent on this code may fail.  Change this setting only if it aligns with the objective of your SAS Studio program.

----
## Documentation

1. PyPi page for [duckduckgo-search](https://pypi.org/project/duckduckgo-search/) 



----
## SAS Program

Refer [here](./extras/Search%20from%20DuckDuckGo.sas) for the SAS program used by the step.  You'd find this useful for situations where you wish to execute this step through non-SAS Studio Custom Step interfaces such as the [SAS Extension for Visual Studio Code](https://github.com/sassoftware/vscode-sas-extension), with minor modifications. 

----
## Installation & Usage

- Refer to the [steps listed here](https://github.com/sassoftware/sas-studio-custom-steps#getting-started---making-a-custom-step-from-this-repository-available-in-sas-studio).

----
## Created/contact:  

- Sundaresh Sankaran (sundaresh.sankaran@sas.com)
- Mallika Dey (dey.mallika@gmail.com)

----
## Change Log

* Version 1.0 (16JAN2025) 
    * Initial version