#!/usr/bin/env python2

"""
Allot of this was copied from a MongoDB script I found.
https://github.com/mzupan/nagios-plugin-mongodb/blob/master/check_mongodb.py

USAGE
=====

see the README.md
"""
# Nagios exit states
# 0 = ok
# 1 = warn
# 2 = crit
# 3 = unknown
from __future__ import print_function
import sys
import optparse
from subprocess import check_output

def main():
    p = optparse.OptionParser(conflict_handler="resolve", description="This Nagios plugin checks the health of upstart jobs.")

    p.add_option('-H', '--host', action='store', type='string', dest='host', default='127.0.0.1', help='The hostname to connect to.')
    p.add_option('-P', '--port', action='store', type='int', dest='port', default=22, help='The ssh port to use.')
    p.add_option('-u', '--user', action='store', type='string', dest='user', default=None, help='The username you want to login as')
    p.add_option('-p', '--pass', action='store', type='string', dest='passwd', default=None, help='The password you want to use for that user')
    p.add_option('-j', '--job', action='store', type='string', dest='job', default=None, help='The upstart job to check.')

    options, arguments = p.parse_args()

    try:
        status = check_output("ssh {user}@{host} -C 'status {job}'".format(**options.__dict__), shell=True)
    except:
        # ssh command failed, job unknown, bad host, etc.
        print(options.job, "state UNKNOWN")
        sys.exit(3)  # 3 = Unknown

    if 'start/running' in status:
        print(options.job, "is running")
        sys.exit(0)  # 0 = ok
    else:
        # anything else is critical: stopping, killed, pre-stop, waiting, etc
        print(options.job, "is CRITICAL.")
        sys.exit(2) # 2 = crit


if __name__ == '__main__':
    main()