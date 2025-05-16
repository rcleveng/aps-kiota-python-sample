from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attr_definition_page_results_metadata_list import Attr_definition_page_results_metadata_list

@dataclass
class Attr_definition_page_results_metadata(AdditionalDataHolder, Parsable):
    """
    The metadata object; only relevant for list custom attributes.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The list object.
    list_: Optional[Attr_definition_page_results_metadata_list] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Attr_definition_page_results_metadata:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Attr_definition_page_results_metadata
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Attr_definition_page_results_metadata()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attr_definition_page_results_metadata_list import Attr_definition_page_results_metadata_list

        from .attr_definition_page_results_metadata_list import Attr_definition_page_results_metadata_list

        fields: dict[str, Callable[[Any], None]] = {
            "list": lambda n : setattr(self, 'list_', n.get_object_value(Attr_definition_page_results_metadata_list)),
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
        writer.write_object_value("list", self.list_)
        writer.write_additional_data_value(self.additional_data)
    

