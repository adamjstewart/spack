# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class LsdSlamNoros(CMakePackage):
    """LSD-SLAM: Large-Scale Direct Monocular SLAM.

    This is a fork of LSD-SLAM that does not require ROS to compile."""

    homepage = "https://github.com/aivijay/lsd_slam_noros"
    git      = "https://github.com/aivijay/lsd_slam_noros.git"

    version('master', branch='master')

    depends_on('cmake@2.8.9:', type='build')
    depends_on('boost+system+thread+atomic')
    depends_on('opencv@2.2:')
    depends_on('g2o')
    depends_on('freeglut')
    depends_on('glew')

    patch('cmake.patch')
