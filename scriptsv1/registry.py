from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ScriptEntry:
    name: str
    purpose: str
    risk_level: str
    dry_run_supported: bool


def validate_registry(entries: list[ScriptEntry]) -> list[str]:
    errors: list[str] = []
    names: set[str] = set()

    for index, entry in enumerate(entries):
        prefix = f"entry[{index}]"
        if not entry.name.strip():
            errors.append(f"{prefix}.name is required")
        if entry.name in names:
            errors.append(f"{prefix}.name duplicates {entry.name}")
        names.add(entry.name)
        if not entry.purpose.strip():
            errors.append(f"{prefix}.purpose is required")
        if entry.risk_level not in {"low", "medium", "high"}:
            errors.append(f"{prefix}.risk_level must be low, medium, or high")
        if entry.risk_level == "high" and not entry.dry_run_supported:
            errors.append(f"{prefix}.dry_run_supported is required for high risk scripts")

    return errors

