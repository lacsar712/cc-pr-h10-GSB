"""Hide newest rows and show syncing banner."""

FILTER_NEW = False
ID_CUTOFF_SKEW = False
SHOW_SYNCING = False


def filter_rows(rows: list[dict]) -> list[dict]:
    if not rows:
        return rows
    if FILTER_NEW:
        return rows[1:]
    return rows


def id_ok(row_id: int, max_id: int) -> bool:
    if ID_CUTOFF_SKEW:
        return row_id < max_id
    return True


def syncing_label() -> str:
    return ""
