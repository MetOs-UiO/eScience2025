Setting up remotes
==================


Since we are working with two repositories: your fork and the repository you forked from, you might want to set up your local repo to see them both.
In order to do that you would have to use terminal even if you use GUI for committing/pushing.

In git, remotes are repositories somewhere on the server (gitlab/github) that are not present locally on your machine.
When you clone a repository and create a branch you generally want your branch to track some other branch on one of the remotes (usually with the same name).

That's why you need to do ``git push --set-origin <remote-name> <branch-name>`` whe you first push a branch you have created locally with ``git switch -c <branch-name>``.

Adding remotes
~~~~~~~~~~~~~~

Here we will add an ``upstream`` repository to the clone of your fork.
Assuming you have cloned your fork and are currently in the folder that contains it. Open a terminal:

.. code-block:: bash

  git remote add upstream <url-of-the-repo-you-forked-from>
  #check if the remote is added
  git remote -v
  #get all the branches/tags from newly added remote:
  git fetch upstream

Now, you have successfully added the upstream remote to your clone.

.. note::
  If you are using GUI, in the git tab when you click on branches, you will see branches from all the remotes you've in your clone ``remote-name/branch-name`` your local branches will not have ``remote-name/`` prefix.

.. note::

  To update your clone with any changes on the remotes (new branches, tags, commits) you might want to regularly run ``git fetch --all`` or for a specific remote: ``git fetch <remote-name>``.

Checking out remote branches
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you have configured the remotes in your clone you can check out the heads of specific branches from those remotes or make local branches to track remote branches:

.. code-block:: bash

  # this will show you all the remote branches:
  git branch -r
  # to see ALL the branches local/remote:
  git branch -v -a
  # check out the head of a remote branch
  git checkout <remote-name/branch-name>
  # create a new branch that will originate
  git switch -c <new-branch> # note, when you push you will need to --set-origin
  # to create a new local branch that will TRACK already existing remote branch
  git switch -c <branch-name> <remote-name>/<branch-name>

  # to delete a local branch
  git -d <branch-name>


.. tip::

  If you have local changes and you want to switch/make a new branch you can use ``git stash`` to get to the latest commit of the branch you are on.
  The changes will stay in the stash and you can use it later. To permanently ``git reset --hard``.