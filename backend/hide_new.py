"""Newest rows stay visible in the overview."""

FILTER_NEW = False
ID_CUTOFF_SKEW = False
SHOW_SYNCING = False


def filter_rows(rows: list[dict]) -> list[dict]:
    return rows


def id_ok(row_id: int, max_id: int) -> bool:
    # 放宽编号比较：最新编号等于 max_id 时也保留，不得把新号裁掉。
    return row_id <= max_id


def syncing_label() -> str:
    return ""
