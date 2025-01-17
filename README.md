# Search from DuckDuckGo
This custom step searches the internet using the DuckDuckGo search engine for websites or news related to a search term provided by the user, and outputs results to a SAS dataset.
## A general idea

----
## Table of Contents

----
## Requirements

-----
## Parameters

-----
## Run-time Control
Note: Run-time control is optional.  You may choose whether to execute the main code of this step or not, based on upstream conditions set by earlier SAS programs.  This includes nodes run prior to this custom step earlier in a SAS Studio Flow, or a previous program in the same session.

Refer this blog (https://communities.sas.com/t5/SAS-Communities-Library/Switch-on-switch-off-run-time-control-of-SAS-Studio-Custom-Steps/ta-p/885526) for more details on the concept.
The following macro variable,
```sas
ddgs_run_trigger
```
will initialize with a value of 1 by default, indicating an 'enabled' status and allowing the custom step to run.
If you wish to control execution of this custom step, include code in an upstream SAS program to set this variable to 0.  This 'disables' execution of the custom step.
To 'disable' this step, run the following code upstream:
```sas
%global ddgs_run_trigger;
%let ddgs_run_trigger = 0;
```
To 'enable' this step again, run the following (it's assumed that this has already been set as a global variable):
```sas
%let ddgs_run_trigger = 1;
```
IMPORTANT: Be aware that disabling this step means that none of its main execution code will run, and any  downstream code which was dependent on this code may fail.  Change this setting only if it aligns with the objective of your SAS Studio program.
-----
## Documentation

-----
## SAS Program

Refer [here]() for the SAS program used by the step.  You'd find this useful for situations where you wish to execute this step through non-SAS Studio Custom Step interfaces such as the [SAS Extension for Visual Studio Code](https://github.com/sassoftware/vscode-sas-extension), with minor modifications.
-----
## Installation & Usage

- Refer to the [steps listed here](https://github.com/sassoftware/sas-studio-custom-steps#getting-started---making-a-custom-step-from-this-repository-available-in-sas-studio).
----
## Created/contact:

----
## Change Log

