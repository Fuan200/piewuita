#!/usr/bin/env python3
# scripts/piewuita-cli

import argparse
from piewuita.create_project import create_project

def main():
    parser = argparse.ArgumentParser(description="Create a new project in Python..")
    parser.add_argument(
        "-n","--name",
        required=True,
        help="project name"
    )
    parser.add_argument(
        "-m","--modules",
        required=False,
        nargs="*",
        default=[],
        help="list of modules to install with pip"
    )
    
    args = parser.parse_args()
    create_project(args.name, args.modules)

if __name__ == '__main__':
    main()