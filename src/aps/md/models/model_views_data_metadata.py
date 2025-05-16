from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .role import Role

@dataclass
class ModelViews_data_metadata(AdditionalDataHolder, Parsable):
    """
    An array of flat JSON objects representing metadata.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Unique ID of the Model View.
    guid: Optional[str] = None
    # ``true``: Model View is a Master View derived from a Revit source design.``false``: Model View is not a Master View.
    is_master_view: Optional[bool] = None
    # Name of the Model View.
    name: Optional[str] = None
    # Specifies the type of a Model View.Possible values are: ``2d``, ``3d``.
    role: Optional[Role] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ModelViews_data_metadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ModelViews_data_metadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ModelViews_data_metadata()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .role import Role

        from .role import Role

        fields: dict[str, Callable[[Any], None]] = {
            "guid": lambda n : setattr(self, 'guid', n.get_str_value()),
            "isMasterView": lambda n : setattr(self, 'is_master_view', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "role": lambda n : setattr(self, 'role', n.get_enum_value(Role)),
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
        writer.write_str_value("guid", self.guid)
        writer.write_bool_value("isMasterView", self.is_master_view)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("role", self.role)
        writer.write_additional_data_value(self.additional_data)
    

