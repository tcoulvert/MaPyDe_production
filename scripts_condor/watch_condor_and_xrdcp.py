# Stdlib packages
import argparse
import copy
import json
import logging
import os
import subprocess
import sys
import time

################################


parser = argparse.ArgumentParser(description="Checks for completed condor jobs and transfers to new location")
parser.add_argument(
    "local_directory", 
    help="Local directory to watch for files being transferred out of HTCondor jobs"
)
parser.add_argument(
    "remote_directory", 
    help="Remote directory to transfer files to"
)
parser.add_argument(
    "--extension",
    type=str,
    default='',
    help="Extension of files to search for, default is everything"
)
parser.add_argument(
    "--keep_local",
    action='store_true',
    help="Saves local files, default behavior deletes local files"
)
parser.add_argument(
    "--sleep",
    type=int,
    default=60,
    help="Seconds to sleep between checks for new files"
)
parser.add_argument(
    "--verbose",
    action='store_true',
    help="Prints out every command run"
)

################################


args = parser.parse_args()
LOCAL_DIRECTORY = args.local_directory
REMOTE_DIRECTTORY = args.remote_directory
KEEP_LOCAL = args.keep_local
SLEEP = args.sleep
VERBOSE = args.verbose

################################


def main():

    transferred_files_set = set()
    removed_files_set = set()

    KeyboardInterruptBool = True
    while KeyboardInterruptBool:
        print('='*60)

        if not os.path.exists(LOCAL_DIRECTORY): 
            print(f"No directory yet, sleeping for {SLEEP} seconds..."); time.sleep(SLEEP); continue

        files = [
            os.path.join(LOCAL_DIRECTORY, file) for file in os.listdir(LOCAL_DIRECTORY) 
            if os.path.isfile(os.path.join(LOCAL_DIRECTORY, file)) 
            and file not in (transferred_files_set | removed_files_set)
        ]

        if len(files) == 0:
            print(f"No new files yet, sleeping for {SLEEP} seconds..."); time.sleep(SLEEP); continue

        print('-'*60)
        print(f"Found files!! Transfering files.")
        for file in files:
            try:
                if VERBOSE: print(f"     xrdcp {file} {os.path.join(REMOTE_DIRECTTORY, file.split('/')[-1])}")
                if os.system(f"xrdcp {file} {os.path.join(REMOTE_DIRECTTORY, file.split('/')[-1])}") in [0, 12800]:
                    transferred_files_set.add(file)
            except KeyboardInterrupt: KeyboardInterruptBool = False; break

        print('-'*60)
        print(f"Removing transferred files from local directory.")
        for file in transferred_files_set:
            try:
                if VERBOSE: print(f"     rm {file}")
                os.system(f"rm {file}")
                removed_files_set.add(file)
            except KeyboardInterrupt: KeyboardInterruptBool = False; break
        transferred_files_set -= removed_files_set
        
        print('-'*60)
        print(f"Sleeping for {SLEEP} seconds...")
        time.sleep(SLEEP)

if __name__ == "__main__":
    main()