from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attr_definition_page_results_metadata_list_options import Attr_definition_page_results_metadata_list_options

@dataclass
class Attr_definition_page_results_metadata_list(AdditionalDataHolder, Parsable):
    """
    The list object.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The options object.
    options: Optional[list[Attr_definition_page_results_metadata_list_options]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Attr_definition_page_results_metadata_list:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Attr_definition_page_results_metadata_list
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Attr_definition_page_results_metadata_list()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attr_definition_page_results_metadata_list_options import Attr_definition_page_results_metadata_list_options

        from .attr_definition_page_results_metadata_list_options import Attr_definition_page_results_metadata_list_options

        fields: dict[str, Callable[[Any], None]] = {
            "options": lambda n : setattr(self, 'options', n.get_collection_of_object_values(Attr_definition_page_results_metadata_list_options)),
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
        writer.write_collection_of_object_values("options", self.options)
        writer.write_additional_data_value(self.additional_data)
    

