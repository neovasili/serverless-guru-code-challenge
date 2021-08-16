# Serverlessguru Code Challenge

|Name|Badge|
|:-:|:-:|
|Linters|[![Checks, linters and formatters](https://github.com/neovasili/serverless-guru-code-challenge/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/neovasili/serverless-guru-code-challenge/actions/workflows/pre-commit.yml)|
|Quality|[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=neovasili_serverless-guru-code-challenge&metric=alert_status)](https://sonarcloud.io/dashboard?id=neovasili_serverless-guru-code-challenge)|
|Build and deploy check|[![Build check](https://github.com/neovasili/serverless-guru-code-challenge/actions/workflows/build-check.yaml/badge.svg)](https://github.com/neovasili/serverless-guru-code-challenge/actions/workflows/build-check.yaml)|
|Run tests|[![Run Tests](https://github.com/neovasili/serverless-guru-code-challenge/actions/workflows/run-tests.yaml/badge.svg)](https://github.com/neovasili/serverless-guru-code-challenge/actions/workflows/run-tests.yaml)|

Repository containing the code challenge requested: [Serverless Guru code challenge](https://github.com/serverless-guru/code-challenges/tree/master/code-challenge-4)

- [Serverlessguru Code Challenge](#serverlessguru-code-challenge)
  - [Documentation contents](#documentation-contents)
  - [Out of scope](#out-of-scope)

## Documentation contents

- [Solution](docs/solution.md)
- [Developer Guide](docs/development.md)
- [CI/CD](docs/ci-cd.md)

## Out of scope

Because lack of time enough or not specifically asked on the code challenge requirements, some things that usually are `must's` for any development, have been left out the scope for now:

- **Unit tests**: only a few "demonstrative" unit tests were created in order to also make the CI workflow do "something".
- **Integration tests**: no integration specific test have been done apart from build and deploy checks; anyway, provided postman collection, can be easily used to check at the CI level some integrations.
- **Tests Coverage integration with Sonar Cloud**: Coverage has been added to compute it, but is still not integrated with Sonar Cloud project.
- **End to end tests**: end to end tests have a high cost in terms of development, maintenance and even infrastructure, so they are out of the scope for this challenge; anyway, provided postman collection, can be easily used to check at the deployment to INT level.
- **List orders operation**: usually, any API will have some sort of listing operation; I included it into the initial design, but I was running out of time, so was left aside.
- **GraphQL error responses handling**: since this is my first approach to AppSync and GraphQL APIs, this is left aside for now in order to complete other things more prior; anyway, errors are catched in the API, even if the response is not explanatory enough for the consumer.
