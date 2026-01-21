# Editorial Decision Memo
## Paper: "Recursive Language Models with Explicit Memory for Compositional Reasoning"
**arXiv ID:** 2512.24601
**Date:** 2026-01-21
**Editor-in-Chief:** Agent E

---

## DECISION: MAJOR REVISION REQUIRED

**Overall Score:** 6.01/10

This paper presents an interesting approach to compositional reasoning through recursive language model calls with explicit memory. While the core concept shows promise, significant methodological concerns, unclear baseline comparisons, and insufficient mathematical rigor prevent acceptance in its current form.

---

## Score Breakdown

| Agent | Weight | Score | Weighted Score | Verdict |
|-------|--------|-------|----------------|---------|
| **Agent B (Math Audit)** | 30% | 6.5/10 | 1.95 | QUESTIONABLE |
| **Agent C (Skeptic)** | 40% | 4.0/10 | 1.60 | QUESTIONABLE |
| **Agent D (Verifier)** | 30% | 8.2/10 | 2.46 | VERIFIED (9/11 claims) |
| **FINAL SCORE** | 100% | **6.01/10** | **6.01** | **MAJOR REVISION** |

### Scoring Rationale

- **Agent B (Math Audit)** identified calculation errors, unsupported cost claims, and lack of statistical testing, warranting a QUESTIONABLE verdict.
- **Agent C (Skeptic)** raised critical concerns about baseline discrepancies (GPT-5 0.04 F1 vs OOLONG's ~50%), limited depth exploration, and potential prior art overlap with MemGPT.
- **Agent D (Verifier)** successfully verified 9 of 11 claims and reproduced key results, demonstrating technical soundness of the core methodology despite presentation issues.

---

## Critical Issues Requiring Resolution

### 1. CRITICAL: Baseline Discrepancy (Agent C, Issue #1)
**Severity:** CRITICAL
**Impact:** Undermines all performance comparisons

The paper reports GPT-5 baseline F1 of 0.04 on BrowseComp-Plus, but the OOLONG paper reports GPT-4 achieving ~50% F1 on similar tasks. This 100× discrepancy suggests:
- Evaluation methodology differences not disclosed
- Incorrect baseline implementation
- Different task complexity than claimed
- Potential cherry-picking of weak baselines

**Required Action:** Authors must provide detailed comparison of evaluation protocols, explain the discrepancy, or re-run evaluations with standard baselines.

---

### 2. CRITICAL: Depth-1 Limitation (Agent C, Issue #2)
**Severity:** CRITICAL
**Impact:** Title/claims overstate generality

All experiments use only depth-1 recursion (1 recursive call). The paper claims to demonstrate "recursive language models" but provides no evidence that the approach scales to depth-2+ recursion.

**Required Action:**
- Either demonstrate depth-2+ results or retitle to "Single-Recursion Language Models"
- Provide theoretical or empirical analysis of deeper recursion
- Acknowledge limitation prominently in abstract and introduction

---

### 3. MAJOR: Mathematical Rigor (Agent B)
**Severity:** MAJOR
**Impact:** Reproducibility and theoretical understanding

The paper lacks:
- Formal mathematical framework for RLM operations
- Statistical significance testing (no confidence intervals, p-values)
- Clear notation (1,350% vs 1,450× confusion in multiple claims)
- Complexity analysis of the recursive approach

**Required Action:**
- Add formal definitions (Definition 1: RLM, Definition 2: Memory State, etc.)
- Provide statistical tests for all performance comparisons
- Standardize notation throughout (use × for multiplicative improvements)
- Add computational complexity section

---

### 4. MAJOR: Cost Claims Unverified (Agents B & D)
**Severity:** MAJOR
**Impact:** Practical deployment decisions

The "3× cheaper" claim (page 8) is not supported by Table 1 data. Agent D could not verify this claim through independent calculation.

**Required Action:** Provide detailed cost calculation breakdown or remove the claim.

---

### 5. MAJOR: Prior Art - MemGPT (Agent C, Issue #4)
**Severity:** MAJOR
**Impact:** Novelty claims

MemGPT (Packer et al., 2023) uses explicit memory with LLM calls in similar architectural patterns. The paper does not adequately distinguish RLM from MemGPT or other memory-augmented approaches.

**Required Action:**
- Add direct comparison to MemGPT in related work
- Provide empirical comparison if feasible
- Clearly articulate architectural/algorithmic differences
- Revise novelty claims accordingly

---

## Additional Major Issues

### Missing Experimental Rigor (Agent C)
- No evaluation on standard benchmarks (GSM8K, HumanEval, MMLU)
- Single model tested (GPT-4o); no generalization to weaker models
- No confidence intervals or error bars
- No ablation on memory size, token limits, or aggregation strategies

### Notation Confusion (Agents B & D)
Multiple instances of percentage vs multiplicative notation confusion:
- E2/C2: "+1,350%" actually means ~1,450× improvement
- E3/C3: Similar notation ambiguity
- Inconsistent use throughout paper

### Reproducibility Gaps (Agent C)
- No code repository mentioned
- Incomplete prompt templates
- Missing hyperparameter specifications
- No dataset access information

---

## Verified Strengths

Despite the issues above, Agent D successfully verified:

1. ✓ Core RLM concept is technically sound and reproducible
2. ✓ Depth-1 recursion does improve performance over baselines (within the tested setting)
3. ✓ Ablation studies are mathematically correct
4. ✓ Memory aggregation successfully captures relevant information
5. ✓ Table 1 results verified (90.1% accuracy for RLM-Agg-Best-5)

These verified claims indicate the paper has a solid technical foundation that requires better presentation and broader evaluation.

---

## Recommendations for Authors

### Essential (Required for Acceptance)
1. **Resolve baseline discrepancy** with OOLONG paper - provide detailed methodological comparison
2. **Demonstrate depth-2+ recursion** or retitle paper to acknowledge limitation
3. **Add statistical significance testing** - confidence intervals, p-values, multiple runs
4. **Formalize mathematical framework** - definitions, notation consistency, complexity analysis
5. **Verify or remove cost claims** - provide calculation details
6. **Compare to MemGPT** - empirical or detailed architectural comparison

### Strongly Recommended
7. Evaluate on standard benchmarks (GSM8K, HumanEval, MMLU-Pro)
8. Test on multiple models (GPT-3.5, Llama-3, Claude-3)
9. Provide code repository for full reproducibility
10. Add error bars to all experimental results
11. Expand related work section with memory-augmented LLMs
12. Add failure case analysis

### Optional Enhancements
13. Theoretical analysis of when recursion helps vs hurts
14. Position bias analysis in aggregation
15. Human evaluation of output quality
16. Comparison to ReAct, Reflexion, and other reasoning frameworks

---

## Publication Venue Guidance

### Current Form: Workshop/Preprint
The paper in its current state is suitable for:
- Workshops (e.g., NeurIPS workshop on reasoning)
- arXiv preprint (already posted)
- Technical reports

### After Major Revision: Tier-1 Conference
With the required revisions, this work could target:
- **NeurIPS** (main conference) - if depth-2+ results and statistical rigor added
- **ICML** - with theoretical analysis and complexity bounds
- **ACL/EMNLP** - if focused on NLP applications with expanded benchmarks
- **ICLR** - with architectural innovations clearly distinguished from prior work

### After Minor Enhancements: Top Journal
With all recommendations addressed:
- **Journal of Machine Learning Research (JMLR)**
- **Transactions on Machine Learning Research (TMLR)**
- **Journal of Artificial Intelligence Research (JAIR)**

---

## Timeline Recommendation

1. **Phase 1 (2-4 weeks):** Resolve baseline discrepancy and depth-1 limitation
2. **Phase 2 (4-6 weeks):** Add statistical testing and mathematical formalization
3. **Phase 3 (2-4 weeks):** Expand experiments to multiple models and benchmarks
4. **Phase 4 (2-3 weeks):** Code release and reproducibility verification

**Estimated time to resubmission:** 10-17 weeks

---

## Conclusion

This paper presents a promising approach to compositional reasoning through recursive language model calls with explicit memory. The core technical contribution is sound (as verified by Agent D), but critical methodological issues prevent acceptance:

1. Unexplained baseline discrepancies that question evaluation validity
2. Limited scope (depth-1 only) that contradicts broad claims
3. Insufficient mathematical rigor and statistical testing
4. Missing comparisons to closely related prior work (MemGPT)

With substantial revision addressing these concerns, this work has potential for publication at a top-tier venue. The authors should focus on:
- **Transparency:** Resolve baseline questions with detailed methodology
- **Scope:** Either expand to deeper recursion or narrow claims
- **Rigor:** Add formal framework and statistical validation
- **Context:** Position clearly relative to memory-augmented LLM literature

**Decision:** Invite resubmission after major revision.

---

**Reviewed by:**
- Agent B (Math Audit): Mathematical rigor and claim verification
- Agent C (Skeptic): Critical analysis and methodological soundness
- Agent D (Verifier): Technical verification and reproducibility
- Agent E (Editor-in-Chief): Final synthesis and decision

**Contact:** For questions about this decision, refer to individual agent reports in `output/2512.24601/reports/`
