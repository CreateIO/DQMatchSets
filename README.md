# DQMatchSets

Files pushed into the template folder become immediately accessable in the dq-test.create.io server using the DQ/template HTTPS GET call.
Files are normally cached locally on the server, but if that call includes "&cache=false", then a re-pull from the DQMatchSets repository
 will occur for each file accesed this way.

Note: the repository branch where pulls are made is currently set to 'master', but can be changed in the DQ server environment file (dq_env.sh)

Example call to the DQ:
https://dq-test.create.io/DQ/template?resource=tabs-&version=1.0.0  (normal, use local cache if available)
https://dq-test.create.io/DQ/template?resource=tabs-&version=1.0.0&cache=false (do not use local cache, re-grab file from git repository