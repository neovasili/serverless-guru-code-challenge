# Serverlessguru Code Challenge

Repository containing the code challenge requested

- [Serverlessguru Code Challenge](#serverlessguru-code-challenge)
  - [Requirements](#requirements)
  - [Project setup](#project-setup)
    - [Supported arguments](#supported-arguments)
    - [Development](#development)
      - [Pre-commit](#pre-commit)
        - [Use pre-commit](#use-pre-commit)
  - [References](#references)

## Requirements

- [Nodejs](https://nodejs.org/en/)
- [Python3](https://www.python.org/download/releases/3.0/)
- [Docker](https://www.docker.com/) necessary for use `serverless-python-requirements` plugin

## Project setup

First things first.

As this is a serverless project we will have some parameters that will be setup from the serverless cli also known as `opt-values`. Those ones can be passed on every invocation of the serverless cli, like this:

```shell
sls info --name jmr --region eu-west-1
```

In this example we are passing the parameters `name` and `region` so, if they are specified in the cli, those values will be replaced in the serverless.yml file with the specified values.

The problem is that when we start having a lot of parameters this can be tedious and have a high cognitive complexity:

```shell
sls info --name juf --region eu-west-1 --cognito-arn "arn:aws:cognito-idp:eu-west-1:123456789012:userpool/eu-west-1_xxxxxxxxxxx" --dns-account "234567890123" --dns-hz-id "XXXXXXXXXXXXXXX" --aws-default-account "123456789012"
```

We have a solution here to simplify this.

You need to create a file called `./api/.local-arguments.yml` (there is a template file that you can use it to simplify the process `.local-arguments.yml.template`) with the following content:

```yaml
---
stage: ${opt:stage, "dev"}
region: ${opt:region, "eu-west-1"}
prefix: ${opt:prefix, "jmr"}
api_version: ${opt:api-version, "v1"}
```

Just change the uppercase values with yours and that's it!

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
  stage: ${ self:custom.arguments.stage }
  region: ${ self:custom.arguments.region }
...
```

### Supported arguments

|Parameter|Default value|Description|
|:--:|:--:|:--:|
|`stage`|`dev`|Service deployment stage|
|`region`|`eu-west-1`|AWS region to deploy to|
|`prefix`||Prefix added to the service name just to avoid service development deployment collisions|
|`api-version`||Argument to define API version which can be useful for deployment purposes|

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

##### Use pre-commit

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

## References

- [Serverless documentation](https://www.serverless.com/framework/docs/providers/aws/cli-reference/deploy/)
