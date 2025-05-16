from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_api_relationships_refs_data_meta_extension import Json_api_relationships_refs_data_meta_extension
    from .metarefs_direction import Metarefs_direction
    from .reftypes_xref import Reftypes_xref

@dataclass
class Json_api_relationships_refs_data_meta(AdditionalDataHolder, Parsable):
    """
    The meta-information describing the custom relationship.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Describes the direction of data flow in the relationship. Possible values are:- ``to`` - Data flows from this resource to the related resource.- ``from`` - Data flows from the related resource to this resource. 
    direction: Optional[Metarefs_direction] = None
    # A container of additional properties that extends the default properties of this resource.
    extension: Optional[Json_api_relationships_refs_data_meta_extension] = None
    # The type of custom relationship. Will always be ``xrefs``.
    ref_type: Optional[Reftypes_xref] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Json_api_relationships_refs_data_meta:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Json_api_relationships_refs_data_meta
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Json_api_relationships_refs_data_meta()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .json_api_relationships_refs_data_meta_extension import Json_api_relationships_refs_data_meta_extension
        from .metarefs_direction import Metarefs_direction
        from .reftypes_xref import Reftypes_xref

        from .json_api_relationships_refs_data_meta_extension import Json_api_relationships_refs_data_meta_extension
        from .metarefs_direction import Metarefs_direction
        from .reftypes_xref import Reftypes_xref

        fields: dict[str, Callable[[Any], None]] = {
            "direction": lambda n : setattr(self, 'direction', n.get_enum_value(Metarefs_direction)),
            "extension": lambda n : setattr(self, 'extension', n.get_object_value(Json_api_relationships_refs_data_meta_extension)),
            "refType": lambda n : setattr(self, 'ref_type', n.get_enum_value(Reftypes_xref)),
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
        writer.write_enum_value("refType", self.ref_type)
        writer.write_additional_data_value(self.additional_data)
    

