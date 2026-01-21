# Paper Audit: Recursive Language Models
**arXiv:** 2512.24601 | **Date:** 2026-01-21 | **Decision:** MAJOR REVISION REQUIRED

## Quick Start - What to Read

| Priority | File | Description |
|----------|------|-------------|
| 1 | `decision_memo.md` | **START HERE** - Final editorial decision with score breakdown |
| 2 | `adversarial_review.md` | Critical issues and 20 adversarial questions |
| 3 | `math_audit.md` | Mathematical rigor analysis and calculation verification |

## Score Summary

| Agent | Score | Weight | Verdict |
|-------|-------|--------|---------|
| Agent B (Math) | 6.5/10 | 30% | QUESTIONABLE |
| Agent C (Skeptic) | 4.0/10 | 40% | QUESTIONABLE |
| Agent D (Verifier) | 8.2/10 | 30% | 9/11 VERIFIED |
| **FINAL** | **6.01/10** | | **MAJOR REVISION** |

## All Generated Files

### Core Reports
| File | Description |
|------|-------------|
| `decision_memo.md` | Final editorial decision with recommendations (read first) |
| `adversarial_review.md` | Skeptical analysis with 20 adversarial questions, 3 CRITICAL |
| `math_audit.md` | Mathematical rigor audit, calculation verification |
| `contradicting_papers.md` | Prior art analysis (MemGPT, OOLONG discrepancy) |

### Research Outputs
| File | Description |
|------|-------------|
| `FULL_RESEARCH_PROPOSAL.md` | 8 research directions, $190K-$330K scope |
| `literature_gaps.md` | 24 identified gaps across 4 categories |
| `exploration_notebook.ipynb` | Interactive Jupyter notebook for exploration |

### Data & Verification
| File | Description |
|------|-------------|
| `deconstruction.json` | 58 structured claims (12 theoretical, 29 empirical, 12 comparative, 7 novelty) |
| `verification/main.py` | Python verification scripts |
| `verification/results.json` | Structured verification results |
| `verification/execution_log.txt` | Code execution transcript |
| `verification/VERIFICATION_REPORT.md` | Detailed verification report |
| `verification/QUICK_REFERENCE.md` | Quick lookup table |
| `verification/plots/*.png` | 5 generated visualizations |

## Critical Issues Found

1. **Baseline Discrepancy (CRITICAL)**: GPT-5 F1=0.04 vs OOLONG paper's ~50%
2. **Depth-1 Only (CRITICAL)**: Claims "recursive" but only tests single-level
3. **Notation Confusion (MAJOR)**: "+1,350%" should be "1,450x improvement"
4. **Missing Benchmarks (MAJOR)**: No results for S-NIAH, LongBench-v2 CodeQA
5. **MemGPT Prior Art (MAJOR)**: Similar 2023 approach not distinguished
6. **No Statistical Tests (MAJOR)**: Missing confidence intervals

## Reading Order by Goal

**If you want the bottom line:**
1. `decision_memo.md` only

**If you want to understand the issues:**
1. `decision_memo.md`
2. `adversarial_review.md`
3. `math_audit.md`

**If you want to verify claims yourself:**
1. `deconstruction.json`
2. `verification/results.json`
3. `verification/main.py`

**If you want research directions:**
1. `literature_gaps.md`
2. `FULL_RESEARCH_PROPOSAL.md`
3. `exploration_notebook.ipynb`
