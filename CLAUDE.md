# CLAUDE.md - Instructions for Claude Code

This file tells Claude Code how to work with this repository.

## Project Overview

This is a **multi-agent paper auditing pipeline** that uses 5 specialized AI agents to rigorously review scientific papers from arXiv. The main entry point is the `paper-audit` skill.

## Repository Structure

```
.claude/
├── skills/paper-audit/       # Main skill definitions
│   ├── SKILL.md              # Orchestrator (main entry point)
│   ├── agent-a-deconstructor.md
│   ├── agent-b-formalist.md
│   ├── agent-c-skeptic.md
│   ├── agent-d-verifier.md
│   └── agent-e-editor.md
└── prompts/paper-audit/      # Templates and helpers

output/                       # Generated audit outputs (per paper)
docs/                         # Documentation
```

## Key Commands

### Primary Command
Ask Claude to audit a paper:
```
Audit this paper: <arXiv-URL-or-ID>
```

Examples:
- `Audit this paper: https://arxiv.org/pdf/2512.24601`
- `Audit this paper: arXiv:2512.24601`
- `Audit paper 2512.24601`

### What It Does
1. Fetches the paper from arXiv
2. Runs 5 agents in sequence (A → B,C,D parallel → E)
3. Generates comprehensive audit in `output/{paper_id}/`
4. Points user to `README.md` as entry point

## Agent Roles

| Agent | Role | Weight | Output |
|-------|------|--------|--------|
| A | Deconstructor | - | `deconstruction.json` |
| B | Math Formalist | 30% | `math_audit.md` |
| C | Skeptic Adversary | 40% | `adversarial_review.md`, `contradicting_papers.md` |
| D | Code Verifier | 30% | `verification/` directory |
| E | Editor-in-Chief | - | `decision_memo.md`, `README.md`, research outputs |

## Development Guidelines

### When Modifying Skills
1. Skills are in `.claude/skills/paper-audit/`
2. Each agent has its own markdown file
3. `SKILL.md` is the main orchestrator
4. Test changes with a real paper audit

### When Adding Features
1. Update the relevant agent file
2. Update `SKILL.md` if changing the pipeline flow
3. Update `agent-e-editor.md` if changing outputs
4. Update documentation in `docs/`

### Code Style
- Use clear, descriptive variable names
- Add comments explaining non-obvious logic
- Follow existing patterns in the codebase

## Output Structure

Every audit creates:
```
output/{paper_id}/
├── README.md                  # User entry point (ALWAYS CREATE THIS)
├── deconstruction.json        # Agent A output
├── math_audit.md              # Agent B output
├── adversarial_review.md      # Agent C output
├── contradicting_papers.md    # Agent C output
├── decision_memo.md           # Agent E output
├── FULL_RESEARCH_PROPOSAL.md  # Agent E output
├── literature_gaps.md         # Agent E output
├── exploration_notebook.ipynb # Agent E output
└── verification/              # Agent D output
    ├── main.py
    ├── results.json
    ├── execution_log.txt
    └── plots/
```

## Important Notes

1. **Always create README.md** in output directory to guide users
2. **Run agents B, C, D in parallel** for efficiency
3. **Point users to README.md** at the end of every audit
4. **Use Task tool** to spawn agents, not direct skill invocation
5. **WebFetch for arXiv** - use both `/abs/` and `/html/` endpoints

## Testing

To test changes:
```bash
claude
> Audit this paper: 2512.24601
```

Check that:
- [ ] All output files are created
- [ ] README.md exists and has correct structure
- [ ] Decision memo has proper scoring
- [ ] No errors in execution

## Common Issues

### Paper Not Found
- Check arXiv ID format
- Try different URL formats

### Agent Timeout
- Increase timeout in SKILL.md
- Check internet connection

### Missing Outputs
- Check agent completion status
- Look for error messages in logs
