"""
This module contains a Python interface for Problem Details for HTTP APIs
<https://tools.ietf.org/html/draft-ietf-appsawg-http-problem-00>, which is a standardized format
to communicate distinct "problem types" to non-human consumers.
"""

from .lifecycle import ConnexionResponse


def problem(status, title, detail, type=None, instance=None, headers=None, ext=None):
    """
    Returns a `Problem Details <https://tools.ietf.org/html/draft-ietf-appsawg-http-problem-00>`_ error response.


    :param status: The HTTP status code generated by the origin server for this occurrence of the problem.
    :type status: int
    :param title: A short, human-readable summary of the problem type.  It SHOULD NOT change from occurrence to
                  occurrence of the problem, except for purposes of localisation.
    :type title: str
    :param detail: An human readable explanation specific to this occurrence of the problem.
    :type detail: str
    :param type: An absolute URI that identifies the problem type.  When dereferenced, it SHOULD provide human-readable
                 documentation for the problem type (e.g., using HTML).  When this member is not present its value is
                 assumed to be "about:blank".
    :type: type: str
    :param instance: An absolute URI that identifies the specific occurrence of the problem.  It may or may not yield
                     further information if dereferenced.
    :type instance: str
    :param headers: HTTP headers to include in the response
    :type headers: dict | None
    :param ext: Extension members to include in the body
    :type ext: dict | None
    :return: error response
    :rtype: ConnexionResponse
    """
    if not type:
        type = 'about:blank'

    problem_response = {'type': type, 'title': title, 'detail': detail, 'status': status}
    if instance:
        problem_response['instance'] = instance
    if ext:
        problem_response.update(ext)

    mimetype = content_type = 'application/problem+json'
    return ConnexionResponse(status, mimetype, content_type,
                             body=problem_response,
                             headers=headers)
