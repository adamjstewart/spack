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
    depends_on('g2o')
    depends_on('freeglut')
    depends_on('glew')

    def patch(self):
        ff = FileFilter(join_path('cmake', 'LsdSlamDependencies.cmake'))
        ff.filter('find_package(G2O REQUIRED)',
                  'find_package(g2o CONFIG REQUIRED)', string=True)
        ff.filter('list(APPEND LsdSlam_EXTERNAL_LIBS ${G2O_LIBRARIES})',
'''
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::freeglut_minimal)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::stuff)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::opengl_helper)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::core)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::g2o_cli_library)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::g2o_hierarchical_library)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::g2o_simulator_library)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::viewer_library)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::types_data)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::types_slam2d)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::types_slam3d)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::types_sba)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::types_sim3)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::types_icp)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::types_sclam2d)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::types_slam2d_addons)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::types_slam3d_addons)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::solver_pcg)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::solver_dense)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::solver_structure_only)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::solver_csparse)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::csparse_extension)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::solver_slam2d_linear)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::solver_cholmod)
list(APPEND LsdSlam_EXTERNAL_LIBS g2o::solver_eigen)
''', string=True)

        ff = FileFilter('CMakeLists.txt')
        ff.filter('cmake_minimum_required(VERSION 2.8.9)',
                  'cmake_minimum_required(VERSION 3.10.2)', string=True)
        ff = FileFilter(join_path('apps', 'CMakeLists.txt'))
        ff.filter('cmake_minimum_required(VERSION 2.8.7)',
                  'cmake_minimum_required(VERSION 3.10.2)', string=True)
        ff = FileFilter(join_path('apps', 'slam', 'CMakeLists.txt'))
        ff.filter('cmake_minimum_required(VERSION 2.8.9)',
                  'cmake_minimum_required(VERSION 3.10.2)', string=True)
        ff = FileFilter(join_path('lsd_slam', 'CMakeLists.txt'))
        ff.filter('cmake_minimum_required(VERSION 2.8.9)',
                  'cmake_minimum_required(VERSION 3.10.2)', string=True)
        #ff.filter('target_link_libraries(${lib_target} ${LsdSlam_ALL_LIBRARIES})',
        #          'find_package(g2o CONFIG REQUIRED)\ntarget_link_libraries(${lib_target} ${LsdSlam_ALL_LIBRARIES})', string=True)

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
