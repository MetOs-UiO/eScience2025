Resolving merge/rebase conflicts
================================

Sometimes when you do ``git status`` after ``git fetch`` you can see that the branches you are diverging.

.. code-block:: bash

    user@machine:~/escience2025-projects$ git status
    On branch pr-test
    Your branch and 'origin/pr-test' have diverged,
    and have 1 and 1 different commits each, respectively.
    (use "git pull" if you want to integrate the remote branch with yours)

    nothing to commit, working tree clean


In this case you need to pull from the remote branch first before you push and resolve potential conflicts, if you try to pull, you will get this error:

.. code-block:: bash

    hint: You have divergent branches and need to specify how to reconcile them.
    hint: You can do so by running one of the following commands sometime before
    hint: your next pull:
    hint:
    hint:   git config pull.rebase false  # merge
    hint:   git config pull.rebase true   # rebase
    hint:   git config pull.ff only       # fast-forward only
    hint:
    hint: You can replace "git config" with "git config --global" to set a default
    hint: preference for all repositories. You can also pass --rebase, --no-rebase,
    hint: or --ff-only on the command line to override the configured default per
    hint: invocation.
    fatal: Need to specify how to reconcile divergent branches.

You can can follow the hints, f.e. if you do ``git pull --no-rebase``:

.. code-block:: bash

    user@machine:~/escience2025-projects$ git pull --no-rebase
    Auto-merging group2/README.md
    CONFLICT (content): Merge conflict in group2/README.md
    Automatic merge failed; fix conflicts and then commit the result.
    user@machine:~/escience2025-projects$ git status
    On branch pr-test
    Your branch and 'origin/pr-test' have diverged,
    and have 1 and 1 different commits each, respectively.
      (use "git pull" if you want to integrate the remote branch with yours)

    You have unmerged paths.
      (fix conflicts and run "git commit")
      (use "git merge --abort" to abort the merge)

    Unmerged paths:
      (use "git add <file>..." to mark resolution)
            both modified:   group2/README.md

    no changes added to commit (use "git add" and/or "git commit -a")

If you look at the file, that has a conflict, you will see:

.. code-block::

    <<<<<<< HEAD
    <!--this is another test comment -->
    =======
    <!-- this is just a comment -->^M
    >>>>>>> fc467bbde952f0befca3e14b99ec9adc6167f9e8

Current changes start with ``<<<<< some-reference`` and end with ``=====``, below are incoming changes which end with ``>>>>>> some-reference``.

You can manually resolve the conflict by modifying the file, the goal is to get rid of ``<<<<<< ===== >>>>>>`` lines.

Another way to resolve this, is to do ``git checkout --ours <path-to-file>`` or ``git checkout --theirs <path-to-file>``.
The former will apply current (local) changes to the file, the latter will apply whatever is incoming.

.. note::

    Jupyter hub notebooks are essentially a mix of json and html (+ some whistles). It's a bit hard to read if you don't know how the raw format works. 

    When you are in the middle of the merge and a notebook is modified in both references (i.e. has a conflict), you will not be able to open it normally.

    Doing ``git checkout --theirs/ours <path-to-file>`` is particularly useful in this case.

    If you have been executing/changing notebooks (f.e. notebook of someone else from another group) and have commited changes into your branch,
    and are pulling/merging ``upstream/main``, you most likely will have conficts in those notebooks.
    Just do ``git checkout --theirs <path-to-file>`` and it will stay the same way it is on the remote. For your own notebooks, if you are happy with your local changes, do ``git checkout --ours <path-to-file>``.

After all changes are resolved. You should add all the files with  f.e. ``git add --all`` and do a commit with ``git commit`` to finish the merge/rebase.
After that, if you do ``git status`` the ``diverged branches`` will dissapear and you can push to the remote branch as usual.


