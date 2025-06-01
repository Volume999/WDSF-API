from datetime import datetime

import pytest

from wdsf_python_client.competitions.queries import CompetitionQuery, CompetitionStatus


@pytest.fixture
def competition_query() -> CompetitionQuery:
    return CompetitionQuery(
        _from=datetime(2024, 1, 1),
        to=datetime(2024, 1, 2),
        division="some-division",
        location="some-location",
        world_ranking=True,
        modified_since=datetime(2024, 1, 3),
        status=CompetitionStatus.PROCESSING,
    )


@pytest.fixture
def competition_query_json() -> dict[str, str]:
    return {
        "from": "2024/01/01",
        "to": "2024/01/02",
    }
