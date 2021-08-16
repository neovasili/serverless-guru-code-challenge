# Developer guide

&#x2B11; [Return to index](../README.md)

This document explains the details of the setup needed to use the repository in terms of development.

- [Developer guide](#developer-guide)
  - [Requirements](#requirements)
  - [Project setup](#project-setup)
    - [Supported arguments](#supported-arguments)
    - [Development](#development)
      - [Pre-commit](#pre-commit)
    - [Postman](#postman)
    - [Create Cognito user](#create-cognito-user)
  - [References](#references)

## Requirements

- [Nodejs](https://nodejs.org/en/)
- [Python3](https://www.python.org/download/releases/3.0/)
- [Docker](https://www.docker.com/) necessary for use `serverless-python-requirements` plugin

## Project setup

First things first.

As this is a serverless project we will have some parameters that will be setup from the serverless cli also known as `opt-values`. Those ones can be passed on every invocation of the serverless cli, like this:

```shell
sls info --region eu-west-1
```

Those ones can be different per developer and also, we need to consider that we will need other ones in order to cope variability of deployments per stage, account and even per developer, so we should define some environment variables (with default values) that will be used by each developer or process that is going to work with the serverless project.

We have a solution here to simplify this challenge.

You need to create a file called `./api/.local-arguments.yml` (there is a template file that you can use it to simplify the process `.local-arguments.template`) with the following content:

```yaml
---
stage: ${opt:stage, "dev"}
region: ${opt:region, "eu-west-1"}
prefix: ${env:PREFIX, "test"}
account: ${env:AWS_ACCOUNT_ID, "123456789012"}
api_version: ${env:API_VERSION, "v1"}
```

Just change the default values (the ones after the coma) with yours and that's it!

This file is ignored by git, so will be local to you and you can always still override any of those parameters in the cli, but if you don't specify them, those values will be retrieved as the default ones, so now, you can simply do:

```shell
sls info
```

And you will get the same output.

The parameters in this file are the ones in the next section, so please read this section to understand their meaning.

Once those values are set up, you can use them in the serverless.yml the following way:

```yaml
...
provider:
  name: aws
  runtime: python3.8
  stage: ${self:custom.arguments.stage}
  region: ${self:custom.arguments.region}
...
```

### Supported arguments

|Parameter|Default value|Description|
|:--:|:--:|:--:|
|`stage`|`dev`|Service deployment stage|
|`region`|`eu-west-1`|AWS region to deploy to|
|`prefix`|`test`|Prefix added to the service name just to avoid service development deployment collisions|
|`account`|`123456789012`|AWS account were to deploy the backend stack|
|`api-version`|`v1`|Argument to define API version which can be useful for deployment purposes|

### Development

For use this project in your local machine, just install npm dependencies:

```shell
npm install
```

To manually create a virtualenv on MacOS and Linux:

```shell
python3 -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```shell
source .env/bin/activate
```

Once the virtualenv is activated, you can install the required dependencies.

```shell
pip3 install -r requirements.txt
pip3 install -r requirements-dev.txt
```

#### Pre-commit

A pre-commit configuration file is provided in this repo to perform some linterns, validations and so on in order to avoid commit code to the repo that later will fail in validations step in the build pipeline.

The first execution can be slower because of installation of dependencies. Further executions will use the pre-commit cache.

Once you have all the requirements achieved, you have to install pre-commit in the local repository:

```shell
pre-commit install
```

And you can test it's working with the following:

```shell
➜ pre-commit run --all-files

Trim Trailing Whitespace.................................................Passed
Check python ast.........................................................Passed
Check for case conflicts.................................................Passed
Check that executables have shebangs.....................................Passed
Check JSON...............................................................Passed
Check for merge conflicts................................................Passed
Check vcs permalinks.....................................................Passed
Detect AWS Credentials...................................................Passed
Dont commit to branch....................................................Passed
Check markdown files.....................................................Passed
Yaml lintern.............................................................Passed
black....................................................................Passed
flake8...................................................................Passed
```

### Postman

This repository contains a extensive postman collection that can be imported and used to manually or automatically test the API.

The postman collection can be found here: `dev_tools/Serverlessguru - code challenge.postman_collection.json`.

There are some environment variables needed to make it work:

|variable name|description|
|:--:|:--:|
|`api_url`|API endpoint url (from AppSync) provided by the serverless framework once it's deployed|
|`cognito_auth_url`|Cognito auth endpoint url; use this one: `https://cognito-idp.<AWS_REGION>.amazonaws.com/`|
|`username`|Cognito user username that is going to be used for the tests|
|`password`|Cognito user password that is going to be used for the tests|
|`cognito_client_id`|Cognito User Pool Client ID; you will need to navigate to Cognito console to retrieve it|

Other variables are used by the postman collection, but they are automatically set making certain operations:

- `session_token`: this variable is set when you execute the request `cognito/InitAuth` and your Cognito user needs to change password
- `access_token`: this variable is set when you execute the request `cognito/InitAuth` and your Cognito user is ready to use; in the previous case, you may need to execute the request `cognito/ReplyChallenge` to get the access token; access token is **required** for all API requests
- `order_id`: this variable is set every time you successfully execute `CreateOrder` request, so it can be used for further other Order related requests

So, in order to use this postman collection you need to:

- Import collection
- Create postman environment and set required variables
- Create Cognito User (if you still don't have one)
- Execute `cognito/InitAuth` request
  - If no challenge where received in response, continue, otherwise run `cognito/ReplyChallenge` request
- Execute `CreateOrder` request
- Execute any other request as desired

### Create Cognito user

If you have AWS cli installed, you  can easily create and validate a Cognito user in order to work with the postman collection or even from the AppSync console. Here are the steps required:

Create user:

```shell
aws cognito-idp sign-up \
    --client-id <YOU_COGNITO_USER_POOL_CLIENT_ID> \
    --username test@test.com \
    --password "Testing-pass1" \
    --user-attributes Name=email,Value=test@test.com \
    --region eu-west-1
```

Confirm sign-up:

```shell
aws cognito-idp admin-confirm-sign-up \
    --user-pool-id <YOU_COGNITO_USER_POOL_ID> \
    --username test@test.com \
    --region eu-west-1
```

Mark email as verified:

```shell
aws cognito-idp admin-update-user-attributes \
    --user-pool-id <YOU_COGNITO_USER_POOL_ID> \
    --username test@test.com \
    --user-attributes Name=email_verified,Value=true \
    --region eu-west-1
```

## References

- [Serverless documentation](https://www.serverless.com/framework/docs/providers/aws/cli-reference/deploy/)
- [Serverless python requirements plugin](https://github.com/sid88in/serverless-appsync-plugin)
- [Serverless iam roles per function plugin](https://github.com/functionalone/serverless-iam-roles-per-function)
- [Serverless AppSync plugin](https://github.com/sid88in/serverless-appsync-plugin)
- [Pre-commit](https://pre-commit.com)
- [Postman](https://www.postman.com)
- [AWS CLI cognito reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html)
