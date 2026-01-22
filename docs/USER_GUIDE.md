# User Guide

This comprehensive guide covers everything you need to know to use the Multi-Agent Paper Audit tool effectively.

---

## Table of Contents

1. [Overview](#overview)
2. [Starting the Tool](#starting-the-tool)
3. [Auditing a Paper](#auditing-a-paper)
4. [Understanding the Output](#understanding-the-output)
5. [Reading Each Report](#reading-each-report)
6. [Interpreting Scores](#interpreting-scores)
7. [Using the Verification Code](#using-the-verification-code)
8. [Advanced Usage](#advanced-usage)
9. [Best Practices](#best-practices)
10. [Glossary](#glossary)

---

## Overview

### What This Tool Does

The Multi-Agent Paper Audit tool uses five AI agents to analyze scientific papers:

| Agent | Name | Job | Weight in Score |
|-------|------|-----|-----------------|
| A | Deconstructor | Extract all claims from the paper | N/A (extraction only) |
| B | Formalist | Check mathematical rigor | 30% |
| C | Skeptic | Generate adversarial questions | 40% |
| D | Verifier | Run code to verify claims | 30% |
| E | Editor | Synthesize everything into a verdict | N/A (synthesis only) |

### Who Should Use This Tool

- **Researchers** - Evaluate papers before citing them
- **Reviewers** - Prepare thorough peer reviews
- **Students** - Learn to critically read papers
- **Journal Editors** - Identify problematic submissions
- **Anyone** - Who wants to understand a paper better

---

## Starting the Tool

### Step 1: Open Your Terminal

**Windows:**
- Press `Windows + R`
- Type `cmd` or `powershell` and press Enter

**Mac:**
- Press `Cmd + Space`
- Type `Terminal` and press Enter

**Linux:**
- Press `Ctrl + Alt + T`

### Step 2: Navigate to the Project Folder

```bash
cd path/to/multi-agent-paper-audit
```

For example:
```bash
cd Documents/multi-agent-paper-audit
```

### Step 3: Start Claude Code

```bash
claude
```

You'll see a prompt:
```
claude>
```

Now you're ready to audit papers!

---

## Auditing a Paper

### Basic Command

```
Audit this paper: <paper-identifier>
```

### Ways to Specify a Paper

| Format | Example |
|--------|---------|
| Full PDF URL | `Audit this paper: https://arxiv.org/pdf/2512.24601.pdf` |
| Abstract URL | `Audit this paper: https://arxiv.org/abs/2512.24601` |
| arXiv ID with prefix | `Audit this paper: arXiv:2512.24601` |
| Just the ID | `Audit this paper: 2512.24601` |

### What Happens During an Audit

When you run an audit, you'll see progress updates:

```
[Audit this paper:] Starting audit of 2512.24601...

[Phase 1] Fetching paper...
  ✓ Paper downloaded: "Recursive Language Models"
  ✓ Output directory: output/2512.24601/

[Phase 2] Agent A: Deconstructing paper...
  ✓ Found 12 theoretical claims
  ✓ Found 29 empirical claims
  ✓ Found 12 comparative claims
  ✓ Found 7 novelty claims
  ✓ Saved: deconstruction.json

[Phase 3] Running parallel agents...
  [Agent B] Auditing mathematical rigor...
  [Agent C] Launching adversarial review...
  [Agent C] Searching for contradicting papers...
  [Agent D] Generating verification code...
  [Agent D] Executing verification...

  ✓ Agent B complete: QUESTIONABLE
  ✓ Agent C complete: QUESTIONABLE, 20 questions generated
  ✓ Agent D complete: 9/11 claims verified

[Phase 4] Agent E: Synthesizing reports...
  ✓ Decision memo generated
  ✓ Research proposal generated
  ✓ Exploration notebook generated

[Phase 5] Creating README index...
  ✓ README.md generated with reading guide

[Phase 6] Audit complete!
  📂 Start here: output/2512.24601/README.md
```

### Typical Duration

| Paper Length | Approximate Time |
|--------------|------------------|
| Short (< 10 pages) | 2-3 minutes |
| Medium (10-20 pages) | 3-5 minutes |
| Long (> 20 pages) | 5-8 minutes |

---

## Understanding the Output

After an audit completes, you'll find all results in the `output/{paper_id}/` folder.

### Folder Structure

```
output/2512.24601/
│
├── README.md                  ← START HERE!
│
├── Core Reports
│   ├── decision_memo.md       ← Final verdict
│   ├── adversarial_review.md  ← Critical questions
│   ├── math_audit.md          ← Math check
│   └── contradicting_papers.md← Prior art
│
├── Research Outputs
│   ├── FULL_RESEARCH_PROPOSAL.md ← Future directions
│   ├── literature_gaps.md     ← What's missing
│   └── exploration_notebook.ipynb ← Interactive
│
├── Data Files
│   └── deconstruction.json    ← All claims
│
└── verification/              ← Code verification
    ├── main.py                ← Scripts
    ├── results.json           ← Results
    ├── execution_log.txt      ← Log
    └── plots/                 ← Visualizations
        ├── improvement_magnitudes.png
        ├── complexity_comparison.png
        └── ...
```

### How to Navigate the Output

**Always start with `README.md`!** It tells you:
- What files to read based on your goal
- The final score and verdict
- Where to find specific information

---

## Reading Each Report

### README.md (Start Here)

**Purpose:** Index and guide to all other files.

**What it contains:**
- Quick Start table showing priority order
- Score summary
- List of all files with descriptions
- Reading order based on your goal

**When to read it:** Always, before anything else.

---

### decision_memo.md

**Purpose:** The final verdict and recommendations.

**What it contains:**
- Executive summary
- Score breakdown (Agent B, C, D)
- Final decision (Accept/Revise/Reject)
- Critical issues that must be fixed
- Recommendations for authors
- Publication venue guidance

**Key sections to look at:**

1. **VERDICT** - The bottom line
   ```
   ### Final Decision: MAJOR REVISION REQUIRED
   ```

2. **Score Breakdown** - How each agent scored
   ```
   | Agent | Raw Score | Weight | Weighted Score |
   |-------|-----------|--------|----------------|
   | Agent B (Math) | 6.5/10 | 30% | 1.95 |
   | Agent C (Skeptic) | 4.0/10 | 40% | 1.60 |
   | Agent D (Verifier) | 8.2/10 | 30% | 2.46 |
   | **TOTAL** | | | **6.01/10** |
   ```

3. **Critical Issues** - What must be fixed
   ```
   1. CRITICAL: Baseline Discrepancy
      - Impact: Undermines all performance comparisons
      - Required Action: Explain the 100× discrepancy
   ```

**When to read it:** When you need the final judgment on a paper.

---

### adversarial_review.md

**Purpose:** Critical questions a skeptical reviewer would ask.

**What it contains:**
- 15-20 adversarial questions
- Severity ratings (CRITICAL/MAJOR/MINOR)
- Rebuttal difficulty scores
- Attack vector analysis

**Key sections:**

1. **Questions by Severity**
   ```
   #### Q1: Why is GPT-5 baseline showing 0.04 F1?
   **Severity:** CRITICAL
   **Rebuttal Difficulty:** 9/10
   ```

2. **Severity Summary**
   ```
   | Severity | Count | Questions |
   |----------|-------|-----------|
   | CRITICAL | 3 | Q1, Q5, Q10 |
   | MAJOR | 14 | Q2-Q4, Q6-Q9... |
   | MINOR | 3 | Q12, Q16, Q20 |
   ```

3. **Final Verdicts**
   ```
   VERDICT: QUESTIONABLE
   Rebuttal Difficulty Score: 7/10
   Overall Skeptic Score: 4/10
   ```

**When to read it:** When preparing a peer review or evaluating paper rigor.

---

### math_audit.md

**Purpose:** Check mathematical correctness.

**What it contains:**
- Verification of percentage calculations
- Analysis of mathematical formulations
- Theoretical claims assessment
- Red flags and concerns

**Key sections:**

1. **Calculation Verification**
   ```
   **Claim:** +1,350% improvement
   **Verification:**
   - Actual: 144,900% or 1,449×
   **RESULT: INCORRECT** ❌
   ```

2. **Theoretical Claims**
   ```
   ### T1: Context Window Extension
   **Mathematical Justification:** NONE
   **Assessment:** Engineering trick, not theoretical result
   ```

3. **Red Flags**
   ```
   🚩 Red Flag 1: Percentage Calculation Error
   🚩 Red Flag 2: Cost Claim Not Supported
   ```

**When to read it:** When you care about mathematical rigor.

---

### contradicting_papers.md

**Purpose:** Related work that challenges the paper's claims.

**What it contains:**
- Papers with similar approaches
- Papers with conflicting findings
- Missing comparisons

**When to read it:** When checking novelty or looking for related work.

---

### deconstruction.json

**Purpose:** Structured list of every claim in the paper.

**Format:**
```json
{
  "theoretical_claims": [
    {
      "id": "T1",
      "text": "RLMs enable LLMs to process prompts...",
      "verifiable": true,
      "confidence": "high"
    }
  ],
  "empirical_claims": [...],
  "comparative_claims": [...],
  "novelty_claims": [...]
}
```

**When to read it:** When you need a complete inventory of claims.

---

### FULL_RESEARCH_PROPOSAL.md

**Purpose:** Future research directions based on gaps found.

**What it contains:**
- 5-8 detailed research directions
- Methodology for each
- Resource estimates
- Risk assessments

**When to read it:** When looking for research opportunities.

---

### literature_gaps.md

**Purpose:** What's missing in the research area.

**What it contains:**
- Theoretical gaps
- Empirical gaps
- Methodological gaps
- Open research questions

**When to read it:** When doing a literature review.

---

### verification/ folder

**Purpose:** Code that verifies numerical claims.

**Files:**
- `main.py` - All verification scripts
- `results.json` - Structured results
- `execution_log.txt` - What happened when code ran
- `plots/` - Generated visualizations

**When to use it:** When you want to verify claims yourself.

---

## Interpreting Scores

### Overall Score Scale

| Score | Verdict | What It Means |
|-------|---------|---------------|
| 8.0 - 10.0 | ACCEPT | Strong paper, ready for publication |
| 6.0 - 7.9 | ACCEPT WITH RESERVATIONS | Good but has concerns |
| 4.0 - 5.9 | MAJOR REVISION | Substantial issues |
| 2.0 - 3.9 | REJECT (Revise & Resubmit) | Fundamental problems |
| 0.0 - 1.9 | REJECT | Fatally flawed |

### Agent B (Math) Score

| Score | Meaning |
|-------|---------|
| 9-10 | Mathematically rigorous, no errors |
| 7-8 | Sound with minor issues |
| 5-6 | Some errors or missing rigor |
| 3-4 | Significant mathematical problems |
| 1-2 | Major errors that invalidate claims |

### Agent C (Skeptic) Score

| Score | Verdict | Meaning |
|-------|---------|---------|
| 9-10 | ROBUST | Paper survives scrutiny |
| 7-8 | DEFENSIBLE | Good but some weak points |
| 4-6 | QUESTIONABLE | Significant concerns |
| 1-3 | SUSPICIOUS | Major red flags |

### Agent D (Verifier) Score

Based on percentage of claims verified:
- 90%+ verified = 9-10
- 70-89% verified = 7-8
- 50-69% verified = 5-6
- Below 50% verified = 1-4

---

## Using the Verification Code

### Running the Verification Scripts

1. **Navigate to the verification folder:**
   ```bash
   cd output/2512.24601/verification
   ```

2. **Install dependencies (if needed):**
   ```bash
   pip install numpy matplotlib pandas
   ```

3. **Run the main script:**
   ```bash
   python main.py
   ```

4. **Check the results:**
   - `results.json` - Structured output
   - `plots/` - Generated visualizations

### Understanding results.json

```json
{
  "verification_status": "9/11 claims verified",
  "score": 8.2,
  "verified_claims": ["E6_C4", "E7_C5", ...],
  "unverified_claims": ["E2_C2", "E3_C3"],
  "mathematical_errors_found": [
    {
      "claim": "E2_C2",
      "claimed": 1350.0,
      "actual": 144900.0
    }
  ]
}
```

### Modifying the Code

The verification code is designed to be modified:

1. Open `main.py` in any text editor
2. Find the section for the claim you want to investigate
3. Modify parameters or add your own tests
4. Run again with `python main.py`

---

## Advanced Usage

### Auditing Multiple Papers

You can audit several papers in one session:

```
Audit this paper: 2512.24601
Audit this paper: 2310.08560
Audit this paper: 2307.03172
```

Each creates its own folder in `output/`.

### Comparing Papers

After auditing multiple papers:

1. Open each `decision_memo.md`
2. Compare scores
3. Look at common issues
4. Check which claims are verified in each

### Using the Exploration Notebook

The Jupyter notebook allows interactive exploration:

1. **Start Jupyter:**
   ```bash
   jupyter notebook output/2512.24601/exploration_notebook.ipynb
   ```

2. **Run cells in order** (Shift + Enter)

3. **Modify and experiment** with the code

---

## Best Practices

### For Paper Evaluation

1. **Read the decision memo first** - Get the bottom line
2. **Check CRITICAL issues** - These are deal-breakers
3. **Look at verification results** - What was actually verified?
4. **Review the math audit** - Are calculations correct?

### For Peer Review

1. **Use adversarial questions** as a starting point
2. **Focus on high-severity items** (CRITICAL > MAJOR > MINOR)
3. **Check prior art** in contradicting_papers.md
4. **Verify claims yourself** using the code

### For Research

1. **Check literature gaps** for opportunities
2. **Read the research proposal** for detailed directions
3. **Use the exploration notebook** to experiment
4. **Build on verified claims** - they're more reliable

---

## Glossary

| Term | Definition |
|------|------------|
| **arXiv** | A free repository of scientific papers (arxiv.org) |
| **Adversarial Review** | Critical analysis that tries to find problems |
| **Claim** | A statement the paper makes that could be true or false |
| **Deconstruction** | Breaking a paper into individual claims |
| **Empirical Claim** | A claim backed by experimental data |
| **F1 Score** | A measure of accuracy (0-100%) |
| **Novelty Claim** | A claim about what's new or first |
| **Rebuttal** | A response to criticism |
| **Theoretical Claim** | A claim about how/why something works |
| **Verification** | Checking if a claim is actually true |
| **Weighted Score** | A score that counts some things more than others |

---

## Getting Help

### Documentation

- [Quick Start Guide](QUICK_START.md) - Fast intro with examples
- [Installation Guide](INSTALLATION.md) - Setup instructions
- [Developer Guide](DEVELOPER_GUIDE.md) - For customization
- [Troubleshooting](TROUBLESHOOTING.md) - Common problems

### Community

- [GitHub Issues](https://github.com/az9713/multi-agent-paper-audit/issues) - Report bugs
- [GitHub Discussions](https://github.com/az9713/multi-agent-paper-audit/discussions) - Ask questions
