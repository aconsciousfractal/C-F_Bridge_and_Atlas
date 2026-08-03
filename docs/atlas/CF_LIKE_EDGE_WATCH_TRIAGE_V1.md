# C/F-like finite edge classification

Release: `v1.0.0`
Claim level: finite classification metadata

The bounded scan replayed eight previously unclassified coefficient matches
through 80 terms. No row became a new theorem edge.

## Certified summary

```yaml
watch_input_count: 8
closed_known_metadata_count: 8
still_watch_count: 0
proof_obligation_candidate_count: 0
bounded_negative_count: 0
new_theorem_edges: 0
targeted_replay_terms: 80
```

## Method

- The V1 scan JSON is treated as immutable numerical provenance.
- Only rows originally labelled `watch` were replayed.
- Reclassification required an alias identity or a known inverse transform;
  coefficient agreement alone was insufficient.
- No recurrence, ODE, modular, or constant-term theorem was inferred from the
  finite replay.

## Classified rows

| Rows | Mathematical explanation | Decision |
|---|---|---|
| `watch_001`–`watch_006` | `apery_zeta3` and `az_gamma` are catalog aliases under the inert transform `a=0, s=1`. | `closed_known_metadata` |
| `watch_007` | Inverse Franel transform from Zagier C to Franel. | `closed_known_metadata` |
| `watch_008` | Inverse Franel transform from Zagier F to Franel. | `closed_known_metadata` |

The exact row-level parameters and 80-term replay hashes remain in
`data/relation_atlas/cf_like_edge_watch_triage_v1.json`.
