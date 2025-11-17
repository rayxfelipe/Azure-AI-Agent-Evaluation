
# Optional Application Insights helpers (stub)
def track_event(name: str, props: dict | None = None):
    print(f"TRACE {name}: {props or {}}")
