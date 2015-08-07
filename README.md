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

Files pushed into the template folder become immediately accessable in the dq-test.create.io server using the DQ/template HTTPS GET call.
Files are normally cached locally on the server, but if that call includes "&cache=false", then a re-pull from the DQMatchSets repository
 will occur for each file accesed this way.

Note: the repository branch where pulls are made is currently set to 'master', but can be changed in the DQ server environment file (dq_env.sh)

Example call to the DQ:
https://dq-test.create.io/DQ/template?resource=tabs-&version=1.0.0  (normal, use local cache if available)
https://dq-test.create.io/DQ/template?resource=tabs-&version=1.0.0&cache=false (do not use local cache, re-grab file from git repository