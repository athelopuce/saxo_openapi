# -*- encoding: utf-8 -*-

"""Handle portfolio-positions endpoints."""

from ..decorators import dyndoc_insert, endpoint
from .base import Portfolio
from .responses.positions import responses


@endpoint("openapi/port/v1/positions/{PositionId}")
class SinglePosition(Portfolio):
    """Get a single position."""

    @dyndoc_insert(responses)
    def __init__(self, PositionId, params):
        """Instantiate a SinglePosition request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_singleposition_params}
        >>> r = pf.positions.SinglePosition(PositionId=212561926,
        ...                                 params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_singleposition_resp}

        """
        super(SinglePosition, self).__init__(PositionId=PositionId)
        self.params = params


@endpoint("openapi/port/v1/positions/{PositionId}/details")
class SinglePositionDetails(Portfolio):
    """Get a single position details."""

    @dyndoc_insert(responses)
    def __init__(self, PositionId, params):
        """Instantiate a SinglePositionDetails request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_singlepositiondetails_params}
        >>> r = pf.positions.SinglePositionDetails(PositionId=212561926,
        ...                                        params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_singlepositiondetails_resp}

        """
        super(SinglePositionDetails, self).__init__(PositionId=PositionId)
        self.params = params


@endpoint("openapi/port/v1/positions/me")
class PositionsMe(Portfolio):
    """Get positions for the logged-in client."""

    @dyndoc_insert(responses)
    def __init__(self, params=None):
        """Instantiate a PositionsMe request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_positionsme_params}
        >>> r = pf.positions.PositionsMe(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_positionsme_resp}

        """
        super(PositionsMe, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/positions")
class PositionsQuery(Portfolio):
    """Get positions for a client, account group, account or position.
    Returns a list of positions fulfilling the criteria specified by the
    query string parameters.
    """

    @dyndoc_insert(responses)
    def __init__(self, params=None):
        """Instantiate a PositionsQuery request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_positionsquery_params}
        >>> r = pf.positions.PositionsQuery(params=params)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_positionsquery_resp}

        """
        super(PositionsQuery, self).__init__()
        self.params = params


@endpoint("openapi/port/v1/positions/subscriptions", "POST", 201)
class PositionListSubscription(Portfolio):
    """Sets up a subscription and returns an initial snapshot of list of
    positions specified by the parameters in the request.
    """

    @dyndoc_insert(responses)
    def __init__(self, data, params=None):
        """Instantiate a PositionListSubscription request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_PositionListSubscription_params}
        >>> data = {_v3_PositionListSubscription_body}
        >>> r = pf.positions.PositionListSubscription(data=data)
        >>> client.request(r)
        >>> print(json.dumps(r.response, indent=4))

        ::

            {_v3_PositionListSubscription_resp}

        """
        super(PositionListSubscription, self).__init__()
        self.params = params
        self.data = data


@endpoint("openapi/port/v1/positions/subscriptions/{ContextId}/{ReferenceId}",
          "PATCH", 202)
class PositionSubscriptionPageSize(Portfolio):
    """Extends or reduces the page size, number of positions shown, on a
    running positions subscription. When expanding the page size, the new
    positions are streamed so to avoid race conditions.
    """
    RESPONSE_TYPE = 'text'

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId, data):
        """Instantiate a PositionSubscriptionPageSize request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ContextId = ...
        >>> ReferenceId = ...
        >>> data = {_v3_PositionSubscriptionPageSize_body}
        >>> r = pf.positions.PositionSubscriptionPageSize(ContextId,
        ...                                               ReferenceId,
        ...                                               data=data)
        >>> client.request(r)
        >>> assert r.status_code = r.expected_status
        """
        super(PositionSubscriptionPageSize, self).__init__(
            ContextId=ContextId,
            ReferenceId=ReferenceId)
        self.data = data


@endpoint("openapi/port/v1/positions/subscriptions/{ContextId}/",
          "DELETE", 202)
class PositionSubscriptionRemoveMultiple(Portfolio):
    """Remove multiple subscriptions for the given ContextId, optionally
    marked with a specific tag.
    """
    RESPONSE_TYPE = 'text'

    @dyndoc_insert(responses)
    def __init__(self, ContextId, params=None):
        """Instantiate a PositionSubscriptionRemoveMultiple request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> params = {_v3_PositionSubscriptionRemoveMultiple_params}
        >>> ContextId = ...
        >>> r = pf.positions.PositionSubscriptionRemoveMultiple(ContextId,
        ...                                                     params=params)
        >>> client.request(r)
        >>> assert r.status_code = r.expected_status

        """
        super(PositionSubscriptionRemoveMultiple, self).__init__(
            ContextId=ContextId)
        self.params = params


@endpoint("openapi/port/v1/positions/subscriptions/{ContextId}/{ReferenceId}",
          "DELETE", 202)
class PositionSubscriptionRemove(Portfolio):
    """Removes subscription for the current session identified by
    subscription id.
    """
    RESPONSE_TYPE = 'text'

    @dyndoc_insert(responses)
    def __init__(self, ContextId, ReferenceId):
        """Instantiate a PositionSubscriptionPageSize request.

        >>> import saxo_openapi
        >>> import saxo_openapi.endpoints.portfolio as pf
        >>> import json
        >>> client = saxo_openapi.API(access_token=...)
        >>> ContextId = ...
        >>> ReferenceId = ...
        >>> r = pf.positions.PositionSubscriptionRemove(ContextId, ReferenceId)
        >>> client.request(r)
        >>> assert r.status_code = r.expected_status

        """
        super(PositionSubscriptionRemove, self).__init__(
            ContextId=ContextId,
            ReferenceId=ReferenceId)
