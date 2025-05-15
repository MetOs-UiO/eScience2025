# Contribute to this page



## The recommended workflow for development
1. Fork the repository to your Github account and fetch upstream to receive the newest commits.
2. Alternatively, you should just clone this repo if you are part of the **eScience2025** team, this way the branches you create will get 
3. Perform the development in a newly-created branch (other than `master`) in your repository. 
4. Note that since we are using `myst-parser` both `.rst` and `.md` can be used.
5. Build the page in the command line to test the introduced modifications by following the instructions below.

### Locally build this page 
Before filling a pull-request you should check that the changes introduced by you still make the site build. Therefore, you should always [build and test locally](https://coderefinery.github.io/sphinx-lesson/contributing-to-a-lesson/#build-and-test-locally) before you ask for a pull request. 

To automatically update the documentation locally during development: 
```
$[~/PROJECT_ROOT] sphinx-autobuild docs/ _build
```
Using venv or conda is highly recommended. Also, when you are pulling from `master`, please don't forget to update your environment with `pip install -r requirements.txt` since those might have been changed since you last built the page locally.

## After you are done with your changes:

1. Merge or rebase on `upstream/master` (`master` if  you work within this repo) and resolve conflicts.
2. Check with `sphinx-autobuild` to see if the page builds and looks as intended.
3. Create a pull request to the `master` branch. Give a short description of what you have added.

The static webpage is hosted on Github and automatically built by pushing changes to the `master` branch. The built webpage is displayed when selecting the `gh-pages` branch. This process is automatic. A guide to the principles can be found [here](https://pythonrepo.com/repo/executablebooks-sphinx-autobuild-python-documentation). 

 If you have any questions, look in the Issues (including closed), if you don't find an answer - create a new one. 

> **NOTE** If workflow above is too hard for you, there is a Github button in the top-right corner.



## Reviewing PRs
1. Checkout branch that is getting pulled.
2. Build locally.
3. Add commits locally to fix things.
4. Add comments  in the pull request.
5. Merge the PR (if you have rights and are happy with the changes).

The web-page will get updated in a few minutes through github actions.

