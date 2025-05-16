from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .top_folder_extension_with_schema_link import Top_folder_extension_with_schema_link

@dataclass
class TopFolderAttributesWithExtensions(AdditionalDataHolder, Parsable):
    """
    The properties of a folder.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The time the folder was created, in the following format: ``YYYY-MM-DDThh:mm:ss.sz``.
    create_time: Optional[datetime.datetime] = None
    # The unique identifier of the user who created the folder.
    create_user_id: Optional[str] = None
    # The name of the user who created the folder.
    create_user_name: Optional[str] = None
    # Reserved for future Use. Do not use. Use ``attributes.name`` for the folder name.
    display_name: Optional[str] = None
    # A container of additional properties that extends the default properties of this resource.
    extension: Optional[Top_folder_extension_with_schema_link] = None
    # The folder’s current visibility state.
    hidden: Optional[bool] = None
    # The last time the folder was modified, in the following format: ``YYYY-MM-DDThh:mm:ss.sz``.
    last_modified_time: Optional[datetime.datetime] = None
    # The date and time the folder or any of its children were last updated.
    last_modified_time_rollup: Optional[str] = None
    # The last time the folder was modified, in the following format: ``YYYY-MM-DDThh:mm:ss.sz``.
    last_modified_user_id: Optional[str] = None
    # The name of the user who last modified the folder.
    last_modified_user_name: Optional[str] = None
    # The name of the folder.
    name: Optional[str] = None
    # The number of objects inside the folder.
    object_count: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TopFolderAttributesWithExtensions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TopFolderAttributesWithExtensions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TopFolderAttributesWithExtensions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .top_folder_extension_with_schema_link import Top_folder_extension_with_schema_link

        from .top_folder_extension_with_schema_link import Top_folder_extension_with_schema_link

        fields: dict[str, Callable[[Any], None]] = {
            "createTime": lambda n : setattr(self, 'create_time', n.get_datetime_value()),
            "createUserId": lambda n : setattr(self, 'create_user_id', n.get_str_value()),
            "createUserName": lambda n : setattr(self, 'create_user_name', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extension": lambda n : setattr(self, 'extension', n.get_object_value(Top_folder_extension_with_schema_link)),
            "hidden": lambda n : setattr(self, 'hidden', n.get_bool_value()),
            "lastModifiedTime": lambda n : setattr(self, 'last_modified_time', n.get_datetime_value()),
            "lastModifiedTimeRollup": lambda n : setattr(self, 'last_modified_time_rollup', n.get_str_value()),
            "lastModifiedUserId": lambda n : setattr(self, 'last_modified_user_id', n.get_str_value()),
            "lastModifiedUserName": lambda n : setattr(self, 'last_modified_user_name', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "objectCount": lambda n : setattr(self, 'object_count', n.get_float_value()),
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
        writer.write_datetime_value("createTime", self.create_time)
        writer.write_str_value("createUserId", self.create_user_id)
        writer.write_str_value("createUserName", self.create_user_name)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("extension", self.extension)
        writer.write_bool_value("hidden", self.hidden)
        writer.write_datetime_value("lastModifiedTime", self.last_modified_time)
        writer.write_str_value("lastModifiedTimeRollup", self.last_modified_time_rollup)
        writer.write_str_value("lastModifiedUserId", self.last_modified_user_id)
        writer.write_str_value("lastModifiedUserName", self.last_modified_user_name)
        writer.write_str_value("name", self.name)
        writer.write_float_value("objectCount", self.object_count)
        writer.write_additional_data_value(self.additional_data)
    

