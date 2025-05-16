from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.api_error import APIError
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .hubs403_error_data import Hubs403Error_data
    from .hubs403_error_jsonapi import Hubs403Error_jsonapi
    from .hubs403_error_links import Hubs403Error_links
    from .hubs403_error_meta import Hubs403Error_meta

@dataclass
class Hubs403Error(APIError, AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # An object intended to contain the return data. Empty in this case, because an error has occurred.
    data: Optional[list[Hubs403Error_data]] = None
    # The JSON API object.
    jsonapi: Optional[Hubs403Error_jsonapi] = None
    # An object intended to contain the URI of a resource. Empty in this case, because an error has occurred.
    links: Optional[Hubs403Error_links] = None
    # Contains information about the error that occurred.
    meta: Optional[Hubs403Error_meta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Hubs403Error:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Hubs403Error
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Hubs403Error()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .hubs403_error_data import Hubs403Error_data
        from .hubs403_error_jsonapi import Hubs403Error_jsonapi
        from .hubs403_error_links import Hubs403Error_links
        from .hubs403_error_meta import Hubs403Error_meta

        from .hubs403_error_data import Hubs403Error_data
        from .hubs403_error_jsonapi import Hubs403Error_jsonapi
        from .hubs403_error_links import Hubs403Error_links
        from .hubs403_error_meta import Hubs403Error_meta

        fields: dict[str, Callable[[Any], None]] = {
            "data": lambda n : setattr(self, 'data', n.get_collection_of_object_values(Hubs403Error_data)),
            "jsonapi": lambda n : setattr(self, 'jsonapi', n.get_object_value(Hubs403Error_jsonapi)),
            "links": lambda n : setattr(self, 'links', n.get_object_value(Hubs403Error_links)),
            "meta": lambda n : setattr(self, 'meta', n.get_object_value(Hubs403Error_meta)),
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
        writer.write_collection_of_object_values("data", self.data)
        writer.write_object_value("jsonapi", self.jsonapi)
        writer.write_object_value("links", self.links)
        writer.write_object_value("meta", self.meta)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def primary_message(self) -> Optional[str]:
        """
        The primary error message.
        """
        return super().message

