import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

function activate(app: JupyterFrontEnd) {
  console.log('The JupyterLab v4.x main application:', app);
}

/**
 * Initialization data for the @jlab-examples/hello-world extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: '@jlab-examples/hello-world:plugin',
  description: 'Minimal JupyterLab extension.',
  autoStart: true,
  activate
};

export default plugin;
