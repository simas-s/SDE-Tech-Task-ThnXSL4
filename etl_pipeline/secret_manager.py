from os import getenv
from google.cloud.secretmanager import SecretManagerServiceClient

PROJECT_ID = getenv("PROJECT_ID", default=None)


def get_secret_value(secret_id: str, version: str = "latest"):
    """
    Function returns value of a provided secret version stored in Secret Manager.
    :param secret_id: Determines which secret this function will return.
    :param version: Determines which version of the provided secret this function will return.
    :return: Value of provided secret version.
    """
    client = SecretManagerServiceClient()
    secret_name = f"projects/{PROJECT_ID}/secrets/{secret_id}/versions/{version}"
    response = client.access_secret_version(request={"name": secret_name})
    return response.payload.data.decode("UTF-8")

