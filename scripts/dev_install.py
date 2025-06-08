# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import subprocess
from pathlib import Path
from typing import Optional


def execute(cmd: str, cwd: Optional[Path] = None) -> None:
    subprocess.run(cmd.split(" "), check=True, cwd=cwd)


def install_dev() -> None:
    install_build_deps = "python -m pip install jupyterlab>=4,<5"
    install_js_deps = "jlpm install"

    python_package_prefix = "packages"
    python_packages = ["hello-world", "toolbar-button", "reverse-proxy-ext"]

    execute(install_build_deps)
    execute(install_js_deps)

    for py_package in python_packages:
        real_package_name = py_package.replace("-", "_")
        execute(f"pip uninstall {real_package_name} -y")
        execute(f"pip install -e {python_package_prefix}/{py_package}[test]")

        # List of server extensions
        if py_package in ["reverse-proxy-extension"]:
            execute(f"jupyter server extension enable {real_package_name}")

        # List of jupyterlab extensions
        if py_package in ["jupyterlab_examples_hello_world", "jupyterlab_examples_toolbar_button"]:
            execute(
                f"jupyter labextension develop --overwrite {python_package_prefix}/{py_package} --overwrite"
            )


if __name__ == "__main__":
    install_dev()
