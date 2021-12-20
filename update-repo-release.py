import argparse
import glob
import os
from github3 import login as ghlogin

parser = argparse.ArgumentParser()
parser.add_argument('--target-owner', metavar='RELEASE', required=True)
parser.add_argument('--target-project', metavar='RELEASE', required=True)
parser.add_argument('--target-release', metavar='RELEASE', required=True)
parser.add_argument('--source-dir', metavar='DIR', required=True)
args = parser.parse_args()

release = ghlogin('', '', os.environ['GITHUB_TOKEN']).repository(args.target_owner, args.target_project).release_from_tag(args.target_release)
files = [os.path.basename(filename)
         for filename in glob.glob(os.path.join(args.source_dir, '*'))
         if os.path.isfile(filename)]
existing_assets = {}
for asset in release.assets():
    existing_assets[asset.name] = asset
for filename in glob.glob(os.path.join(_from, '*')):
    if os.path.isfile(filename):
        name = os.path.basename(filename)
        print('->', name)
        if name in existing_assets:
            # always delete because upload_asset does not replace
            print('  delete old version')
            existing_assets[name].delete()
        print('  upload new version')
        with open(filename, 'rb') as f:
            release.upload_asset('application/octet-stream', name, f)
