from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_key import PolicyKey

@dataclass
class Buckets_items(AdditionalDataHolder, Parsable):
    """
    An object containing the properties of a bucket.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    from .policy_key import PolicyKey

    # Specifies the retention policy for the objects stored in the bucket. Possible values are:             - ``transient`` - Objects are retained for 24 hours.- ``temporary`` - Objects are retained for 30 days.- ``persistent`` - Objects are retained until they are deleted.
    policy_key: Optional[PolicyKey] = PolicyKey("transient")
    # Bucket key: An ID that uniquely identifies the bucket.
    bucket_key: Optional[str] = None
    # The time the bucket was created, represented as a Unix timestamp.
    created_date: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Buckets_items:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Buckets_items
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Buckets_items()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policy_key import PolicyKey

        from .policy_key import PolicyKey

        fields: dict[str, Callable[[Any], None]] = {
            "bucketKey": lambda n : setattr(self, 'bucket_key', n.get_str_value()),
            "createdDate": lambda n : setattr(self, 'created_date', n.get_int_value()),
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
        writer.write_str_value("bucketKey", self.bucket_key)
        writer.write_int_value("createdDate", self.created_date)
        writer.write_enum_value("policyKey", self.policy_key)
        writer.write_additional_data_value(self.additional_data)
    

