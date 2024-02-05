# Selenium

To deploy:
- PR this repository and merge to `staging`. This will automatically deploy infrastructure changes and update the nightly regression tests.

## Running behave locally

### Run all tests

`docker compose --profile local up`

### Run selected tests
Run selected tests based on a given tag:
```
behave -t \<tag> -k
```
Replace <tag> with the relevant tag for the test eg `owner_regression` or `pipeline_dss`:

## Running in Cloud (LambdaTest)

Go to https://accounts.lambdatest.com/dashboard and click Configure Tunnel. Copy the user and key into `.env`:

`CLOUD_USER=foo`
`CLOUD_KEY=bar`

Then run this command to bring up the local cluster:

`docker compose --profile cloud up`

## Devops information

### We no longer run Selenium using Grid in the Monolith deployment pipelines. 

Instead, the deployment pipeline uses individual containers in parallel. The code for this is [here](https://github.com/tailsdotcom/tails/blob/staging/.github/workflows/monolith_deploy.yaml#L727-L766).
To include additional tests, add the step to be run under the `matrix: test:` array.

### Deployment of tunnel and cronjobs

https://github.com/tailsdotcom/tails-apps-k8s/tree/staging/selenium

## QA information

The dependencies are all managed with Pipenv. Please follow PyCharm's doc for how to set up your local environment: https://www.jetbrains.com/help/pycharm/pipenv.html

If you want to update your dependencies you can just run `pipenv update` which will update the Pipfile.lock with the latest available versions of all Python dependencies.

## Running via hyperexecute

- Install hyperexecute via lambdatest https://www.lambdatest.com/support/docs/hyperexecute-cli-run-tests-on-hyperexecute-grid/
- Run 'chmod +x hyperexecute' in your terminal to set up authorisation access 
- Follow the steps in this guide to add your LT credentials to your local https://tailscom.atlassian.net/wiki/spaces/EQA/pages/3626958944/The+Hyperexecute+Guide#Step-2%3A-Running-Tests 
- Then run the following commands, the test .yamls are contained in a new folder called yaml_files and are further organised via device type (chrome, iphone, android) and you will need to call the full folder path + file name in order to run them as part of your HYE terminal command:
  - Mac: './hyperexecute --config yaml_files/{filename}.yaml -v' e.g. './hyperexecute --config yaml_files/desktop/desktop_perf_nonprod.yaml -v'
  - Windows: 'hyperexecute.exe --config yaml_files/{filename}.yaml -v' e.g. 'hyperexecute.exe --config yaml_files/desktop/desktop_perf_nonprod.yaml -v'
- If you want to run a specific test or set of tests you can do so via the tags by adding "--vars tag="tag_name_here" onto the end of the command
- You can then go to https://hyperexecute.lambdatest.com/hyperexecute/jobs to see the build running and whether the tests pass
- The steps above will run all tests that have the correct tags which are listed in the iphone.yaml, desktop.yaml and android.yaml: specificTags: ["@nightly_iphone"]
- To run your own set of tags, use the debug_single_tags_iphone.yaml file and pass in --vars tag="tag_name_here"


Adding your tests to the builds: 
- Either create a new tag and add it into the device yaml file you wish, or use one of the listed existing tags and add it to your scenario
Additional HYE guide: https://tailscom.atlassian.net/wiki/spaces/EQA/pages/3626958944/The+Hyperexecute+Guide

Issues: 
- If you get an error to restart the binary to update the changes when trying to run the tests, just re-run the final command above 
- If you see an error regarding formatting of ./hyperexcute command, ensure the hyperexecute file is saved in the correct place in the directory. It should be directly in your main project folder
- If the build isn't showing in Lambdatest, check there isn't already two builds running as this is the maximum. You can abort the builds from the jobs page https://hyperexecute.lambdatest.com/hyperexecute/jobs

## Installing Selenium repo

Cloning the repo: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository
Setting up in Pycharm: https://tailscom.atlassian.net/wiki/x/nYBm0w
Setting up a virtual environment in Pycharm (needed to run the pip commands in the above doc): https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#view_list
