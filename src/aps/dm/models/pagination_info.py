from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .pagination_info_first import PaginationInfo_first
    from .pagination_info_next import PaginationInfo_next
    from .pagination_info_prev import PaginationInfo_prev
    from .pagination_info_self import PaginationInfo_self

@dataclass
class PaginationInfo(AdditionalDataHolder, Parsable):
    """
    An object that is returned with responses that can be split across multiple pages. "Next," "Previous," and "First" are available only if the response is split across multiple pages.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A container for the link to the first page of the response.
    first: Optional[PaginationInfo_first] = None
    # A container for the link to the next page of the response.
    next: Optional[PaginationInfo_next] = None
    # A container for the link to the previous page of the response.
    prev: Optional[PaginationInfo_prev] = None
    # A container for the link to the current page of the response.
    self: Optional[PaginationInfo_self] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PaginationInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PaginationInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PaginationInfo()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .pagination_info_first import PaginationInfo_first
        from .pagination_info_next import PaginationInfo_next
        from .pagination_info_prev import PaginationInfo_prev
        from .pagination_info_self import PaginationInfo_self

        from .pagination_info_first import PaginationInfo_first
        from .pagination_info_next import PaginationInfo_next
        from .pagination_info_prev import PaginationInfo_prev
        from .pagination_info_self import PaginationInfo_self

        fields: dict[str, Callable[[Any], None]] = {
            "first": lambda n : setattr(self, 'first', n.get_object_value(PaginationInfo_first)),
            "next": lambda n : setattr(self, 'next', n.get_object_value(PaginationInfo_next)),
            "prev": lambda n : setattr(self, 'prev', n.get_object_value(PaginationInfo_prev)),
            "self": lambda n : setattr(self, 'self', n.get_object_value(PaginationInfo_self)),
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
        writer.write_object_value("first", self.first)
        writer.write_object_value("next", self.next)
        writer.write_object_value("prev", self.prev)
        writer.write_object_value("self", self.self)
        writer.write_additional_data_value(self.additional_data)
    

