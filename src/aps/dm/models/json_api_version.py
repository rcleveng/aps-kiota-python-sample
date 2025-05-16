from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_api_version_value import Json_api_version_value

@dataclass
class Json_api_version(AdditionalDataHolder, Parsable):
    """
    The JSON API object.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The version of JSON API. Will always be ``1.0``.
    version: Optional[Json_api_version_value] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Json_api_version:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Json_api_version
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Json_api_version()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .json_api_version_value import Json_api_version_value

        from .json_api_version_value import Json_api_version_value

        fields: dict[str, Callable[[Any], None]] = {
            "version": lambda n : setattr(self, 'version', n.get_enum_value(Json_api_version_value)),
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
        writer.write_enum_value("version", self.version)
        writer.write_additional_data_value(self.additional_data)
    

