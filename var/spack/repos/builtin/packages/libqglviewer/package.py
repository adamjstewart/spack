# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


class Libqglviewer(QMakePackage):
    """libQGLViewer is a C++ library based on Qt that eases the creation of
    OpenGL 3D viewers."""

    homepage = "http://libqglviewer.com/"
    url      = "http://libqglviewer.com/src/libQGLViewer-2.7.2.tar.gz"

    version('2.7.2', sha256='e2d2799dec5cff74548e951556a1fa06a11d9bcde2ce6593f9c27a17543b7c08')

    # http://libqglviewer.com/installUnix.html

    depends_on('qt+opengl')
    depends_on('freeglut', when='^qt@:3.0')

    def patch(self):
        if self.spec.satisfies('platform=darwin'):
            # Build .dylib instead of Framework
            filter_file('!staticlib: CONFIG *= lib_bundle', '',
                        join_path('QGLViewer', 'QGLViewer.pro'))

    def qmake_args(self):
        args = ['PREFIX=' + self.prefix]

        if self.spec.satisfies('platform=darwin'):
            args.extend(['-spec', 'macx-g++'])

        return args
