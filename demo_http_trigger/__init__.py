import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    comment = req.params.get('comment') or "Azure Functions is cool!"

    return func.HttpResponse(
        body=comment,
        status_code=200,
    )
