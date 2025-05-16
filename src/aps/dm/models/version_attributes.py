from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .version_extension_with_schema_link import Version_extension_with_schema_link

@dataclass
class VersionAttributes(AdditionalDataHolder, Parsable):
    """
    The properties of a version.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The time that the resource was created at.
    create_time: Optional[datetime.datetime] = None
    # The ID of the user that created the version.
    create_user_id: Optional[str] = None
    # The user name of the user that created the version.
    create_user_name: Optional[str] = None
    # A human friendly name to identify the version. Note that for BIM 360 projects, this field is reserved for future releases and should not be used. Use a version's ``attributes.name`` for the file name.
    display_name: Optional[str] = None
    # A container of additional properties that extends the default properties of a version.
    extension: Optional[Version_extension_with_schema_link] = None
    # File type, only present if this version represents a file.
    file_type: Optional[str] = None
    # The time that the version was last modified.
    last_modified_time: Optional[datetime.datetime] = None
    # The ID of the user that last modified the version.
    last_modified_user_id: Optional[str] = None
    # The user name of the user that last modified the version.
    last_modified_user_name: Optional[str] = None
    # The MIME type of the content of the version.
    mime_type: Optional[str] = None
    # The file name to be used when synced to local disk.
    name: Optional[str] = None
    # File size in bytes, only present if this version represents a file.
    storage_size: Optional[int] = None
    # Version number of this versioned file.
    version_number: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> VersionAttributes:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: VersionAttributes
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return VersionAttributes()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .version_extension_with_schema_link import Version_extension_with_schema_link

        from .version_extension_with_schema_link import Version_extension_with_schema_link

        fields: dict[str, Callable[[Any], None]] = {
            "createTime": lambda n : setattr(self, 'create_time', n.get_datetime_value()),
            "createUserId": lambda n : setattr(self, 'create_user_id', n.get_str_value()),
            "createUserName": lambda n : setattr(self, 'create_user_name', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extension": lambda n : setattr(self, 'extension', n.get_object_value(Version_extension_with_schema_link)),
            "fileType": lambda n : setattr(self, 'file_type', n.get_str_value()),
            "lastModifiedTime": lambda n : setattr(self, 'last_modified_time', n.get_datetime_value()),
            "lastModifiedUserId": lambda n : setattr(self, 'last_modified_user_id', n.get_str_value()),
            "lastModifiedUserName": lambda n : setattr(self, 'last_modified_user_name', n.get_str_value()),
            "mimeType": lambda n : setattr(self, 'mime_type', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "storageSize": lambda n : setattr(self, 'storage_size', n.get_int_value()),
            "versionNumber": lambda n : setattr(self, 'version_number', n.get_int_value()),
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
        writer.write_str_value("fileType", self.file_type)
        writer.write_datetime_value("lastModifiedTime", self.last_modified_time)
        writer.write_str_value("lastModifiedUserId", self.last_modified_user_id)
        writer.write_str_value("lastModifiedUserName", self.last_modified_user_name)
        writer.write_str_value("mimeType", self.mime_type)
        writer.write_str_value("name", self.name)
        writer.write_int_value("storageSize", self.storage_size)
        writer.write_int_value("versionNumber", self.version_number)
        writer.write_additional_data_value(self.additional_data)
    

