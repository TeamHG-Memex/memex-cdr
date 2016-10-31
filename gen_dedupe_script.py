#!/usr/bin/env python
import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_folder')
    args = parser.parse_args()
    script_name = '{}.sh'.format(os.path.basename(args.input_folder.rstrip('/')))
    print(script_name)
    assert not os.path.exists(script_name)
    with open(script_name, 'wt') as f:
        print('set -ex', file=f)
        for filename in os.listdir(args.input_folder):
            if filename.endswith('_items.jl.gz'):
                output = filename[:-len('_items.jl.gz')] + '_items_deduped.jl.gz'
                output = os.path.join(args.input_folder, output)
                if not os.path.exists(output):
                    print('./cdr_dedupe.py --redis_prefix "dedup" --input_file {input} --result_file {output}'
                          .format(input=os.path.join(args.input_folder, filename),
                                  output=output),
                          file=f)


if __name__ == '__main__':
    main()
