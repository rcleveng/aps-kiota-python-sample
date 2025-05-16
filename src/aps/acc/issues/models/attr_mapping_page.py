from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .attr_mapping_page_results import Attr_mapping_page_results
    from .pagination import Pagination

@dataclass
class Attr_mapping_page(AdditionalDataHolder, Parsable):
    """
    The pagination object.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The pagination object.
    pagination: Optional[Pagination] = None
    # A list of issue attribute mappings.
    results: Optional[list[Attr_mapping_page_results]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Attr_mapping_page:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Attr_mapping_page
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Attr_mapping_page()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .attr_mapping_page_results import Attr_mapping_page_results
        from .pagination import Pagination

        from .attr_mapping_page_results import Attr_mapping_page_results
        from .pagination import Pagination

        fields: dict[str, Callable[[Any], None]] = {
            "pagination": lambda n : setattr(self, 'pagination', n.get_object_value(Pagination)),
            "results": lambda n : setattr(self, 'results', n.get_collection_of_object_values(Attr_mapping_page_results)),
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
        writer.write_object_value("pagination", self.pagination)
        writer.write_collection_of_object_values("results", self.results)
        writer.write_additional_data_value(self.additional_data)
    

