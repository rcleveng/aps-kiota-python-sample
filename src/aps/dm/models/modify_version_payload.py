from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_api_version import Json_api_version
    from .modify_version_payload_data import ModifyVersionPayload_data

@dataclass
class ModifyVersionPayload(AdditionalDataHolder, Parsable):
    """
    An object that contains the information on the version to be patched.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Contains the information to update
    data: Optional[ModifyVersionPayload_data] = None
    # The JSON API object.
    jsonapi: Optional[Json_api_version] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ModifyVersionPayload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModifyVersionPayload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ModifyVersionPayload()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .json_api_version import Json_api_version
        from .modify_version_payload_data import ModifyVersionPayload_data

        from .json_api_version import Json_api_version
        from .modify_version_payload_data import ModifyVersionPayload_data

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_object_value(ModifyVersionPayload_data)),
            "jsonapi": lambda n : setattr(self, 'jsonapi', n.get_object_value(Json_api_version)),
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
        writer.write_object_value("data", self.data)
        writer.write_object_value("jsonapi", self.jsonapi)
        writer.write_additional_data_value(self.additional_data)
    

