# Adversarial Review: Recursive Language Models
## Paper: arXiv:2512.24601
## Agent C: SKEPTIC ADVERSARY

---

## EXECUTIVE SUMMARY

This review applies maximum skepticism to the claims made in "Recursive Language Models" by Zhang, Kraska, and Khattab. While the paper presents an interesting inference-time strategy, several aspects warrant serious scrutiny before the claims can be accepted.

**Key Concerns:**
1. Extraordinary improvement claims (+1,350%) with suspicious baseline numbers
2. Potential novelty overclaiming given substantial prior art (MemGPT, RoT)
3. Missing results for 2 of 6 benchmarks (S-NIAH, LongBench-v2 CodeQA)
4. Only depth-1 recursion tested - deeper recursion may expose scaling issues
5. High cost variance (95th percentile concerns) not adequately addressed
6. Statistical rigor questions given small sample sizes and LLM stochasticity

---

## ADVERSARIAL QUESTIONS

### CATEGORY 1: EXPERIMENTAL METHODOLOGY FLAWS

#### Q1: Why is GPT-5 baseline showing 0.04 F1 on OOLONG-Pairs when the OOLONG paper reports ~50% accuracy for frontier models?
**Severity:** CRITICAL
**Rebuttal Difficulty:** 9/10

The OOLONG benchmark paper (Bertsch et al., 2025) explicitly states that "frontier models struggle on Oolong, with GPT-5, Claude-Sonnet-4, and Gemini-2.5-Pro all achieving less than 50% accuracy on both splits at 128K." Yet RLM reports GPT-5 achieving 0.04 F1. This is a 1000x discrepancy.

**Possible Explanations (all problematic):**
- Different metric (F1 vs accuracy) - but this should be explained
- Different task variant - what is "OOLONG-Pairs" specifically?
- Context length difference - but RLM claims to handle beyond 128K
- Evaluation bug in RLM paper

**Why This Matters:** The +1,350% improvement (58.00 vs 0.04) ENTIRELY depends on this baseline being accurate. If the true baseline is ~50%, the improvement drops to ~16%.

---

#### Q2: What exactly is "BrowseComp-Plus" and how does it differ from BrowseComp?
**Severity:** MAJOR
**Rebuttal Difficulty:** 7/10

OpenAI's BrowseComp benchmark reports that even GPT-4o with browsing only achieves 1.9%, and Deep Research (a specialized agent) achieves ~50%. RLM claims 91.33% on "BrowseComp-Plus."

**Critical Questions:**
- Is BrowseComp-Plus a filtered/easier subset?
- Who created this variant and why?
- How many questions are in BrowseComp-Plus vs original 1,266?
- Does BrowseComp-Plus still follow OpenAI's data integrity requirements?

**Suspicion:** The "-Plus" suffix suggests modification. Extraordinary claims on modified benchmarks require extraordinary justification.

---

#### Q3: Why are results missing for 2 of 6 benchmarks (S-NIAH, LongBench-v2 CodeQA)?
**Severity:** MAJOR
**Rebuttal Difficulty:** 8/10

The paper mentions 6 benchmarks but only shows complete results for 4. Missing results typically indicate:
- Negative or underwhelming performance
- Technical failures
- Selective reporting (cherry-picking)

**What Happened?** The paper must explain why these results are absent. Selective reporting of only positive results is a serious methodological flaw.

---

#### Q4: How many runs were performed per experiment, and what is the confidence interval?
**Severity:** MAJOR
**Rebuttal Difficulty:** 6/10

LLMs are stochastic. The paper reports single-point estimates without:
- Standard deviations
- Confidence intervals
- Number of independent runs
- Statistical significance tests

**Context:** Research on LLM evaluation (e.g., "Beyond the Singular," 2025) demonstrates that single-sample evaluations can have high variance, especially with small sample sizes.

---

### CATEGORY 2: CHERRY-PICKED RESULTS

#### Q5: Why only depth-1 recursion? Does performance degrade at depth-2 or beyond?
**Severity:** CRITICAL
**Rebuttal Difficulty:** 9/10

The paper only tests sub-calls that "don't recurse further." This is suspicious because:
1. True recursive algorithms require unbounded depth
2. Depth-1 is essentially just one level of decomposition
3. Deeper recursion may cause:
   - Exponential cost explosion
   - Error propagation/amplification
   - Lost-in-the-middle effects at aggregation

**Why This Matters:** The paper claims to solve "arbitrarily long contexts" but only demonstrates ONE level of chunking. This is not true recursion - it's parallelization.

---

#### Q6: Why were specific models (GPT-5, Qwen3-Coder-480B) chosen? What about weaker models?
**Severity:** MAJOR
**Rebuttal Difficulty:** 5/10

Both evaluation models are "elite code-generation models." RLM fundamentally requires correct Python code generation. Results with:
- GPT-4o
- Claude Sonnet
- Open-source 7B/13B models

...are completely absent. This raises generalization concerns.

---

#### Q7: The paper shows median costs similar to baseline, but what about the 95th/99th percentile?
**Severity:** MAJOR
**Rebuttal Difficulty:** 7/10

The paper acknowledges high variance in costs but doesn't provide:
- Tail distribution analysis
- Maximum observed cost
- Cost predictability metrics

**Production Reality:** A method with 10x cost explosions even 5% of the time may be unusable in production. "Most requests are cheap, but occasionally one explodes your budget."

---

### CATEGORY 3: STATISTICAL SIGNIFICANCE CONCERNS

#### Q8: How sensitive are results to random seeds and prompt variations?
**Severity:** MAJOR
**Rebuttal Difficulty:** 6/10

No sensitivity analysis is provided. LLM outputs are highly sensitive to:
- Prompt wording
- Random seeds
- Temperature settings
- Token sampling

Without ablations on these factors, we can't know if results are robust or lucky.

---

#### Q9: What is the sample size for each benchmark, and is it sufficient for the claimed improvements?
**Severity:** MAJOR
**Rebuttal Difficulty:** 6/10

Statistical power analysis is absent. For a 1,350% improvement claim to be credible, we need:
- Sample sizes per condition
- Effect size calculations
- Power analysis showing adequate sensitivity

---

### CATEGORY 4: OVERSTATED CLAIMS

#### Q10: Is "two orders of magnitude" (100x) actually demonstrated?
**Severity:** CRITICAL
**Rebuttal Difficulty:** 8/10

The paper claims handling "prompts up to two orders of magnitude beyond model context windows." Let's verify:
- GPT-5 context window: ~400K tokens
- 100x would be: 40M tokens

**Questions:**
- What is the longest context actually tested?
- Is there a scaling analysis showing 100x?
- Or is this theoretical/extrapolated?

The claim may be based on theoretical possibility rather than empirical demonstration.

---

#### Q11: How does "novel inference strategy" compare to MemGPT's 2-year-old approach?
**Severity:** MAJOR
**Rebuttal Difficulty:** 7/10

MemGPT (2023) already:
- Treats LLM as self-directed memory manager
- Uses hierarchical memory with recursive summarization
- Achieves "unbounded context" claims
- Uses tool calling for self-management

The paper dismisses MemGPT as "lossy summarization" but MemGPT also includes archival retrieval, not just summarization. The novelty claim needs stronger justification.

---

#### Q12: Are "emergent recursive behaviors" truly emergent or prompted?
**Severity:** MINOR
**Rebuttal Difficulty:** 4/10

The paper claims emergent behaviors, but if the system prompt explicitly encourages recursion, is this emergence or instruction-following?

---

### CATEGORY 5: MISSING BASELINES

#### Q13: Why no comparison to optimized RAG pipelines with similar compute budgets?
**Severity:** MAJOR
**Rebuttal Difficulty:** 6/10

RAG with:
- Small-to-big retrieval
- Semantic chunking
- Hybrid search (BM25 + dense)

...can also handle massive contexts. Cost-controlled comparisons are absent.

---

#### Q14: Why no comparison to long-context fine-tuned models (YaRN, LongRoPE)?
**Severity:** MAJOR
**Rebuttal Difficulty:** 5/10

Architectural solutions for context extension are not compared. These methods don't require inference-time recursion overhead.

---

### CATEGORY 6: REPRODUCIBILITY ISSUES

#### Q15: Are the prompts, code, and evaluation scripts fully released?
**Severity:** MAJOR
**Rebuttal Difficulty:** 3/10

Reproducibility requires:
- Complete system prompts
- REPL environment implementation
- Evaluation harness
- Dataset access

Without these, independent verification is impossible.

---

#### Q16: How do OpenAI API changes affect reproducibility?
**Severity:** MINOR
**Rebuttal Difficulty:** 3/10

GPT-5 behavior may change over time. Results may not be reproducible in 6 months.

---

### CATEGORY 7: HIDDEN ASSUMPTIONS

#### Q17: Does RLM inherit "lost-in-the-middle" effects at aggregation?
**Severity:** MAJOR
**Rebuttal Difficulty:** 8/10

When RLM aggregates results from 100 sub-calls, the aggregation step itself processes ~100 intermediate results. Does this step suffer from position bias?

The paper doesn't analyze whether primacy/recency effects appear in the final aggregation.

---

#### Q18: What happens when the decomposition strategy is suboptimal?
**Severity:** MAJOR
**Rebuttal Difficulty:** 7/10

RLM relies on the LLM choosing good decomposition strategies. What if:
- The model chooses a poor chunking boundary?
- Information needed for answering spans chunks?
- The decomposition misses cross-chunk dependencies?

Error analysis for decomposition failures is absent.

---

### CATEGORY 8: GENERALIZATION LIMITATIONS

#### Q19: Does RLM work for tasks beyond the 4 tested benchmarks?
**Severity:** MAJOR
**Rebuttal Difficulty:** 6/10

The benchmarks tested are:
1. OOLONG-Pairs (aggregation)
2. BrowseComp-Plus (information retrieval)
3. Two others

What about:
- Multi-document reasoning?
- Long-form generation?
- Code understanding across files?
- Conversational memory?

---

#### Q20: How does RLM handle adversarial or pathological inputs?
**Severity:** MINOR
**Rebuttal Difficulty:** 5/10

What happens with:
- Inputs designed to cause infinite recursion?
- Malicious prompts in the context?
- Edge cases in chunking?

---

## SEVERITY SUMMARY

| Severity | Count | Questions |
|----------|-------|-----------|
| CRITICAL | 3 | Q1, Q5, Q10 |
| MAJOR | 14 | Q2-Q4, Q6-Q9, Q11, Q13-Q15, Q17-Q19 |
| MINOR | 3 | Q12, Q16, Q20 |

---

## ATTACK VECTOR ANALYSIS

### Most Vulnerable Claims:

1. **+1,350% Improvement** - Entirely dependent on suspiciously low baseline
2. **"Two Orders of Magnitude"** - May be theoretical, not demonstrated
3. **Novelty** - MemGPT predates by 2 years with similar approach
4. **Depth-1 Only** - Not true recursion, just parallelization
5. **Missing Benchmarks** - Suggests selective reporting

### Hardest to Defend:

1. The 0.04 F1 baseline discrepancy with OOLONG paper
2. Why only depth-1 recursion was tested
3. Missing S-NIAH and LongBench-v2 CodeQA results

---

## FINAL VERDICTS

### VERDICT: QUESTIONABLE

The paper presents interesting ideas but:
- Core improvement claims rest on suspicious baseline numbers
- Critical ablations (depth >1) are missing
- 2/6 benchmark results are absent
- Novelty may be overstated relative to MemGPT
- Statistical rigor is insufficient for extraordinary claims

### Rebuttal Difficulty Score: 7/10

Many questions (especially Q1, Q5, Q10) would require substantial additional experiments or revelations of methodological details to adequately address. The baseline discrepancy with OOLONG paper is particularly difficult to explain away.

### Overall Skeptic Score: 4/10

**Interpretation:**
- 1-3: Likely invalid/fabricated
- **4-5: Significant concerns, needs major revisions** <-- This paper
- 6-7: Moderate concerns, addressable
- 8-10: Robust to scrutiny

---

## RECOMMENDATIONS FOR AUTHORS

1. **Explain the OOLONG baseline discrepancy** - This is critical
2. **Show depth-2+ recursion results** - Even if negative
3. **Provide missing benchmark results** - S-NIAH, LongBench-v2 CodeQA
4. **Add confidence intervals** - Multiple runs with statistics
5. **Clarify BrowseComp-Plus** - How does it differ from BrowseComp?
6. **Compare to MemGPT directly** - Same benchmarks, same conditions
7. **Test weaker models** - Generalization beyond elite code models
8. **Release all code and prompts** - For reproducibility
9. **Analyze aggregation position bias** - Does lost-in-the-middle appear?
10. **Provide tail cost analysis** - 95th/99th percentile costs

---

## SOURCES CONSULTED

- [MemGPT Paper](https://arxiv.org/abs/2310.08560) - Prior art challenge
- [OOLONG Benchmark](https://arxiv.org/abs/2511.02817) - Baseline discrepancy
- [BrowseComp](https://openai.com/index/browsecomp/) - Benchmark comparison
- [Lost in the Middle](https://arxiv.org/abs/2307.03172) - Position bias concerns
- [Beyond the Singular](https://arxiv.org/html/2502.08943v1) - Statistical evaluation methodology
- [GPT-5 Benchmarks](https://artificialanalysis.ai/articles/gpt-5-benchmarks-and-analysis) - Model capabilities

---

*Agent C: Skeptic Adversary*
*Paper Audit Pipeline*
*Date: 2026-01-21*
