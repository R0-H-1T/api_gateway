from fastapi import Form
from typing import Annotated
from typing_extensions import Doc

class OAuth2RefreshForm:
    def __init__(
        self,
        *,
        grant_type: Annotated[
            str,
            Form(pattern='refresh_token'),
            Doc(
                """
                    This OAuth2 spec requires the grant type to strictly be
                    `refresh_token`
                """
            )
        ],
        refresh_token: Annotated[
            str,
            Form(),
            Doc(
                """
                    refresh token to be sent is of the type str
                """
            )
        ]
    ):
        self.grant_type = grant_type
        self.refresh_token = refresh_token