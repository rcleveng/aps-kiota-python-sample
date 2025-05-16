from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .match_id_in import MatchId_In

@dataclass
class MatchId(AdditionalDataHolder, Parsable):
    """
    Use this to retrieve only the properties of objects with Object IDs or External IDs matching the specified values. Use the ``MatchIdType`` Enum to pick between Object IDs and External IDs. 
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Returns only the objects with their ``objectid`` or ``externalId`` attribute exactly matching one of the values specified in the array.The first element of the array contains the name of the attribute to match (``objectid`` or ``externalId``). Subsequent elements contain the values to match.For example, if you specify an array as: ``"$in":["objectid",1,2]``, the request will only return the properties of the objects with ``objectid`` = ``1`` and ``2``. If you specify an array as ``"$in":["externalId","doc_982afc8a","doc_afd75233" ]`` the request will only return the properties of the objects with ``externalId`` = ``doc_982afc8a`` and ``doc_afd75233``.
    in_: Optional[list[MatchId_In]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MatchId:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MatchId
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MatchId()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .match_id_in import MatchId_In

        from .match_id_in import MatchId_In

        fields: dict[str, Callable[[Any], None]] = {
            "$in": lambda n : setattr(self, 'in_', n.get_collection_of_object_values(MatchId_In)),
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
        writer.write_collection_of_object_values("$in", self.in_)
        writer.write_additional_data_value(self.additional_data)
    

