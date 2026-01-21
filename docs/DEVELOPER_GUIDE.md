# Developer Guide

This guide is for developers who want to understand, modify, or extend the Multi-Agent Paper Audit tool. We assume you may be new to this type of project, so we explain everything step by step.

---

## Table of Contents

1. [Understanding the Codebase](#understanding-the-codebase)
2. [How Skills Work](#how-skills-work)
3. [The Agent System](#the-agent-system)
4. [Modifying Agents](#modifying-agents)
5. [Adding New Features](#adding-new-features)
6. [Testing Your Changes](#testing-your-changes)
7. [Code Style Guide](#code-style-guide)
8. [Contributing](#contributing)

---

## Understanding the Codebase

### What Is This Project?

This project is a **skill** for Claude Code. A skill is like a plugin that teaches Claude Code how to do something specific - in this case, how to audit scientific papers.

### Key Concept: Skills vs Traditional Code

| Traditional Code | Skills |
|-----------------|--------|
| Written in Python, JavaScript, etc. | Written in Markdown |
| Computer executes the code | AI reads and follows instructions |
| Fixed logic | Flexible, AI adapts to context |
| Needs compilation/running | Just edit the markdown file |

### Project Structure

```
multi-agent-paper-audit/
│
├── .claude/                      # Claude Code configuration
│   ├── skills/                   # Skill definitions
│   │   └── paper-audit/          # Our audit skill
│   │       ├── SKILL.md          # Main orchestrator
│   │       ├── agent-a-deconstructor.md
│   │       ├── agent-b-formalist.md
│   │       ├── agent-c-skeptic.md
│   │       ├── agent-d-verifier.md
│   │       └── agent-e-editor.md
│   │
│   └── prompts/                  # Templates and helpers
│       └── paper-audit/
│           └── verification-templates/
│
├── output/                       # Generated outputs (per paper)
│   └── {paper_id}/               # One folder per audited paper
│
├── docs/                         # Documentation
│
├── README.md                     # Project overview
├── CLAUDE.md                     # Instructions for Claude Code
└── LICENSE                       # MIT License
```

### What Each File Does

| File | Purpose |
|------|---------|
| `SKILL.md` | **The main orchestrator** - controls the entire audit flow |
| `agent-a-deconstructor.md` | Instructions for extracting claims |
| `agent-b-formalist.md` | Instructions for math auditing |
| `agent-c-skeptic.md` | Instructions for adversarial review |
| `agent-d-verifier.md` | Instructions for code verification |
| `agent-e-editor.md` | Instructions for synthesis |
| `CLAUDE.md` | Tells Claude Code how to work with this project |

---

## How Skills Work

### Anatomy of a Skill File

Every skill file has two parts:

1. **Front Matter** - Metadata in YAML format
2. **Content** - Instructions in Markdown

Example:
```markdown
---
name: paper-audit
description: Audit scientific papers from arXiv
---

# Paper Audit Skill

Instructions go here...
```

### How Claude Code Finds Skills

When you type `/audit-paper`, Claude Code:

1. Looks in `.claude/skills/` for matching skill
2. Finds `paper-audit/SKILL.md` (main entry point)
3. Reads the instructions
4. Follows them step by step

### How Skills Call Other Skills

The main skill (`SKILL.md`) can invoke sub-skills:

```markdown
Invoke skill: paper-audit:agent-a-deconstructor
```

This tells Claude to read and follow `agent-a-deconstructor.md`.

---

## The Agent System

### Overview

The audit uses 5 agents working together:

```
User Request
     │
     ▼
┌─────────────────────┐
│    SKILL.md         │  ← Orchestrator (you call this)
│    (Orchestrator)   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Agent A          │  ← Runs first
│  (Deconstructor)    │
└──────────┬──────────┘
           │
     ┌─────┼─────┐
     ▼     ▼     ▼
┌───────┐┌───────┐┌───────┐
│Agent B││Agent C││Agent D│  ← Run in parallel
│ (Math)││(Skept)││(Verif)│
└───┬───┘└───┬───┘└───┬───┘
    │        │        │
    └────────┼────────┘
             ▼
┌─────────────────────┐
│    Agent E          │  ← Runs last
│  (Editor-in-Chief)  │
└─────────────────────┘
```

### What Each Agent Does

#### Agent A: Deconstructor

**Input:** Paper content (from arXiv)
**Output:** `deconstruction.json`

Extracts claims in four categories:
- Theoretical claims (how/why things work)
- Empirical claims (numbers and measurements)
- Comparative claims (vs other methods)
- Novelty claims (what's new)

#### Agent B: Formalist

**Input:** `deconstruction.json` (theoretical claims)
**Output:** `math_audit.md`
**Weight:** 30% of final score

Checks:
- Mathematical correctness
- Calculation verification
- Logical consistency
- Statistical rigor

#### Agent C: Skeptic

**Input:** Full paper content
**Output:** `adversarial_review.md`, `contradicting_papers.md`
**Weight:** 40% of final score

Does:
- Generates adversarial questions
- Searches for contradicting papers
- Identifies weak points
- Assesses defensibility

#### Agent D: Verifier

**Input:** `deconstruction.json` (empirical claims)
**Output:** `verification/` folder
**Weight:** 30% of final score

Does:
- Writes verification code
- Runs the code
- Checks numerical claims
- Creates visualizations

#### Agent E: Editor-in-Chief

**Input:** All outputs from A, B, C, D
**Output:** `decision_memo.md`, `README.md`, research outputs

Does:
- Calculates final score
- Determines verdict
- Writes decision memo
- Creates research proposal
- Generates README for users

---

## Modifying Agents

### Before You Modify

1. **Understand the current behavior** - Run an audit first
2. **Read the agent file** - Understand what it does
3. **Make a backup** - Copy the file before editing

### How to Modify an Agent

Let's say you want to change how Agent C generates questions.

#### Step 1: Open the File

```bash
code .claude/skills/paper-audit/agent-c-skeptic.md
```

Or use any text editor (Notepad, VS Code, etc.)

#### Step 2: Find the Section to Modify

The file is organized with headers:

```markdown
## Adversarial Questions

Generate 15+ questions covering these attack vectors:

1. Experimental methodology flaws
2. Statistical significance concerns
...
```

#### Step 3: Make Your Change

For example, to add a new attack vector:

```markdown
## Adversarial Questions

Generate 15+ questions covering these attack vectors:

1. Experimental methodology flaws
2. Statistical significance concerns
3. **Reproducibility concerns**    ← NEW
...
```

#### Step 4: Save and Test

Save the file and run an audit to test:

```bash
claude
> /audit-paper 2512.24601
```

### Example Modifications

#### Example 1: Change the Scoring Weights

In `agent-e-editor.md`, find the weighting section:

```markdown
| Agent | Weight |
|-------|--------|
| Agent B (Math) | 30% |
| Agent C (Skeptic) | 40% |
| Agent D (Verifier) | 30% |
```

Change to whatever you want (must sum to 100%):

```markdown
| Agent | Weight |
|-------|--------|
| Agent B (Math) | 40% |
| Agent C (Skeptic) | 30% |
| Agent D (Verifier) | 30% |
```

#### Example 2: Add More Adversarial Questions

In `agent-c-skeptic.md`, find:

```markdown
Generate 15+ adversarial questions
```

Change to:

```markdown
Generate 25+ adversarial questions
```

#### Example 3: Change the Verdict Thresholds

In `agent-e-editor.md`, find:

```markdown
| 8.0 - 10.0 | ACCEPT |
| 6.0 - 7.9 | ACCEPT WITH RESERVATIONS |
```

Adjust the thresholds as needed.

---

## Adding New Features

### Adding a New Agent

To add Agent F (example: citation checker):

#### Step 1: Create the Agent File

Create `.claude/skills/paper-audit/agent-f-citation-checker.md`:

```markdown
---
name: paper-audit:agent-f-citation-checker
description: Checks citation quality and coverage
---

# Agent F: Citation Checker

## Your Mission

Check the paper's citations for:
1. Missing important citations
2. Outdated references
3. Self-citation ratio
4. Citation context quality

## Inputs

- Paper content
- `deconstruction.json`

## Output

Create `citation_audit.md` with:
- Citation statistics
- Missing citations
- Quality assessment

## Process

1. Count total citations
2. Identify citation categories
3. Search for missing important works
4. Calculate self-citation ratio
5. Assess citation context
```

#### Step 2: Update the Orchestrator

In `SKILL.md`, add your agent to Phase 3:

```markdown
### Phase 3: Parallel Agent Execution (B, C, D, F)

#### Agent F: Citation Checker
```
Invoke skill: paper-audit:agent-f-citation-checker
Output: output/{paper_id}/citation_audit.md
```
```

#### Step 3: Update Agent E

In `agent-e-editor.md`, add the new input:

```markdown
## Inputs

- `output/{paper_id}/citation_audit.md` - Agent F's citation analysis
```

#### Step 4: Test

Run an audit and verify Agent F runs correctly.

### Adding New Output Files

To add a new output file:

1. **Decide which agent creates it**
2. **Add instructions to that agent's file**
3. **Update the README template in SKILL.md**
4. **Update the checklist in SKILL.md**

### Adding New Input Formats

Currently only arXiv is supported. To add PDF support:

1. **Modify SKILL.md** to detect PDF files:
   ```markdown
   **Local PDF:**
   - `./path/to/paper.pdf`
   ```

2. **Add PDF processing instructions**:
   ```markdown
   ### For local PDFs:
   - Use Read tool to read PDF content
   - Extract text and structure
   ```

---

## Testing Your Changes

### Manual Testing

After any change, run a full audit:

```bash
claude
> /audit-paper 2512.24601
```

Check:
- [ ] No error messages during execution
- [ ] All expected files are created
- [ ] Output makes sense
- [ ] New features work as expected

### Testing Checklist

Use this checklist after modifications:

```markdown
## Pre-Commit Testing Checklist

### Phase 1: Basic Functionality
- [ ] Audit starts without errors
- [ ] Paper is fetched successfully
- [ ] Progress updates are shown

### Phase 2: Agent A
- [ ] deconstruction.json is created
- [ ] JSON is valid (no syntax errors)
- [ ] All claim types are populated

### Phase 3: Parallel Agents
- [ ] Agent B output exists (math_audit.md)
- [ ] Agent C outputs exist (adversarial_review.md, contradicting_papers.md)
- [ ] Agent D outputs exist (verification/ folder)

### Phase 4: Agent E
- [ ] decision_memo.md is complete
- [ ] README.md is created
- [ ] Score is calculated correctly

### Phase 5: Final
- [ ] User is directed to README.md
- [ ] All artifact paths are correct
```

### Common Testing Issues

| Issue | Likely Cause | Solution |
|-------|--------------|----------|
| Agent doesn't run | Syntax error in skill file | Check markdown formatting |
| Missing output | Agent instructions incomplete | Add explicit output instructions |
| Wrong score | Weight calculation error | Check weights sum to 100% |
| Timeout | Too complex instructions | Simplify or break into steps |

---

## Code Style Guide

### Markdown Style

```markdown
# Main Heading (one per file)

## Section Heading

### Subsection

Regular paragraph text.

**Bold for emphasis**

`code for inline code`

```code block for multi-line code```

- Bullet lists
- Like this

1. Numbered lists
2. Like this

| Tables | Like |
|--------|------|
| This | Way |
```

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Skill files | `kebab-case.md` | `agent-a-deconstructor.md` |
| Output files | `snake_case.md` | `adversarial_review.md` |
| Folders | `snake_case` | `paper_audit` |
| JSON keys | `snake_case` | `theoretical_claims` |

### Best Practices

1. **Be explicit** - AI follows instructions literally
2. **Use examples** - Show what you want, not just describe it
3. **Add checklists** - Help AI track progress
4. **Include output templates** - Show exact format expected
5. **Test after changes** - Always verify modifications work

---

## Contributing

### How to Contribute

1. **Fork the repository** on GitHub
2. **Create a branch** for your feature
3. **Make your changes**
4. **Test thoroughly**
5. **Submit a pull request**

### What to Contribute

We welcome:
- Bug fixes
- New agents
- Documentation improvements
- Output format improvements
- New verification templates

### Pull Request Guidelines

Your PR should include:
- Clear description of changes
- Testing you performed
- Any documentation updates needed
- No breaking changes (or clear migration path)

### Getting Help

- **Questions:** Open a GitHub Discussion
- **Bugs:** Open a GitHub Issue
- **Features:** Discuss in Issues first

---

## Appendix: File Templates

### New Agent Template

```markdown
---
name: paper-audit:agent-x-name
description: Brief description of what this agent does
---

# Agent X: Name

You are Agent X in the Paper Audit Pipeline. Your role is to [description].

## Your Mission

1. [Primary goal]
2. [Secondary goal]
3. [Tertiary goal]

## Inputs

- `input/file.json` - Description

## Outputs

Create the following files:

1. `output_file.md` - Description

## Process

### Step 1: [Name]

[Instructions]

### Step 2: [Name]

[Instructions]

## Output Template

```markdown
# Output Title

## Section 1

[Content]

## Section 2

[Content]
```

## Checklist

Before completing:

- [ ] Item 1
- [ ] Item 2
- [ ] Item 3
```

### Verification Template

```python
# verification_template.py

"""
Verification script for [claim type]
Generated by Agent D
"""

def verify_claim(claim_id, expected, actual):
    """Verify a single claim."""
    result = {
        'claim_id': claim_id,
        'expected': expected,
        'actual': actual,
        'verified': abs(expected - actual) < 0.01
    }
    return result

def main():
    results = []

    # Add your verifications here
    results.append(verify_claim('E1', expected=58.0, actual=58.0))

    # Output results
    import json
    with open('results.json', 'w') as f:
        json.dump(results, f, indent=2)

if __name__ == '__main__':
    main()
```
