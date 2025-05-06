The JupyterLab Interface
========================

By default, you will get the web-based user interface for Project Jupyter that is called `JupyterLab <https://jupyterlab.readthedocs.io/en/stable/>`_.

Menu Bar
--------

The menu bar at the top of JupyterLab has top-level menus that expose actions available in JupyterLab with
their keyboard shortcuts. The default menus are:

- **File**: actions related to files and directories
- **Edit**: actions related to editing documents and other activities
- **View**: actions that alter the appearance of JupyterLab
- **Run**: actions for running code in different activities such as notebooks and code consoles
- **Kernel**: actions for managing kernels, which are separate processes for running code
- **Tabs**: a list of the open documents and activities in the dock panel
- **Settings**: common settings and an advanced settings editor
- **Help**: a list of JupyterLab and kernel help links

Left Sidebar
------------

The left sidebar contains a number of commonly-used tabs, such as a file browser, a list of running
kernels and terminals, the command palette, and a list of tabs in the main work area:



If you move your mouse on the other icon of this left sidebar, a short information is given on its functionality.

If you click on the "stop button" icon, you can see what is currently running on your server and you can click on
"SHUT DOWN" to stop a running Python notebook or Terminal.

Start a new Terminal
--------------------

Similarly, you can start a new Terminal by clicking on "Terminal" in the Launcher.


Tips
----
 If the **Launcher** tab does not exist
 anymore in your JupyterLab, you can start a new one in "**File** --> **New Launcher**".



Create a new python 3 notebook
------------------------------

Go back to the **File Browser** left sidebar tab and in the launcher select **Python 3** under the Notebook
section:


By default, your new notebook is named as "**Untitled.ipynb**":

- **ipynb** is the extension for any Jupyter notebook and you should make sure all your notebooks get this extension (otherwise it is not recognized as a Jupyter notebook)
- you can rename your jupyter notebook with the tab "File --> Rename Notebook..." or
  right click on its name.

Using debugger
~~~~~~~~~~~~~~

If you want to see the list variables, their values, function callbacks, sett breakpoints. You can eneable a debugger in your notebook.

To do that: click on the little bug button in the headder of your. Where kernels, play etc is lockated:

.. image:: img/bug-button.png
   :width: 600
   :alt: bug button

When you click on it, it will change its color to orange and the debugger panel on the right will open. You can always collapse the panel and expand it back.

.. image:: img/bug-tab.png
   :width: 600
   :alt: bug tab
