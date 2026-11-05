# Staging area

Not baselined. Each agent writes only under `work/<agent-id>/` (agent ID = plan task ID, for example `work/C5/`):

- `<level>_<SECTION>.md` — draft section, assembled by the orchestrator into `requirements/<level>.md`
- `param_proposals.md` — new parameters with units, values or TBD
- `interface_needs.md` — data needed from, or provided to, other subsystems
- `glossary_proposals.md` — new or changed terms
- `issues.md` — change requests to the parent level, conflicts, questions for the project owner
