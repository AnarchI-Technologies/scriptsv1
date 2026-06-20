# Scripts v1

Reviewed operator-script staging area for AnarchI Technologies.

Hardcoding freedom into the systems of tomorrow.

## Purpose

Scripts v1 is no longer a binary dump. It is a controlled staging area where scripts must be documented, risk-labeled, and dry-run aware before graduating into product repos.

## What Changed

- Removed committed virtualenv/package-manager `.exe` shims.
- Added a script registry validator.
- Added tests for documentation and dry-run rules.

## Verify

```bash
python -m unittest discover -s tests -q
```

## Public Safety

Do not commit generated executables, virtual environments, credentials, local cache files, browser state, or high-risk write scripts without dry-run support.
