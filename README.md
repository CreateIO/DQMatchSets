# DQMatchSets

Template resources are HIERARCHICAL!!  This means that templates that are global (or at least for use in the US) should
   be in the "US" folder.  Templates (or parts of a template) that are unique to a specific region should be in the
   specific folder appropriate to them (i.e. "US/US11001" for DC, or "US/US24510 for Baltimore city).  Note that under
   any of these folders, you can put template resources in their sub-folders to group them if needed (such as "US/US11001/filters"
   for example).

   The DQ will look for the resource in the folder "US" first, then attempt to read the same resource from the local region
   folder.  If it exists in the local region, any (or all) of the JSON objects in that local region folder resource will
   replace or override the same JSON object (if it exists) in the "US" folder.

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

To have your local server use the branch you are testing with, run the create app locally with the command:
   $ grunt serve:template=branch_name (where branch_name is the name of the branch you are deploying to,
      and then execute the code that requires the template.  This option is typically
      used during development, and is not recommended for final deployment to the servers.

To publish template data for use with production or test servers:
   1) Merge your changes (typically from the “test” branch) into the appropriate branch for where you are deploying
      (oberlin-prod for production, oberlin-integration for test/demo, or just test for those)
   2) Insure that the environment vars in the server are configured correctly to the branch and dq instance you desire
      (test = dq-test.create.io    prod=dq-prod.create.io)

