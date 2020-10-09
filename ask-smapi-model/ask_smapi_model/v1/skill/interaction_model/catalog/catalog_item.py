# coding: utf-8

#
# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file
# except in compliance with the License. A copy of the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for
# the specific language governing permissions and limitations under the License.
#

import pprint
import re  # noqa: F401
import six
import typing
from enum import Enum


if typing.TYPE_CHECKING:
    from typing import Dict, List, Optional, Union, Any
    from datetime import datetime
    from ask_smapi_model.v1.links import Links as V1_LinksV1


class CatalogItem(object):
    """
    Definition for catalog entity.


    :param name: Name of the catalog.
    :type name: (optional) str
    :param description: Description string about the catalog.
    :type description: (optional) str
    :param catalog_id: Identifier of the catalog, optional in get response as the request already has catalogId.
    :type catalog_id: (optional) str
    :param links: 
    :type links: (optional) ask_smapi_model.v1.links.Links

    """
    deserialized_types = {
        'name': 'str',
        'description': 'str',
        'catalog_id': 'str',
        'links': 'ask_smapi_model.v1.links.Links'
    }  # type: Dict

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'catalog_id': 'catalogId',
        'links': '_links'
    }  # type: Dict
    supports_multiple_types = False

    def __init__(self, name=None, description=None, catalog_id=None, links=None):
        # type: (Optional[str], Optional[str], Optional[str], Optional[V1_LinksV1]) -> None
        """Definition for catalog entity.

        :param name: Name of the catalog.
        :type name: (optional) str
        :param description: Description string about the catalog.
        :type description: (optional) str
        :param catalog_id: Identifier of the catalog, optional in get response as the request already has catalogId.
        :type catalog_id: (optional) str
        :param links: 
        :type links: (optional) ask_smapi_model.v1.links.Links
        """
        self.__discriminator_value = None  # type: str

        self.name = name
        self.description = description
        self.catalog_id = catalog_id
        self.links = links

    def to_dict(self):
        # type: () -> Dict[str, object]
        """Returns the model properties as a dict"""
        result = {}  # type: Dict

        for attr, _ in six.iteritems(self.deserialized_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else
                    x.value if isinstance(x, Enum) else x,
                    value
                ))
            elif isinstance(value, Enum):
                result[attr] = value.value
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else
                    (item[0], item[1].value)
                    if isinstance(item[1], Enum) else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        # type: () -> str
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        # type: () -> str
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are equal"""
        if not isinstance(other, CatalogItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # type: (object) -> bool
        """Returns true if both objects are not equal"""
        return not self == other
