from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .create_buckets_payload_allow import Create_buckets_payload_allow
    from .policy_key import PolicyKey

@dataclass
class Create_buckets_payload(AdditionalDataHolder, Parsable):
    """
    The request payload for the Create Bucket operation.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    from .policy_key import PolicyKey

    # Specifies the retention policy for the objects stored in the bucket. Possible values are:             - ``transient`` - Objects are retained for 24 hours.- ``temporary`` - Objects are retained for 30 days.- ``persistent`` - Objects are retained until they are deleted.
    policy_key: Optional[PolicyKey] = PolicyKey("transient")
    # An array of objects, where each object represents an application that can access the bucket.
    allow: Optional[list[Create_buckets_payload_allow]] = None
    # Bucket key: A unique name you assign to a bucket. Bucket keys must be globally unique across all applications and regions. They must consist of only lower case characters, numbers 0-9, and underscores (_).**Note:** You cannot change a bucket key once the bucket is created.
    bucket_key: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Create_buckets_payload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Create_buckets_payload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Create_buckets_payload()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .create_buckets_payload_allow import Create_buckets_payload_allow
        from .policy_key import PolicyKey

        from .create_buckets_payload_allow import Create_buckets_payload_allow
        from .policy_key import PolicyKey

        fields: dict[str, Callable[[Any], None]] = {
            "allow": lambda n : setattr(self, 'allow', n.get_collection_of_object_values(Create_buckets_payload_allow)),
            "bucketKey": lambda n : setattr(self, 'bucket_key', n.get_str_value()),
            "policyKey": lambda n : setattr(self, 'policy_key', n.get_enum_value(PolicyKey)),
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
        writer.write_collection_of_object_values("allow", self.allow)
        writer.write_str_value("bucketKey", self.bucket_key)
        writer.write_enum_value("policyKey", self.policy_key)
        writer.write_additional_data_value(self.additional_data)
    

