from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .nested_xref import Nested_xref

@dataclass
class Json_api_relationships_refs_data_meta_extension_data(AdditionalDataHolder, Parsable):
    """
    The container of the additional properties.The additional properties must follow the schema specified by ``extensions.type`` and ``extensions.version``. Properties that don't follow the schema will be ignored.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The type of the xref, which defines how nested xrefs are handled. Possible values are:-  ``attachment``: Nested xrefs are not ignored.-  ``overlay`` : Nested xrefs are ignored.
    nested_type: Optional[Nested_xref] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Json_api_relationships_refs_data_meta_extension_data:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Json_api_relationships_refs_data_meta_extension_data
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Json_api_relationships_refs_data_meta_extension_data()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .nested_xref import Nested_xref

        from .nested_xref import Nested_xref

        fields: dict[str, Callable[[Any], None]] = {
            "nestedType": lambda n : setattr(self, 'nested_type', n.get_enum_value(Nested_xref)),
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
        writer.write_enum_value("nestedType", self.nested_type)
        writer.write_additional_data_value(self.additional_data)
    

