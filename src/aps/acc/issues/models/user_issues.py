from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .user_issues_filter import User_issues_filter
    from .user_issues_new import User_issues_new

@dataclass
class User_issues(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Not relevant
    filter: Optional[User_issues_filter] = None
    # If this object appears in the response, it indicates that the user can create and modify issues.
    new: Optional[User_issues_new] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> User_issues:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: User_issues
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return User_issues()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .user_issues_filter import User_issues_filter
        from .user_issues_new import User_issues_new

        from .user_issues_filter import User_issues_filter
        from .user_issues_new import User_issues_new

        fields: dict[str, Callable[[Any], None]] = {
            "filter": lambda n : setattr(self, 'filter', n.get_object_value(User_issues_filter)),
            "new": lambda n : setattr(self, 'new', n.get_object_value(User_issues_new)),
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
        writer.write_object_value("filter", self.filter)
        writer.write_object_value("new", self.new)
        writer.write_additional_data_value(self.additional_data)
    

