import boto3


class BotoHelper:
    def __init__(self, namespace: str, region_name="eu-west-1"):
        self.__namespace = namespace
        self.client = boto3.client(self.__namespace, region_name)
        # boto3.set_stream_logger(name='botocore')

    def change_credentials(self, credentials: dict, region: str = "eu-west-1"):
        self.client = boto3.client(
            self.__namespace,
            region_name=region,
            aws_access_key_id=credentials["AccessKeyId"],
            aws_secret_access_key=credentials["SecretAccessKey"],
            aws_session_token=credentials["SessionToken"],
        )

    def who_am_i(self):
        response = self.client.get_caller_identity()
        print(response)


class BotoResourceHelper(BotoHelper):
    def __init__(self, namespace: str, region_name="eu-west-1"):
        super().__init__(namespace=namespace, region_name=region_name)
        self.__namespace = namespace
        self.resource = boto3.resource(self.__namespace, region_name)

    def change_credentials(self, credentials: dict, region: str = "eu-west-1"):
        self.resource = boto3.resource(
            self.__namespace,
            region_name=region,
            aws_access_key_id=credentials["AccessKeyId"],
            aws_secret_access_key=credentials["SecretAccessKey"],
            aws_session_token=credentials["SessionToken"],
        )
