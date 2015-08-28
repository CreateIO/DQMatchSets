# DQMatchSets

To add or change a template resource:
1) create a new branch in the DQMatchSets repository off of the “test” branch.
2) Commit and push your new or modified files up to the repository in your new branch.
3) Test your changes locally by using the command grunt serve:template=my_new_branch (instead of the normal grunt serve,
   and where my_new_branch is the name of your branch)
4) The DQ test server will fetch it from github and cache it locally when it can’t find it in its local cache for the
   specified branch, or when you use the serve:template option.
5) Please be judicious with this command, as it will pull from github for every template request made (and there is a 5000 request per day limit)!
6) When you are done, issue a pull request for your branch to merge with the baseline “test” branch.

Files pushed into the template folder and pushed to github become immediately accessable to both the dq-test.create.io,
   and the dq-prod.create.io servers ON THE BRANCH pushed to or merged into (typically via a pull request).

Note that template files are cached locally on each server...  If you make changes to an EXISTING template and you want
   to see these changes show up on the DQ server, you must either
   1) Run the create app locally with the command $ grunt serve:template=branch_name (where branch_name is the name of
      the branch you are deploying to, and then execute the code that requires the template.  This option is typically
      used during development, and is not recommended for final deployment to the servers.  To clear the cache for those,
      use the following method:
   2) To clear the cache on the test or prod servers for the github branch where you have pushed your changes to,
      use the script (located in the top level of the DQMatchSets repository -- i.e. same location as this README file):
         $ ./clear_cache.sh branch_name
      where "branch_name" is the name of the branch you have pushed your changes to.  This defaults to the dq-test server.
      If you must clear the cache on the dq-prod server, add the optional server specifier:
         $ ./clear_cache.sh branch_name server=prod


Example call to the DQ for template data:
https://dq-test.create.io/DQ/template?resource=tabs-&version=1.0.0&branch=test  (normal, use local cache if available)
https://dq-test.create.io/DQ/template?resource=tabs-&version=1.0.0&cache=false&branch=test (do not use local cache, re-grab file from git repository