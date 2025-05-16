from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.api_error import APIError
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .permission_level import Permission_level
    from .user_issues import User_issues

@dataclass
class User(APIError, AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Not relevant
    can_manage_templates: Optional[bool] = None
    # Unique identifier for the given user.
    id: Optional[str] = None
    # States whether the current logged in user is a system admin.
    is_project_admin: Optional[bool] = None
    # The issues property
    issues: Optional[User_issues] = None
    # The permission level of the user. Each permission level corresponds to a combination of values in the response. For example, a combination of read and create in the response, corresponds to a Create for other companies permission level.
    permission_levels: Optional[list[Permission_level]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> User:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: User
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return User()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .permission_level import Permission_level
        from .user_issues import User_issues

        from .permission_level import Permission_level
        from .user_issues import User_issues

        fields: dict[str, Callable[[Any], None]] = {
            "canManageTemplates": lambda n : setattr(self, 'can_manage_templates', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isProjectAdmin": lambda n : setattr(self, 'is_project_admin', n.get_bool_value()),
            "issues": lambda n : setattr(self, 'issues', n.get_object_value(User_issues)),
            "permissionLevels": lambda n : setattr(self, 'permission_levels', n.get_collection_of_enum_values(Permission_level)),
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
        writer.write_bool_value("canManageTemplates", self.can_manage_templates)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isProjectAdmin", self.is_project_admin)
        writer.write_object_value("issues", self.issues)
        writer.write_collection_of_enum_values("permissionLevels", self.permission_levels)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def primary_message(self) -> Optional[str]:
        """
        The primary error message.
        """
        return super().message

