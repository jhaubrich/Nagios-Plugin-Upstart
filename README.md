# Nagios-Upstart

## Overview
This is a *very* simple script to check remote upstart jobs via ssh.

## Installation
In your Nagios plugins diretory run
``` bash
$ git clone <git link>
```

## Usage
Because SSH is used you need to setup passwordless login on the host.
### Install in Nagios
Edit your commands.cfg and add the following

``` build
define command {
    command_name    check_upstart
    command_line    $USER1$/nagios-plugin-upstart/check_upstart.py -H $_HOSTHOST$ -P $_HOSTPORT$ -u $_HOSTUSER$ -j $_HOSTJOB$
}
```

#### Check Upstart Service

```
define service {
    use                     generic-service
    hostgroup_name          Aprature Industries Servers
    service_description     droid_state
    
    check_command           check_upstart
    _host                   glados
    _port                   2202
    _user                   wheatley
    _job                    atlas_pbody
}
```