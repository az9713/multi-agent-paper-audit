# Quick Start Guide

Get up and running with the Multi-Agent Paper Audit tool in 5 minutes. This guide includes 10 hands-on examples to help you learn the tool quickly.

## Before You Begin

### What You Need

1. **A computer** - Windows, Mac, or Linux
2. **Internet connection** - To fetch papers from arXiv
3. **Claude Code CLI** - The AI command line tool

### Check If Claude Code Is Installed

Open your terminal (Command Prompt on Windows, Terminal on Mac/Linux) and type:

```bash
claude --version
```

If you see a version number, you're ready! If not, see the [Installation Guide](INSTALLATION.md).

---

## Your First Audit (2 minutes)

Let's audit a real paper together.

### Step 1: Open Claude Code

```bash
cd multi-agent-paper-audit
claude
```

You should see a prompt like:
```
claude>
```

### Step 2: Run Your First Audit

Type this command:

```
/audit-paper 2512.24601
```

### Step 3: Wait for Results

You'll see progress updates:
```
[/audit-paper] Starting audit of 2512.24601...

[Phase 1] Fetching paper...
  ✓ Paper downloaded: "Recursive Language Models"

[Phase 2] Agent A: Deconstructing paper...
  ✓ Found 12 theoretical claims
  ✓ Found 29 empirical claims

[Phase 3] Running parallel agents...
  ✓ Agent B complete: QUESTIONABLE
  ✓ Agent C complete: 20 questions generated
  ✓ Agent D complete: 9/11 claims verified

[Phase 4] Agent E: Synthesizing reports...
  ✓ Decision memo generated

[Phase 5] Creating README index...
  ✓ README.md generated

[Phase 6] Audit complete!
  📂 Start here: output/2512.24601/README.md
```

### Step 4: View Your Results

Open the output folder:
- **Windows:** `explorer output\2512.24601`
- **Mac:** `open output/2512.24601`
- **Linux:** `xdg-open output/2512.24601`

Start with `README.md` - it tells you which file to read first!

---

## 10 Example Use Cases

These examples will help you understand what the tool can do. Try them in order for the best learning experience.

---

### Use Case 1: Quick Paper Summary

**Goal:** Get a quick understanding of what a paper claims.

**How:**
```
/audit-paper 2512.24601
```

**What to look at:** Open `deconstruction.json` - it lists every claim the paper makes, organized by type:
- `theoretical_claims` - How/why things work
- `empirical_claims` - Numerical results
- `comparative_claims` - Comparisons to other methods
- `novelty_claims` - What's new

**What you'll learn:** The paper claims to improve performance by 1,350% using recursive language models.

---

### Use Case 2: Find Mathematical Errors

**Goal:** Check if the paper's math is correct.

**How:**
```
/audit-paper 2512.24601
```

**What to look at:** Open `math_audit.md` and look for:
- ❌ INCORRECT markers
- ⚠️ AMBIGUOUS markers
- 🚩 Red Flag sections

**What you'll learn:** The "+1,350%" claim is actually incorrect - the real improvement is 1,450× (144,900%), a notation confusion.

---

### Use Case 3: Generate Tough Review Questions

**Goal:** Prepare for a paper discussion or write a peer review.

**How:**
```
/audit-paper 2512.24601
```

**What to look at:** Open `adversarial_review.md` - it contains 15-20 tough questions organized by:
- **CRITICAL** - Would invalidate the paper if true
- **MAJOR** - Significantly weakens claims
- **MINOR** - Issues but not deal-breakers

**What you'll learn:** The paper has 3 CRITICAL issues including suspicious baseline numbers.

---

### Use Case 4: Check for Prior Art

**Goal:** Find if similar work already exists.

**How:**
```
/audit-paper 2512.24601
```

**What to look at:** Open `contradicting_papers.md` - it lists:
- Papers that do similar things
- Papers with conflicting findings
- Missing citations

**What you'll learn:** MemGPT (2023) uses a similar approach but isn't adequately compared.

---

### Use Case 5: Verify Numerical Claims

**Goal:** Check if the numbers in the paper are correct.

**How:**
```
/audit-paper 2512.24601
```

**What to look at:** Open `verification/results.json` - it shows:
- Which claims were verified ✓
- Which claims failed verification ✗
- Actual vs claimed values

**What you'll learn:** 9 out of 11 numerical claims are verified; 2 have notation issues.

---

### Use Case 6: Get Research Ideas

**Goal:** Find directions for your own research based on the paper's gaps.

**How:**
```
/audit-paper 2512.24601
```

**What to look at:** Open `FULL_RESEARCH_PROPOSAL.md` - it contains:
- 8 detailed research directions
- Methodology for each
- Resource estimates
- Risk assessments

**What you'll learn:** Testing depth-2+ recursion is a promising research direction worth exploring.

---

### Use Case 7: Understand Literature Gaps

**Goal:** Find what's missing in the research area.

**How:**
```
/audit-paper 2512.24601
```

**What to look at:** Open `literature_gaps.md` - it lists:
- Theoretical gaps (missing proofs)
- Empirical gaps (missing experiments)
- Methodological gaps (missing rigor)

**What you'll learn:** 24 gaps identified, including lack of formal computational model.

---

### Use Case 8: Get a Publication Recommendation

**Goal:** Understand if a paper is ready for publication.

**How:**
```
/audit-paper 2512.24601
```

**What to look at:** Open `decision_memo.md` and check:
- **VERDICT** section for the decision
- **Score Breakdown** for agent scores
- **Recommendations for Authors** for what to fix

**What you'll learn:** The paper needs MAJOR REVISION (score 6.01/10) before it's ready for top venues.

---

### Use Case 9: Explore Claims Interactively

**Goal:** Play with the data yourself.

**How:**
```
/audit-paper 2512.24601
```

**What to look at:** Open `exploration_notebook.ipynb` in Jupyter:
```bash
jupyter notebook output/2512.24601/exploration_notebook.ipynb
```

**What you'll learn:** How to run verification code and create your own analyses.

---

### Use Case 10: Compare Multiple Papers

**Goal:** Audit several papers in the same area.

**How:**
```
/audit-paper 2512.24601
/audit-paper 2310.08560
/audit-paper 2307.03172
```

**What to look at:** Compare the `decision_memo.md` files from each:
- Which has the highest score?
- What are common issues?
- Which claims overlap?

**What you'll learn:** How to systematically compare papers in a research area.

---

## Tips for Success

### Tip 1: Always Start with README.md
Every audit creates a README in the output folder. It tells you exactly which file to read first based on your goal.

### Tip 2: Focus on CRITICAL Issues First
In the adversarial review, CRITICAL issues are what matter most. Start there.

### Tip 3: Check the Score Breakdown
The final score comes from three agents:
- Agent B (Math): 30%
- Agent C (Skeptic): 40%
- Agent D (Verifier): 30%

A low Agent C score means the paper has defensibility problems.

### Tip 4: Use the Verification Code
The `verification/main.py` script is ready to run:
```bash
cd output/2512.24601/verification
python main.py
```

### Tip 5: Read the Research Proposal
Even if you're not doing research, the `FULL_RESEARCH_PROPOSAL.md` helps you understand the paper's limitations.

---

## Common Questions

### Q: How long does an audit take?
**A:** Usually 3-5 minutes depending on paper length and complexity.

### Q: Can I audit papers not on arXiv?
**A:** Currently only arXiv papers are supported. PDF support is planned.

### Q: What if the audit fails?
**A:** Check the [Troubleshooting Guide](TROUBLESHOOTING.md) for common issues.

### Q: Can I customize the agents?
**A:** Yes! See the [Developer Guide](DEVELOPER_GUIDE.md) for how to modify agents.

---

## Next Steps

Now that you've completed the quick start:

1. **Read the full [User Guide](USER_GUIDE.md)** for all features
2. **Try auditing papers in your field**
3. **Check the [Developer Guide](DEVELOPER_GUIDE.md)** if you want to customize

Happy auditing!
