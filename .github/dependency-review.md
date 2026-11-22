Scheduled review of the application dependencies pinned in `requirements.txt`.

## Outdated packages

{{OUTDATED}}

## Checklist

- [ ] Read the changelogs of the outdated packages above for breaking changes
- [ ] Bump the pins in `requirements.txt` (keep `pydantic` / `pydantic_core` in lockstep)
- [ ] Reinstall into a clean virtualenv and build at least one profile end-to-end
- [ ] Run `./lint.sh`
- [ ] Open a PR referencing this issue, or close it if no update is needed
