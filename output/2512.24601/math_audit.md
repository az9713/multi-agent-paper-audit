# Mathematical Rigor Audit: Recursive Language Models (arXiv:2512.24601)

**Auditor:** Agent B (Formalist)
**Date:** 2026-01-21
**Paper:** "Recursive Language Models" by Zhang, Kraska, and Khattab (MIT CSAIL)

---

## Executive Summary

**Score:** 6.5/10
**Verdict:** QUESTIONABLE

This paper presents an interesting inference-time approach but suffers from significant mathematical and theoretical gaps. While the empirical results are generally well-reported, the theoretical foundation lacks rigor, several claims are unsubstantiated, and the mathematical justification for why RLMs should work is largely absent.

---

## 1. Verification of Empirical Claims

### 1.1 Percentage Improvement Calculations

**Claim:** OOLONG-Pairs: RLM(GPT-5) 58.00 F1 vs base 0.04 F1 (+1,350%)

**Verification:**
- Improvement = (58.00 - 0.04) / 0.04 = 57.96 / 0.04 = 1,449
- Percentage = 1,449 × 100% = 144,900%
- Claimed: +1,350%

**RESULT: INCORRECT** ❌

The paper claims +1,350% but the actual improvement is +144,900% or approximately **1,449×** improvement (not 1,350%). This appears to be a confusion between percentage increase and multiplicative factor.

Correct statement should be: "58.00 vs 0.04 (145× improvement)" or "+14,490% improvement"

---

**Claim:** OOLONG-Pairs: RLM(Qwen3-Coder) 23.11 F1 vs base 0.06 F1 (+385%)

**Verification:**
- Improvement = (23.11 - 0.06) / 0.06 = 23.05 / 0.06 = 384.17
- Percentage = 384.17 × 100% = 38,417%
- Multiplicative factor = 23.11 / 0.06 = 385.17×

**RESULT: AMBIGUOUS** ⚠️

If interpreted as multiplicative factor (385×), this is approximately correct. If interpreted as percentage increase (+385%), this is incorrect (should be +38,417%). The notation is inconsistent with the previous claim.

---

**Claim:** OOLONG: RLM(GPT-5) 56.50% vs base 44.00% (+28.4%)

**Verification:**
- Absolute improvement = 56.50 - 44.00 = 12.50 percentage points
- Relative improvement = 12.50 / 44.00 = 0.284 = 28.4%

**RESULT: CORRECT** ✓

---

**Claim:** OOLONG: RLM(Qwen3-Coder) 48.00% vs base 36.00% (+33.3%)

**Verification:**
- Absolute improvement = 48.00 - 36.00 = 12.00 percentage points
- Relative improvement = 12.00 / 36.00 = 0.333... = 33.3%

**RESULT: CORRECT** ✓

---

**Claim:** Ablation: Without sub-calls, OOLONG drops from 56.50% to 36.00%

**Verification:**
- Table 1 shows: RLM = 56.50, RLM (no sub-calls) = 36.00
- Drop = 56.50 - 36.00 = 20.50 percentage points
- Relative decrease = 20.50 / 56.50 = 36.3%

**RESULT: CORRECT** ✓

---

**Claim:** Ablation: Without sub-calls, OOLONG-Pairs drops from 58.00% to 17.34%

**Verification:**
- Table 1 shows: RLM = 58.00, RLM (no sub-calls) = 43.93
- The claim states 17.34, but Table 1 shows 43.93 (GPT-5) and 17.34 (Qwen3-Coder)

**RESULT: AMBIGUOUS** ⚠️

The paper doesn't specify which model. For GPT-5: drop is 58.00 → 43.93. For Qwen3-Coder: drop is 23.11 → 17.34. The claim appears to confuse models.

---

**Claim:** Cost: 3× cheaper than summarization baselines

**Verification:**
From Table 1:
- OOLONG: RLM(GPT-5) $0.43 vs Summary agent $0.13 (RLM is MORE expensive)
- BrowseComp+: RLM(GPT-5) $0.99 vs Summary agent $0.57 (1.74× more expensive, not 3× cheaper)

**RESULT: INCORRECT** ❌

The claim is not supported by Table 1. In most cases, RLM is comparable or slightly more expensive than summarization. Only when comparing to base model ingesting full context (theoretical $1.50-$2.75) is RLM cheaper.

---

## 2. Mathematical Formulations

### 2.1 OOLONG Scoring Function

**Stated:** "score(ŷ) = 0.75^|y-ŷ|"

**Issues:**
1. No justification for why 0.75 is chosen
2. This exponential decay seems arbitrary
3. No bounds analysis (what if |y-ŷ| is very large?)
4. Inconsistent with "exact match" scoring mentioned in same sentence

**Assessment:** The scoring function lacks theoretical justification. Why 0.75 and not 0.8 or 0.7? This appears to be borrowed from the OOLONG paper without critical evaluation.

---

### 2.2 Information Density Claims

**Claim:** "S-NIAH scales roughly constant, OOLONG scales linearly (O(N)), OOLONG-Pairs scales quadratically (O(N²))"

**Analysis:**
- These are intuitive complexity characterizations, NOT formal proofs
- No mathematical derivation of these complexities
- The paper provides narrative justification but no rigorous analysis
- The characterization is reasonable but unproven

**Assessment:** Plausible but unsubstantiated. The authors provide no formal analysis of computational complexity or information-theoretic density.

---

## 3. Theoretical Claims Assessment

### T1: Context Window Extension via Environment Variables

**Claim:** "RLMs enable LLMs to process prompts far exceeding their context windows by treating long prompts as environmental variables within a Python REPL"

**Mathematical Justification:** NONE

**Issues:**
- No formal model of how this extends capacity
- No information-theoretic analysis
- No proof that this approach preserves necessary information
- Essentially an engineering trick presented as a theoretical advance

**Assessment:** This is an implementation strategy, not a theoretical result. The paper lacks any mathematical framework for why this should work.

---

### T2-T3: Superiority of External Environment

**Claims:**
- "Placing prompts in an external REPL environment... is superior to feeding massive prompts directly"
- "Programmatic inspection... enables more effective processing"

**Mathematical Justification:** NONE

**Issues:**
- No formal comparison framework
- No proof of optimality or superiority
- Only empirical demonstrations
- Confuses empirical success with theoretical necessity

**Assessment:** These are empirical observations, not mathematical theorems. The paper provides no rigorous justification.

---

### T4-T5: Recursive Decomposition

**Claims:**
- "Recursive sub-task construction allows models to handle complexity that exceeds single-pass capabilities"
- "llm_query() function enables compositional problem decomposition"

**Mathematical Framework:** ABSENT

**Issues:**
- No formal definition of "complexity"
- No proof that recursion extends capabilities
- No analysis of recursive depth vs. problem complexity
- No compositional semantics

**Assessment:** Intuitive but mathematically ungrounded. The paper needs a formal framework for recursive computation over LLMs.

---

### T6-T8: Emergent Behaviors

**Claims:**
- "Filtering via code execution without explicit training"
- "Recursive decomposition emerges naturally"
- "Answer verification improves accuracy without explicit verification training"

**Status:** These are OBSERVATIONS, not theorems

**Issues:**
- "Emergent" is used loosely without formal definition
- No analysis of when/why these behaviors emerge
- No characterization of conditions for emergence
- Confuses empirical observation with theoretical understanding

**Assessment:** The paper documents interesting phenomena but provides no theoretical explanation for emergence.

---

### T9: Long Output Handling

**Claim:** "Constructing answers in REPL variables provides mechanism for handling outputs exceeding context length"

**Mathematical Analysis:** NONE

**Issues:**
- No formal model of output capacity
- No proof of unbounded output length
- No analysis of information loss in construction process

**Assessment:** Descriptive claim with no mathematical content.

---

### T10-T12: System Limitations

**Claims:**
- "Synchronous design creates runtime inefficiency"
- "Models not explicitly trained as RLMs can still effectively utilize the framework"
- "Recursion depth limitation to one may be limiting performance"

**Status:** Engineering observations

**Assessment:** These are design discussions, not mathematical claims. However, T12 raises an interesting question that could be mathematically analyzed but isn't.

---

## 4. Unstated Assumptions

### 4.1 Critical Unstated Assumptions

1. **Lossless Environment Interaction:** The paper assumes code execution perfectly captures relevant information. No analysis of what's lost in translation.

2. **Sub-LM Reliability:** Assumes recursive LM calls are reliable. No error propagation analysis.

3. **Prompt Decomposability:** Assumes all tasks can be meaningfully decomposed. No characterization of decomposable vs. non-decomposable tasks.

4. **Model Capabilities:** Assumes models have sufficient coding ability. No formal requirements.

5. **Cost Model:** Assumes API cost is the right metric. No analysis of total computational cost including code execution overhead.

6. **Context Independence:** Assumes chunks can be processed independently. No analysis of inter-chunk dependencies.

7. **Optimal Chunking:** Assumes model-chosen chunking is near-optimal. No analysis or bounds.

---

## 5. Logical Consistency Issues

### 5.1 Internal Contradictions

1. **Context Rot Claims:**
   - Paper claims RLMs avoid context rot
   - But RLM still uses LLM calls that suffer context rot
   - Resolution: RLMs mitigate but don't eliminate context rot
   - **Status:** Imprecise language, not true contradiction

2. **Cost Claims:**
   - Abstract claims "comparable (or cheaper) cost"
   - Table 1 shows RLMs often more expensive than base model
   - Figure 3 shows high variance with expensive tail
   - **Status:** Inconsistent framing

3. **Training Requirements:**
   - Claims models don't need RLM training
   - But acknowledges different models behave differently (Qwen3 needs special prompting)
   - Section 5 suggests training would help
   - **Status:** Tension between "training-free" and "training would help"

### 5.2 Circular Reasoning

The paper argues:
- RLMs work because they decompose problems
- Decomposition works because it avoids context rot
- Context rot is avoided because we use smaller contexts
- But smaller contexts work because models can decompose...

This is somewhat circular. A more rigorous analysis would break this cycle with formal guarantees.

---

## 6. Missing Mathematical Framework

### What's Missing:

1. **Formal Model:** No mathematical definition of RLM as a computational system

2. **Capacity Analysis:** No formal analysis of representational capacity vs. base LLM

3. **Complexity Theory:** No characterization of which problems RLMs can solve

4. **Information Theory:** No analysis of information preservation through decomposition

5. **Error Analysis:** No propagation analysis for recursive errors

6. **Optimality:** No proofs or bounds on performance

7. **Convergence:** No analysis of when iterative RLM process terminates

8. **Decomposition Theory:** No formal framework for problem decomposition

---

## 7. Statistical and Experimental Concerns

### 7.1 Sample Sizes

- S-NIAH: 50 tasks ✓
- BrowseComp-Plus: 150 tasks ✓
- OOLONG: 50 tasks ✓
- OOLONG-Pairs: 20 tasks ⚠️ (small)
- CodeQA: Not specified ❌

**Issue:** Small sample sizes, especially for OOLONG-Pairs (20 tasks), limit statistical power.

### 7.2 Statistical Significance

**MAJOR ISSUE:** No significance tests reported

- No confidence intervals
- No p-values
- No error bars
- Only means and standard deviations for costs

**Assessment:** Cannot determine if improvements are statistically significant.

### 7.3 Variance Analysis

- Table 1 reports cost variance but not performance variance
- Figure 3 shows high variance in RLM costs
- No analysis of performance variance across runs

**Issue:** High variance suggests instability but this isn't analyzed.

---

## 8. Reproducibility Concerns

### 8.1 Underspecified Elements

1. **Random Seeds:** Not mentioned
2. **Sampling Parameters:** Only "default" mentioned for GPT-5
3. **Code Execution Environment:** Python version, limits not specified
4. **Timeout Values:** Not specified
5. **Retry Logic:** Not described
6. **BM25 Parameters:** Not specified

### 8.2 Model Versioning

- "GPT-5" refers to specific model version (from system card reference)
- Qwen3-Coder-480B-A35B-Instruct is specific ✓
- But model behaviors may change over time

---

## 9. Specific Red Flags

### 🚩 Red Flag 1: Percentage Calculation Error

The +1,350% claim for OOLONG-Pairs is mathematically incorrect by 2 orders of magnitude. This suggests insufficient attention to mathematical detail.

### 🚩 Red Flag 2: Cost Claim Not Supported

"3× cheaper than summarization baselines" is not supported by the data presented. This is either wrong or refers to a specific scenario not clearly identified.

### 🚩 Red Flag 3: No Theoretical Foundation

The paper presents an engineering approach with empirical validation but lacks any theoretical framework. This is less a "scientific result" and more an "engineering demonstration."

### 🚩 Red Flag 4: Cherry-Picked Comparisons

The paper compares to "base model" but base models can't even fit many tasks. This makes improvements look dramatic but may not be fair comparison.

### 🚩 Red Flag 5: Emergent Behavior Claims

"Emergent" is used without formal definition or analysis. These are observed patterns, not understood phenomena.

### 🚩 Red Flag 6: No Failure Analysis

The paper doesn't analyze when/why RLMs fail. Example B.2 shows a failure but no systematic analysis.

---

## 10. Detailed Mathematical Issues

### Issue 1: Information Density (Section 2)

**Claim:** Tasks characterized by information density scaling (constant, linear, quadratic)

**Mathematical Issue:**
- No formal definition of "information density"
- No connection to information theory (Shannon entropy, mutual information, etc.)
- Complexity characterization is intuitive, not rigorous
- No proof that OOLONG-Pairs is truly O(N²)

**Fix Needed:** Define I(task, N) formally and prove complexity bounds.

---

### Issue 2: Effective Context Window (Section 2)

**Quote:** "the effective context window of an LLM cannot be understood independently of the specific task"

**Mathematical Issue:**
- "Effective context window" undefined
- No formal model relating task complexity to context requirements
- Could be formalized using computational complexity or information theory but isn't

**Fix Needed:** Define effective_context(model, task, performance_threshold) and analyze.

---

### Issue 3: Context Rot (Throughout)

**Usage:** Paper relies heavily on "context rot" concept

**Mathematical Issue:**
- Borrowed term from Hong et al. (2025) but not formally defined here
- No mathematical model of degradation
- No quantification of how RLMs mitigate it
- Should be modeled as error_rate(context_length, complexity)

**Fix Needed:** Formal model of context degradation and proof that RLMs reduce it.

---

### Issue 4: Observation Claims (Section 3.1)

**Example:** "RLMs exhibit interesting context management"

**Mathematical Issue:**
- Qualitative observations presented as results
- No quantification or formalization
- Pattern descriptions without theoretical explanation
- Should extract formal principles from observations

**Fix Needed:** Convert observations to testable hypotheses with metrics.

---

## 11. Strengths

### Mathematical Strengths:

1. **Clear Empirical Reporting:** Table 1 is well-structured with means and standard deviations
2. **Multiple Metrics:** Uses appropriate task-specific metrics (F1, accuracy, exact match)
3. **Cost Tracking:** Explicitly reports API costs (rare in ML papers)
4. **Scaling Analysis:** Figure 1 provides valuable scaling insights
5. **Ablation Study:** Tests contribution of sub-calls systematically
6. **Multiple Models:** Tests on both proprietary and open models
7. **Honest Failure Discussion:** Appendix B shows failure cases

---

## 12. Recommendations for Improvement

### Critical Fixes:

1. **Fix Percentage Calculations:** Correct the +1,350% claim (should be ~145×)

2. **Fix Cost Claims:** Clarify or remove "3× cheaper" claim

3. **Add Statistical Tests:** Report confidence intervals and significance tests

4. **Add Formal Framework:** Develop mathematical model of RLMs as computational systems

5. **Define Key Concepts:** Formally define: information density, effective context window, context rot mitigation

6. **Complexity Analysis:** Prove complexity bounds for different task classes

7. **Error Analysis:** Analyze error propagation in recursive calls

8. **Failure Analysis:** Systematically characterize when RLMs fail

### Enhancements:

9. **Information Theory:** Apply Shannon entropy to quantify information density

10. **Optimization Theory:** Analyze optimal chunking and decomposition strategies

11. **Probabilistic Analysis:** Model RLM as probabilistic graphical model

12. **Sample Size:** Increase tasks for OOLONG-Pairs (current: 20)

13. **Reproducibility:** Specify all hyperparameters, seeds, environment details

---

## 13. Comparison to Related Work

The paper cites relevant work but lacks mathematical comparison:

- **vs. MemWalker:** No formal comparison of tree navigation vs. REPL environment
- **vs. ReSum:** No theoretical analysis of why code > summarization
- **vs. Context Folding:** No formal model differentiating approaches

**Issue:** Comparisons are empirical only, no theoretical positioning.

---

## 14. Alternative Explanations

The paper attributes improvements to RLM framework but doesn't rule out alternatives:

1. **More Compute:** RLMs use more LLM calls—is that the only reason for improvement?
2. **Better Prompting:** The RLM prompt is elaborate—is that sufficient?
3. **Test-Time Scaling:** Is this just inference-time compute scaling?
4. **Ensemble Effect:** Multiple LM calls could be viewed as ensemble

**Issue:** No ablation isolating the specific contribution of the REPL environment vs. just more compute.

---

## 15. Generalization Claims

**Claim:** RLMs are "general-purpose inference paradigm"

**Mathematical Support:** NONE

**Issues:**
- Tested on 5 task types only
- All tasks involve document/code processing
- No results on other modalities (vision, audio)
- No characterization of task classes where RLMs work
- "General-purpose" is overstated

**Assessment:** Promising approach for document-heavy tasks, but "general-purpose" is unsubstantiated.

---

## 16. Correctness of Table 1

I'll verify consistency of Table 1 values:

**Checked:**
- All methods run on all tasks ✓
- Costs have standard deviations ✓
- "No sub-calls" scores are generally lower ✓
- * markers for context limit issues are consistent ✓

**Issue Found:**
BrowseComp+ base model shows 0.00 with "N/A ± N/A" cost—this is correct (can't fit in context) but the * explanation could be clearer.

---

## 17. Figure 1 Analysis

**Scaling Plots:**

**Mathematical Observations:**
- Log-scale x-axis (powers of 2 from 2^13 to 2^18)
- S-NIAH: GPT-5 ~flat at ~90%, RLM ~flat at ~90% (both good)
- OOLONG: GPT-5 degrades ~80→40%, RLM ~80→50% (both degrade but RLM less)
- OOLONG-Pairs: GPT-5 degrades ~90→5%, RLM degrades ~60→50% (dramatic difference)

**Issues:**
- No error bars (statistical uncertainty unknown)
- Red region indicates >272K token limit but no tasks go there in plot
- Claims "RLM maintains strong performance" but OOLONG still shows degradation
- Y-axis is "Score (%)" but different metrics used (accuracy vs F1)

**Assessment:** Informative visualization but needs error bars and metric clarification.

---

## 18. Cost Analysis (Figure 3)

**Observations:**
- Median RLM cost < median base model cost (good)
- 95th percentile RLM cost >> 95th percentile base model cost (high variance)
- Summary agent has intermediate variance

**Mathematical Issue:**
- Mean would be more relevant than quartiles for cost comparison
- High variance suggests unreliable cost prediction
- No analysis of cost-performance tradeoff (Pareto frontier)

---

## Final Mathematical Rigor Assessment

### Quantitative Breakdown:

- **Empirical Correctness:** 7/10 (mostly correct with notable errors)
- **Mathematical Rigor:** 3/10 (almost no formal mathematics)
- **Theoretical Justification:** 2/10 (minimal theory)
- **Statistical Validity:** 5/10 (missing significance tests)
- **Logical Consistency:** 7/10 (mostly consistent with minor issues)
- **Reproducibility:** 6/10 (some details missing)

### Overall Score: 6.5/10

**Rationale:**
- Strong empirical work (+3)
- Clear presentation (+1.5)
- Honest limitations discussion (+1)
- Multiple models and tasks (+1)
- **Missing theoretical foundation (-2)**
- **Mathematical errors in claims (-1)**
- **No statistical significance tests (-1)**
- **Overstated generality (-0.5)**

---

## Conclusion

This paper presents a **practically useful engineering approach** with **solid empirical validation** but **weak theoretical foundations**. It reads more like a systems paper than a machine learning theory paper.

### Key Mathematical Deficiencies:

1. No formal computational model
2. Incorrect percentage calculations in key claims
3. No statistical significance testing
4. Intuitive complexity characterizations without proofs
5. "Emergent" phenomena observed but not explained
6. No information-theoretic or complexity-theoretic analysis

### Verdict: QUESTIONABLE

The paper makes valuable empirical contributions but lacks the mathematical rigor expected for theoretical claims. The approach works in practice but we don't understand why in a formal sense. Several numerical claims are incorrect or unsupported.

### Recommendation:

**For Publication:** Yes, with major revisions to:
1. Fix mathematical errors
2. Add formal framework
3. Add statistical tests
4. Tone down generality claims
5. Clearly position as engineering contribution, not theoretical advance

**As-is Mathematical Rigor:** Insufficient for a theory venue, acceptable for systems/empirical venue.

---

## Appendix: Detailed Calculation Verification

### A.1 OOLONG-Pairs GPT-5 Improvement

```
Base: 0.04
RLM: 58.00
Absolute improvement: 58.00 - 0.04 = 57.96
Relative improvement: 57.96 / 0.04 = 1449
Percentage increase: 1449 × 100% = 144,900%
Multiplicative factor: 58.00 / 0.04 = 1450×

Paper claims: +1,350%
Error: ~100× too small
```

### A.2 Cost Comparison (BrowseComp+)

```
RLM(GPT-5): $0.99 ± $1.22
Summary agent(GPT-5): $0.57 ± $0.10
Ratio: 0.99 / 0.57 = 1.74 (RLM is 74% MORE expensive)

Paper claims: "3× cheaper"
Status: Incorrect for this comparison
```

Possible interpretation: Comparing to theoretical base model cost ($1.50-$2.75):
```
RLM: $0.99
Theoretical base: ~$2.00
Ratio: 2.00 / 0.99 = 2.02× cheaper (not 3×)
```

Still doesn't match claim exactly.

---

**End of Mathematical Audit Report**
