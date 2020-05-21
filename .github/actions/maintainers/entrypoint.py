#!/usr/bin/env python3
#
# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

"""Maintainer action.

This action checks which packages have changed in a PR, and checks
whether or not these packages have maintainers.
"""

import json
import os
import subprocess


def spack(*args):
    """Run the spack executable with arguments, and return the output split.

    This does just enough to run `spack pkg` and `spack maintainers`, the
    two commands used by this action.
    """
    github_workspace = os.environ['GITHUB_WORKSPACE']
    spack = os.path.join(github_workspace, 'bin', 'spack')
    output = subprocess.run([spack] + list(args), stdout=subprocess.PIPE)
    return output.stdout.decode('utf-8').split()


def main():
    event_path = os.environ['GITHUB_EVENT_PATH']

    with open(event_path) as f:
        data = json.load(f)

    # Get data from the event payload
    pr_data = data['pull_request']
    base_branch_name = pr_data['base']['ref']
    author = pr_data['user']['login']

    # Get a list of packages that this PR modified
    changed_pkgs = spack(
        'pkg', 'changed', '--type', 'ARC', base_branch_name + '...')

    # Get maintainers for all modified packages
    packages_with_maintainers = []
    packages_without_maintainers = []
    maintainers = set()
    for pkg in changed_pkgs:
        pkg_maintainers = set(spack('maintainers', pkg))
        if pkg_maintainers:
            packages_with_maintainers.append(pkg)
            maintainers |= pkg_maintainers
        else:
            packages_without_maintainers.append(pkg)

    # No need to ask the author to review their own PR
    maintainers -= set([author])

    # Return outputs so that later GitHub actions can access them
    print('::set-output name=packages-with-maintainers::"{}"'.format(
        ' '.join(packages_with_maintainers)))
    print('::set-output name=packages-without-maintainers::"{}"'.format(
        ' '.join(packages_without_maintainers)))
    print('::set-output name=maintainers::"{}"'.format(' '.join(maintainers)))
    print('::set-output name=author::{}'.format(author))


if __name__ == "__main__":
    main()
