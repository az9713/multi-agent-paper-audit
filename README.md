# Multi-Agent Paper Audit

A rigorous 5-agent pipeline for auditing scientific papers from arXiv. This tool helps researchers, reviewers, and students critically evaluate academic papers through automated adversarial review, mathematical verification, and code execution.

## What This Tool Does

When you give it an arXiv paper, it:

1. **Extracts all claims** - Finds every theoretical, empirical, and novelty claim
2. **Audits the math** - Checks calculations, formulas, and statistical rigor
3. **Asks tough questions** - Generates adversarial questions a skeptical reviewer would ask
4. **Verifies with code** - Runs verification scripts to check numerical claims
5. **Produces a verdict** - Synthesizes everything into a decision memo

## Quick Example

```bash
# Audit a paper from arXiv
claude
> /audit-paper https://arxiv.org/pdf/2512.24601
```

**Output:** A complete audit with decision memo, adversarial review, and research directions.

## Documentation

| Document | Description | Who It's For |
|----------|-------------|--------------|
| [Quick Start Guide](docs/QUICK_START.md) | Get running in 5 minutes with 10 example use cases | Everyone |
| [User Guide](docs/USER_GUIDE.md) | Complete guide to using the tool | Users |
| [Installation Guide](docs/INSTALLATION.md) | Step-by-step setup instructions | New users |
| [Developer Guide](docs/DEVELOPER_GUIDE.md) | How to modify and extend the tool | Developers |
| [Architecture](docs/ARCHITECTURE.md) | System design and how it works | Developers |
| [Troubleshooting](docs/TROUBLESHOOTING.md) | Common problems and solutions | Everyone |

## Requirements

- **Claude Code CLI** - The AI-powered command line tool
- **Python 3.8+** - For running verification scripts
- **Internet connection** - For fetching papers and web searches

## Installation (30 seconds)

```bash
# 1. Clone this repository
git clone https://github.com/az9713/multi-agent-paper-audit.git
cd multi-agent-paper-audit

# 2. That's it! The skills are ready to use with Claude Code
claude
```

## Sample Output

After auditing a paper, you get:

```
output/2512.24601/
├── README.md                 ← START HERE - Reading guide
├── decision_memo.md          ← Final verdict and score
├── adversarial_review.md     ← Critical analysis
├── math_audit.md             ← Mathematical rigor check
├── deconstruction.json       ← All extracted claims
├── FULL_RESEARCH_PROPOSAL.md ← Future research directions
└── verification/
    ├── main.py               ← Verification code
    ├── results.json          ← Verification results
    └── plots/                ← Generated visualizations
```

## How It Works

```
┌─────────────────────────────────────────────────────────────┐
│                    You: /audit-paper                         │
└──────────────────────────┬──────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────┐
│              Agent A: Deconstructor                          │
│   Extracts all claims from the paper                         │
└──────────────────────────┬──────────────────────────────────┘
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Agent B    │    │  Agent C    │    │  Agent D    │
│  Math Audit │    │  Skeptic    │    │  Verifier   │
│  (30%)      │    │  (40%)      │    │  (30%)      │
└──────┬──────┘    └──────┬──────┘    └──────┬──────┘
       │                  │                  │
       └──────────────────┼──────────────────┘
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              Agent E: Editor-in-Chief                        │
│   Synthesizes all reports → Final Decision                   │
└─────────────────────────────────────────────────────────────┘
```

## Scoring System

| Score | Verdict | Meaning |
|-------|---------|---------|
| 8.0 - 10.0 | ACCEPT | Strong paper, minor issues at most |
| 6.0 - 7.9 | ACCEPT WITH RESERVATIONS | Good but notable concerns |
| 4.0 - 5.9 | MAJOR REVISION | Substantial issues need fixing |
| 2.0 - 3.9 | REJECT (Revise & Resubmit) | Fundamental problems |
| 0.0 - 1.9 | REJECT | Fatally flawed |

## Contributing

We welcome contributions! See the [Developer Guide](docs/DEVELOPER_GUIDE.md) for how to get started.

## License

MIT License - See [LICENSE](LICENSE) for details.

## Support

- **Issues:** [GitHub Issues](https://github.com/az9713/multi-agent-paper-audit/issues)
- **Discussions:** [GitHub Discussions](https://github.com/az9713/multi-agent-paper-audit/discussions)
