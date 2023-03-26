import argparse
import glob
import re
import os
import time
from github3 import login as ghlogin

github = ghlogin('', '', os.environ['GITHUB_TOKEN'])

# latest version of vaultwarden
server_repository = github.repository('dani-garcia', 'vaultwarden')
server_release = server_repository.latest_release()
server_version = server_release.tag_name
server_version_clean = server_version.replace('v', '')

# latest version of bw_web_builds
web_repository = github.repository('dani-garcia', 'bw_web_builds')
web_release = web_repository.latest_release()
web_version = web_release.tag_name
web_version_clean = web_version.replace('v', '')

# timestamp for the debian changelog
release_timestamp = time.strftime('%a, %e %b %Y %H:%M:%S %z')


print('Latest upstream server release: %s' % server_version_clean)
print('Latest upstream web vault release: %s' % web_version_clean)


any_updates = False

# update web vault changelog
with open('vaultwarden-web-vault/debian/changelog', 'r') as f:
    web_changelog = f.read()
m = re.match('vaultwarden-web-vault \(([0-9a-z.]+)-([0-9]+)\)', web_changelog)
assert m
current_web_version = m.group(1)
web_version_deb = '%s-%s' % (m.group(1), m.group(2))
print('vaultwarden-web-vault: current version %s' % current_web_version)
if current_web_version != web_version_clean:
    any_updates = True
    print('Web vault needs update')
    with open('vaultwarden-web-vault/debian/changelog', 'w') as f:
        f.write('vaultwarden-web-vault (%s-1) unstable; urgency=medium\n' % web_version_clean)
        f.write('\n')
        f.write('  * Update to upstream version %s.\n' % web_version)
        f.write('\n')
        f.write(' -- Gijs van Tulder <gvtulder@gmail.com>  %s\n' % release_timestamp)
        f.write('\n')
        f.write(web_changelog)

    # set deb version
    web_version_deb = '%s-1' % web_version_clean


# update server changelog
with open('vaultwarden/debian/changelog', 'r') as f:
    server_changelog = f.read()
m = re.match('vaultwarden \(([0-9a-z.]+)-([0-9]+)\)', server_changelog)
assert m
current_server_version = m.group(1)
server_version_deb = '%s-%s' % (m.group(1), m.group(2))
print('vaultwarden: current version %s' % current_server_version)
if current_server_version != server_version_clean:
    any_updates = True
    print('Server needs update')
    with open('vaultwarden/debian/changelog', 'w') as f:
        f.write('vaultwarden (%s-1) unstable; urgency=medium\n' % server_version_clean)
        f.write('\n')
        f.write('  * Update to upstream version %s.\n' % server_version)
        f.write('  * Require upstream version %s.\n' % web_version)
        f.write('\n')
        f.write(' -- Gijs van Tulder <gvtulder@gmail.com>  %s\n' % release_timestamp)
        f.write('\n')
        f.write(server_changelog)

    # update server control, require latest web vault version
    with open('vaultwarden/debian/control', 'r') as f:
        server_control = f.read()
    server_control = re.sub('vaultwarden-web-vault \(>= [0-9a-z.]+\)',
                            'vaultwarden-web-vault (>= %s)' % web_version_clean,
                            server_control)
    with open('vaultwarden/debian/control', 'w') as f:
        f.write(server_control)

    # set deb version
    server_version_deb = '%s-1' % server_version_clean


# write GitHub environment variables
with open(os.getenv('GITHUB_ENV', 'github.env'), 'w') as f:
    f.write('VW_SERVER_VERSION=%s\n' % server_version)
    f.write('VW_WEB_VERSION=%s\n' % web_version)
    f.write('VW_SERVER_VERSION_CLEAN=%s\n' % server_version_clean)
    f.write('VW_WEB_VERSION_CLEAN=%s\n' % web_version_clean)
    f.write('VW_SERVER_VERSION_DEB=%s\n' % server_version_deb)
    f.write('VW_WEB_VERSION_DEB=%s\n' % web_version_deb)
    if any_updates:
        f.write('VW_HAS_UPDATE=true\n')

