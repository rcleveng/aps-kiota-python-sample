from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Downloads403Error_meta_warnings(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A more comprehensive explanation of the issue, providing specific information and potential solutions, if any.
    detail: Optional[str] = None
    # A code that indicates what went wrong.
    error_code: Optional[str] = None
    # The HTTP status code returned in response to the request.
    http_status_code: Optional[str] = None
    # A quick summary of the issue, at a glance.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Downloads403Error_meta_warnings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Downloads403Error_meta_warnings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Downloads403Error_meta_warnings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "Detail": lambda n : setattr(self, 'detail', n.get_str_value()),
            "ErrorCode": lambda n : setattr(self, 'error_code', n.get_str_value()),
            "HttpStatusCode": lambda n : setattr(self, 'http_status_code', n.get_str_value()),
            "Title": lambda n : setattr(self, 'title', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("Detail", self.detail)
        writer.write_str_value("ErrorCode", self.error_code)
        writer.write_str_value("HttpStatusCode", self.http_status_code)
        writer.write_str_value("Title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

