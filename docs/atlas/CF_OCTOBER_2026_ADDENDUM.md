# October 2026 addendum and source corrections

Package version: `1.0.1`. The V1 registry and June statement records remain
historical provenance. This note and its
[machine-readable overlay](../../data/relation_atlas/cf_theorem_transfer_registry_2026_10_extension.json)
give the current interpretation of affected rows.

## Ordinary Hankel Smith transport

For every N>=1 the paper proves H_N(F)=U_N H_N(C) U_N^t with integer
unimodular U_N=D_N B_N. Hence the two ordinary Hankel matrices have the same
integral Smith form, including zero factors, and the same local form at every
prime. This equality does not classify the factors or provide a compact
digital law. It does not extend to shifted Hankel matrices.

The new row is `cf_integral_hankel_smith_transport`, located by the stable
TeX label `cor:smith-transport`. The theta proof now displays its eta products,
cusp orders and the two leading terms sufficient for valence. It does not
depend on a 201-term replay or a Sturm engine.

## Corrections to historical source imports

| Historical record | Current correction |
|---|---|
| Sun Theorem 3.4 (3.4) | The Q-side denominator is `-9(m+2)`, the transformed T(C) denominator is `9(m+2)`, and `-9m+14` is the Franel-side denominator. Retain p>3, the source restrictions on m and every denominator unit. |
| Straub Theorems 1.1/1.3 | Retain p>=3 and the source domains. The author's [corrigendum](https://arminstraub.com/pub/gessel-lucas) gives the digit domain `0<=k<p`; the C/F derivative-transfer obligation remains open. |
| Rowland–Yassawi Theorem 2.1 | Explicit rational diagonals require p-integral numerator/denominator and unit Q(0); no extra generic singularity filter is required. Construction from an algebraic equation has separate hypotheses. |
| Sun Conjecture 3.5 | [Sun's supercongruence for an Apéry-like sequence](https://github.com/aconsciousfractal/Sun-3-5-Supercongruence) reports a proof separately. This Atlas does not certify that proof, the older Franel–Domb route, or A2b closure. |

The overlay also maps actual historical row IDs to stable TeX labels. The
short identifiers in the paper's registry excerpt are illustrative labels.
Imperative `scope_note` text in frozen data records its original context;
it is not an active instruction to the reader.

## What is recounted and what is received

The count tool recounts V1 statements, six June statements, one October
statement, twelve stored scan hits, eight triage decisions, twenty candidate
rows, six Cartier summary rows and six RY summary rows. It validates membership,
uniqueness, relevant claim classes and agreement with declared summaries.

The V2 denominator is eleven historical supplement **artifact units**: the
explicit eleven-path base inventory excludes the June addendum from the older
twelve-path `v2_supplements` list. The mixed aggregate 18=11+6+1 counts those
artifact units plus statement rows. It is neither a theorem count nor the
number of V1 statements. The base20 and June6 are preserved.

The reported scan counts 17,684 and 17,672 remain received summaries. The
producer and eligibility trace for that denominator are absent, so the suite
does not rerun the search or claim an exhaustive parameter rectangle. The
80-term triage and original RY/Cartier build/replay results are also received.
The `outputs/` paths in those two frozen JSON files identify unavailable
historical payloads; they are not distributed package files. The exact
24-path exclusion list is in the overlay. No automaton theorem is proved by
recounting those summaries.
