# JupyterLab 4.1 Extensions with python 3.10 by Examples

The examples currently target **JupyterLab 4.0 or later**.

## Develop by Examples

Start with the [Hello World](hello-world) and then jump to the topic you are interested in.

- [Hello World](hello-world)
- [Toolbar item](toolbar-button)

## Prerequisites

Writing an extension requires basic knowledge of JavaScript, Typescript and potentially Python.

These examples are developed and tested on top of JupyterLab.
You can create a [conda](https://docs.conda.io/en/latest/miniconda.html) environment to get started
after cloning this repository.

```bash
conda env create 
```

> The previous command will use the [environment.yaml](https://github.com/jupyterlab/extension-examples/blob/master/environment.yml) file as requirements for the environment.

## Develop and Use the Examples

### Build and Install one Example

Go to the example directory you want to install, e.g. `cd ./hello-world`, and run the following commands:

```bash
pip install -e .
jupyter labextension develop . --overwrite
```

Rebuild the extension:

```bash
jlpm run build
```

You can now start JupyterLab and check if your extension is working fine:

```bash
jupyter lab
```

### Change the Sources

If you want to develop and iterate on the code, you will need to open 2 terminals.

In terminal 1, go to the extension folder and run the following:

```bash
jlpm watch
```

Then in terminal 2, start JupyterLab with the watch flag:

```bash
jupyter lab --watch
```

From there, you can change your extension source code, it will be recompiled,
and you can refresh your browser to see your changes.


## About JupyterLab

JupyterLab can be used as a platform to combine existing data-science components into a
new powerful application that can be deployed remotely to many users. Some of the higher
level components that can be used are text editors, terminals, notebooks, interactive widgets,
filebrowser, renderers for different file formats that provide access to an enormous ecosystem
of libraries from different languages.

Complementary to these examples, you can rely on the official JupyterLab documentation.

- [Extension Developer Guide](https://jupyterlab.readthedocs.io/en/stable/extension/extension_dev.html)
- [Common Extension Points](https://jupyterlab.readthedocs.io/en/stable/extension/extension_points.html)
- [Astronomy Picture of the Day JupyterLab Extension](https://jupyterLab.readthedocs.io/en/stable/extension/extension_tutorial.html)

