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

    depends_on('cmake@2.8.9:3.11', type='build')
    depends_on('boost+system+thread+atomic')
    depends_on('opencv@2.2:')
    depends_on('g2o build_type=Debug')
    depends_on('freeglut')
    depends_on('glew')

    #def patch(self):
    #    ff = FileFilter(join_path(
    #        'cmake', 'LsdSlamDependencies_Config.cmake.in'))
    #    ff.filter(r'set\(BOOST_ROOT .*\)',
    #              'set(BOOST_ROOT {0})'.format(self.spec['boost'].prefix))
    #    ff.filter(r'set\(OpenCV_DIR .*\)',
    #              'set(OpenCV_DIR {0})'.format(self.spec['opencv'].prefix))
    #    ff.filter(r'set\(G2O_ROOT .*\)',
    #              'set(G2O_ROOT {0})'.format(self.spec['g2o'].prefix))
    #    ff.filter(r'set\(GLUT_INCLUDE_DIR .*\)',
    #              'set(GLUT_INCLUDE_DIR {0})'.format(
    #                  self.spec['freeglut'].headers.directories[0]))
    #    ff.filter(r'set\(GLEW_INCLUDE_DIR .*\)',
    #              'set(GLEW_INCLUDE_DIR {0})'.format(
    #                  self.spec['glew'].headers.directories[0]))

    #def cmake_args(self):
    #    return ['-DLsdSlam_USE_MANUAL_CONFIG_FILE=TRUE']
