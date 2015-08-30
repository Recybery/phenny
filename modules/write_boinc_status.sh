#! /bin/bash

boinccmd --get_tasks | grep  'name\|project URL\|scheduler state\|fraction done' | grep -v WU | head -n 12 > boincStatus.out
