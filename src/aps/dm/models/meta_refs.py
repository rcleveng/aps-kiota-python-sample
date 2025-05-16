from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_attributes_extension_object_with_schema_link import Base_attributes_extension_object_with_schema_link
    from .metarefs_direction import Metarefs_direction
    from .type_entity import Type_entity
    from .type_ref import Type_ref

@dataclass
class MetaRefs(AdditionalDataHolder, Parsable):
    """
    Metadata on the resources referenced by this resource.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Describes the direction of data flow in the relationship. Possible values are:- ``to`` - Data flows from this resource to the related resource.- ``from`` - Data flows from the related resource to this resource. 
    direction: Optional[Metarefs_direction] = None
    # A container of additional properties that extends this resource.
    extension: Optional[Base_attributes_extension_object_with_schema_link] = None
    # The ID of the resource from where data flows.
    from_id: Optional[str] = None
    # The type of the resource. Possible values are ``folders``, ``items``, ``versions``.
    from_type: Optional[Type_entity] = None
    # The type of the resource. Possible values are ``derived``, ``dependencies``, ``auxiliary``, ``xrefs``, and ``includes``.
    ref_type: Optional[Type_ref] = None
    # The ID of the resource to where the data flows.
    to_id: Optional[str] = None
    # The type of the resource. Possible values are ``folders``, ``items``, ``versions``.
    to_type: Optional[Type_entity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MetaRefs:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MetaRefs
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MetaRefs()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_attributes_extension_object_with_schema_link import Base_attributes_extension_object_with_schema_link
        from .metarefs_direction import Metarefs_direction
        from .type_entity import Type_entity
        from .type_ref import Type_ref

        from .base_attributes_extension_object_with_schema_link import Base_attributes_extension_object_with_schema_link
        from .metarefs_direction import Metarefs_direction
        from .type_entity import Type_entity
        from .type_ref import Type_ref

        fields: dict[str, Callable[[Any], None]] = {
            "direction": lambda n : setattr(self, 'direction', n.get_enum_value(Metarefs_direction)),
            "extension": lambda n : setattr(self, 'extension', n.get_object_value(Base_attributes_extension_object_with_schema_link)),
            "fromId": lambda n : setattr(self, 'from_id', n.get_str_value()),
            "fromType": lambda n : setattr(self, 'from_type', n.get_enum_value(Type_entity)),
            "refType": lambda n : setattr(self, 'ref_type', n.get_enum_value(Type_ref)),
            "toId": lambda n : setattr(self, 'to_id', n.get_str_value()),
            "toType": lambda n : setattr(self, 'to_type', n.get_enum_value(Type_entity)),
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
        writer.write_enum_value("direction", self.direction)
        writer.write_object_value("extension", self.extension)
        writer.write_str_value("fromId", self.from_id)
        writer.write_enum_value("fromType", self.from_type)
        writer.write_enum_value("refType", self.ref_type)
        writer.write_str_value("toId", self.to_id)
        writer.write_enum_value("toType", self.to_type)
        writer.write_additional_data_value(self.additional_data)
    

