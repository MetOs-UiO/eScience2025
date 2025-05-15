Basic setup
===========


1. Fork projects repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. |fbutton| image:: img/fork_button.png

Before you start working on your group projects. You should fork `eScience2025-projects repo <https://github.com/MetOs-UiO/eScience2025-projects>`_.
To make a fork, go to the repo page. There you will see a ``fork`` button |fbutton|. Click on it to create a copy of this repository in your github user space.
**Uncheck** ``Copy the main branch only`` if you do not want to miss on other branches currently on the original repo.

.. image:: img/fork-create.png
   :width: 700
   :alt: Fork Creation page

2. Get GitHub Access token
~~~~~~~~~~~~~~~~~~~~~~~~~~

From `GitHub documentation <https://docs.github.com/en/enterprise-server@3.9/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>`_.

- Go to Github.
- Click on your your profile image in the top-right.
- Click ``Settings``
- Click ``Developer Settings``
- Click ``Personel access tokens->Tokens (classic)``
- Click ``Generate new token``
- Click ``Generate new token (classic)``
- Authenticate
- Make a note
- Click on ``repo``, ``user``, ``admin:org-read``
- Click ``generate``
- Save token somewhere, treat it as a password

3. Setup git and clone on jupyterhub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After you have forked the projects repo you should login to `Jupyterhub <https://escience2025.craas2.sigma2.no>`_.

There, you would need to clone your fork and create your first branch you would be working on. See :doc:`Starting with git on the jupyterhub <../git_integration/git_jlab>`.

.. attention::
  :class: toggle


  If you have already accessed `test sever <https://test-escience2025.craas2.sigma2.no>`_, you should move to `<https://escience2025.craas2.sigma2.no>`_.
  Test server is only there for testing and will get shutdown.

- :doc:`Open terminal <../common/terminal>`.
- Type this commands filling in your **github** username and email (without ``<>``):

  .. code-block:: bash

    git config --global user.name "<your_username>"
    git config --global user.email "<your_email>"

- Clone **your fork** of  projects repository:

  .. code-block:: bash

    git clone https://github.com/<your_username>/eScience2025-projects

- Go into your clone:

  .. code-block:: bash

    cd eScience2025-projects

- Add upstream repository (See :doc:`Setting up remotes <../git_integration/remotes>`):
     - to check if it's already added do ``git remote -v``

  .. code-block:: bash

    git remote add upstream https://github.com/MetOs-UiO/eScience2025-projects
    git fetch --all

- Make your first branch with a sensible name (what are you going to work on). Below you first checkout the current state of the upstream (the main repo, not your fork), and then add a branch (which will then be up to date with the main branch on the main repo) and switch to it, and finally you push your new local branch to the remote origin (which is your fork).

  .. code-block:: bash

    git checkout upstream/main
    git switch -c <sensible-branch-name>
    git push origin <sensible-branch-name>


.. note::
    If you do not wish to type your token to authenticate every time you fetch/pull/push:

    .. code-block:: bash

          # activate pangeo-notebook conda environment
          source activate pangeo-notebook
          # pipe your token into github login command
          echo "<your-token-here>"  | gh auth login --with-token
          # check if you are logged in
          gh auth status

    If you switch terminal/restart your instance, you might have to activate environment and login again.

    .. attention::

        If github still asks for credentials, even if you did ``gh auth login``:

        .. code-block:: bash

            gh auth refresh
            # will ask for yes. It will give you a OTP for github.
            # got to https://github.com/login/device,
            # since we do not have the browser within jupyterlab
            # login, enter OTP
            gh auth status


4. Sharing your work within the group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Within your fork, you should put all your code in your ``group#`` folder.

When you need to share your work with the others within your group you need to make a :doc:`Pull Request <../git_integration/github-work>` to the `upstream repo <https://github.com/MetOs-UiO/eScience2025-projects>`_ ``main`` branch.

After a Teaching assistant responsible for you group has merged your PR to ``upstream/main`` other members of your group can pull these changes into branches on their forks to work on.

In addition, you will most likely want to create new branches based on the updated ``upstream/main``. See :doc:`Setting up remotes <../git_integration/remotes>`.
