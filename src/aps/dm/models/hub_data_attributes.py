from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_attributes_extension_object_with_schema_link import Base_attributes_extension_object_with_schema_link
    from .region import Region

@dataclass
class HubData_attributes(AdditionalDataHolder, Parsable):
    """
    The properties of the hub.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A container of additional properties that extends this resource.
    extension: Optional[Base_attributes_extension_object_with_schema_link] = None
    # A human friendly name to identify the hub.
    name: Optional[str] = None
    # Specifies where the hub is stored. Possible values are:- ``US`` - Data center for the US region.- ``EMEA`` - Data center for the European Union, Middle East, and Africa regions.- ``AUS`` - Data center for the Australia region.
    region: Optional[Region] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HubData_attributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HubData_attributes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HubData_attributes()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_attributes_extension_object_with_schema_link import Base_attributes_extension_object_with_schema_link
        from .region import Region

        from .base_attributes_extension_object_with_schema_link import Base_attributes_extension_object_with_schema_link
        from .region import Region

        fields: dict[str, Callable[[Any], None]] = {
            "extension": lambda n : setattr(self, 'extension', n.get_object_value(Base_attributes_extension_object_with_schema_link)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_enum_value(Region)),
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
        writer.write_object_value("extension", self.extension)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("region", self.region)
        writer.write_additional_data_value(self.additional_data)
    

