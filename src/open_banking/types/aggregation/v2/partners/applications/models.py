"""File Generated by Sideko (sideko.dev)"""

import io
import typing


import pydantic

ModelFiles = typing.List[
    typing.Tuple[str, typing.Union[typing.BinaryIO, io.BufferedReader]]
]


class AppFinancialInstitutionStatus(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    abbrv_name: typing.Optional[str] = pydantic.Field(alias="abbrvName", default=None)
    created_date: int = pydantic.Field(alias="createdDate")
    decryption_key_activated: bool = pydantic.Field(alias="decryptionKeyActivated")
    id: int = pydantic.Field(alias="id")
    last_modified_date: int = pydantic.Field(alias="lastModifiedDate")
    logo_url: typing.Optional[str] = pydantic.Field(alias="logoUrl", default=None)
    status: bool = pydantic.Field(alias="status")


class AppStatus(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    app_name: str = pydantic.Field(alias="appName")
    application_id: typing.Optional[str] = pydantic.Field(
        alias="applicationId", default=None
    )
    institution_details: typing.Optional[typing.List[AppFinancialInstitutionStatus]] = (
        pydantic.Field(alias="institutionDetails", default=None)
    )
    modified_date: int = pydantic.Field(alias="modifiedDate")
    note: typing.Optional[str] = pydantic.Field(alias="note", default=None)
    partner_id: str = pydantic.Field(alias="partnerId")
    pre_app_id: str = pydantic.Field(alias="preAppId")
    scopes: typing.Optional[str] = pydantic.Field(alias="scopes", default=None)
    status: str = pydantic.Field(alias="status")
    submitted_date: int = pydantic.Field(alias="submittedDate")


class AppStatuses(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    applications: typing.List[AppStatus] = pydantic.Field(alias="applications")
    number_of_records_per_page: int = pydantic.Field(alias="numberOfRecordsPerPage")
    page_number: int = pydantic.Field(alias="pageNumber")
    total_pages: int = pydantic.Field(alias="totalPages")
    total_records: int = pydantic.Field(alias="totalRecords")
