# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTorchScatter(PythonPackage):
    """This package consists of a small extension library of
    highly optimized sparse update (scatter and segment)
    operations for the use in PyTorch, which are missing in the
    main package."""

    homepage = "https://github.com/rusty1s/pytorch_scatter"
    pypi = "torch-scatter/torch_scatter-2.1.2.tar.gz"

    license("MIT")

    version("2.1.2", sha256="69b3aa435f2424ac6a1bfb6ff702da6eb73b33ca0db38fb26989c74159258e47")
    version(
        "2.0.5",
        sha256="148fbe634fb9e9465dbde2ab337138f63650ed8abbac42bb3f565e3fe92e9b2f",
        deprecated=True,
    )

    depends_on("python", type=("build", "link", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-torch", type=("build", "link", "run"))

    # Historical dependencies
    depends_on("py-pytest-runner", type="build", when="@:2.0.7")

    def setup_build_environment(self, env):
        if self.spec.satisfies("@2.0.6:"):
            if "+cuda" in self.spec["py-torch"]:
                env.set("FORCE_CUDA", 1)
                env.set("FORCE_ONLY_CUDA", 0)
                env.set("FORCE_ONLY_CPU", 0)
            else:
                env.set("FORCE_CUDA", 0)
                env.set("FORCE_ONLY_CUDA", 0)
                env.set("FORCE_ONLY_CPU", 1)
        else:
            if "+cuda" in self.spec["py-torch"]:
                env.set("FORCE_CUDA", 1)
                env.set("FORCE_CPU", 0)
            else:
                env.set("FORCE_CUDA", 0)
                env.set("FORCE_CPU", 1)
