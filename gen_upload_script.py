#!/usr/bin/env python3

import os.path
import sys

path = sys.argv[1]
paths = []
for dirpath, _, filenames in os.walk(path):
    for fname in filenames:
        if 'dedup' in fname:
            paths.append(os.path.join(dirpath, fname))

tpl = 's3cmd -c ~/cdr.cfg put {path} s3://memex-fall2016-qpr/hg_{prefix}_{name}'

dirname = os.path.basename(path.rstrip('/'))
script_name = 'upload_{}.sh'.format(dirname)
assert not os.path.exists(script_name)

with open(script_name, 'wt') as f:
    for path in paths:
        print(tpl.format(path=path, prefix=dirname, name=os.path.basename(path)), file=f)
