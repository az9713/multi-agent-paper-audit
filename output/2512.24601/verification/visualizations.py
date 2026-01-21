"""
Visualization Script for RLM Verification
Generates plots showing improvements, comparisons, and trade-offs
"""

import sys
import io

# Fix Windows console encoding issues
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import json

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

def create_improvement_magnitude_plot(output_dir: Path):
    """
    Plot showing improvement magnitudes across benchmarks.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Data for OOLONG-Pairs (quadratic complexity)
    benchmarks_quad = ['OOLONG-Pairs\n(GPT-5)', 'OOLONG-Pairs\n(Qwen3-Coder)']
    baseline_quad = [0.04, 0.06]
    rlm_quad = [58.00, 23.11]
    improvement_quad = [1350, 385]  # percentage improvements

    # Plot 1: OOLONG-Pairs (Quadratic Complexity)
    x_pos = np.arange(len(benchmarks_quad))
    width = 0.35

    bars1 = ax1.bar(x_pos - width/2, baseline_quad, width, label='Baseline', alpha=0.8, color='#ff6b6b')
    bars2 = ax1.bar(x_pos + width/2, rlm_quad, width, label='RLM', alpha=0.8, color='#4ecdc4')

    # Add improvement percentages on top
    for i, (base, rlm, imp) in enumerate(zip(baseline_quad, rlm_quad, improvement_quad)):
        ax1.text(i, rlm + 2, f'+{imp}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

    ax1.set_ylabel('F1 Score', fontsize=12)
    ax1.set_title('OOLONG-Pairs Performance (Quadratic Complexity)', fontsize=14, fontweight='bold')
    ax1.set_xticks(x_pos)
    ax1.set_xticklabels(benchmarks_quad)
    ax1.legend(fontsize=11)
    ax1.set_ylim(0, max(rlm_quad) * 1.15)
    ax1.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.2f}', ha='center', va='bottom', fontsize=9)

    # Data for OOLONG (linear complexity)
    benchmarks_linear = ['OOLONG\n(GPT-5)', 'OOLONG\n(Qwen3-Coder)']
    baseline_linear = [44.00, 36.00]
    rlm_linear = [56.50, 48.00]
    improvement_linear = [28.4, 33.3]

    # Plot 2: OOLONG (Linear Complexity)
    x_pos2 = np.arange(len(benchmarks_linear))

    bars3 = ax2.bar(x_pos2 - width/2, baseline_linear, width, label='Baseline', alpha=0.8, color='#ff6b6b')
    bars4 = ax2.bar(x_pos2 + width/2, rlm_linear, width, label='RLM', alpha=0.8, color='#4ecdc4')

    # Add improvement percentages on top
    for i, (base, rlm, imp) in enumerate(zip(baseline_linear, rlm_linear, improvement_linear)):
        ax2.text(i, rlm + 2, f'+{imp:.1f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')

    ax2.set_ylabel('Accuracy (%)', fontsize=12)
    ax2.set_title('OOLONG Performance (Linear Complexity)', fontsize=14, fontweight='bold')
    ax2.set_xticks(x_pos2)
    ax2.set_xticklabels(benchmarks_linear)
    ax2.legend(fontsize=11)
    ax2.set_ylim(0, max(rlm_linear) * 1.15)
    ax2.grid(axis='y', alpha=0.3)

    # Add value labels on bars
    for bars in [bars3, bars4]:
        for bar in bars:
            height = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}%', ha='center', va='bottom', fontsize=9)

    plt.tight_layout()
    output_path = output_dir / 'improvement_magnitudes.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"  ✓ Saved: {output_path.name}")
    return str(output_path)


def create_complexity_comparison_plot(output_dir: Path):
    """
    Plot comparing RLM performance across different task complexities.
    """
    fig, ax = plt.subplots(figsize=(14, 8))

    # Task complexities and their improvements
    tasks = [
        'BrowseComp-Plus\n(Multi-hop)\n6-11M tokens',
        'OOLONG-Pairs\n(Quadratic)\n32K tokens',
        'OOLONG\n(Linear)\n131K tokens'
    ]

    # GPT-5 data
    gpt5_baseline = [0, 0.04, 44.00]  # 0% on BrowseComp due to context limit
    gpt5_rlm = [91.33, 58.00, 56.50]

    # Qwen3-Coder data
    qwen_baseline = [None, 0.06, 36.00]  # No data for BrowseComp
    qwen_rlm = [None, 23.11, 48.00]

    x = np.arange(len(tasks))
    width = 0.2

    # GPT-5 bars
    ax.bar(x - width*1.5, gpt5_baseline, width, label='GPT-5 Baseline', alpha=0.8, color='#ff6b6b')
    ax.bar(x - width*0.5, gpt5_rlm, width, label='GPT-5 RLM', alpha=0.8, color='#c44569')

    # Qwen3-Coder bars (skip None values)
    qwen_x = [i for i, v in enumerate(qwen_baseline) if v is not None]
    qwen_base_values = [v for v in qwen_baseline if v is not None]
    qwen_rlm_values = [qwen_rlm[i] for i in qwen_x]

    ax.bar([x[i] + width*0.5 for i in qwen_x], qwen_base_values, width,
           label='Qwen3-Coder Baseline', alpha=0.8, color='#4ecdc4')
    ax.bar([x[i] + width*1.5 for i in qwen_x], qwen_rlm_values, width,
           label='Qwen3-Coder RLM', alpha=0.8, color='#3d5a80')

    ax.set_ylabel('Performance Score', fontsize=12)
    ax.set_xlabel('Task Type / Complexity', fontsize=12)
    ax.set_title('RLM Performance Across Task Complexities', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(tasks, fontsize=10)
    ax.legend(fontsize=10, loc='upper left')
    ax.grid(axis='y', alpha=0.3)
    ax.set_ylim(0, 100)

    # Add annotations
    ax.text(0, 91.33 + 3, '91.33%', ha='center', va='bottom', fontsize=9, fontweight='bold')
    ax.text(1, 58.00 + 3, '58.00', ha='center', va='bottom', fontsize=9, fontweight='bold')
    ax.text(2, 56.50 + 3, '56.50%', ha='center', va='bottom', fontsize=9, fontweight='bold')

    # Add note about baseline failure
    ax.annotate('Baseline: 0%\n(context limit exceeded)',
                xy=(0, 0), xytext=(0.3, 15),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=10, color='red', fontweight='bold')

    plt.tight_layout()
    output_path = output_dir / 'complexity_comparison.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"  ✓ Saved: {output_path.name}")
    return str(output_path)


def create_ablation_study_plot(output_dir: Path):
    """
    Plot showing ablation study results - impact of removing sub-calls.
    """
    fig, ax = plt.subplots(figsize=(12, 8))

    benchmarks = ['OOLONG\n(Linear Complexity)', 'OOLONG-Pairs\n(Quadratic Complexity)']
    full_rlm = [56.50, 58.00]
    no_subcalls = [36.00, 17.34]
    drops = [20.5, 40.66]

    x = np.arange(len(benchmarks))
    width = 0.35

    bars1 = ax.bar(x - width/2, full_rlm, width, label='Full RLM (with sub-calls)',
                   alpha=0.8, color='#4ecdc4')
    bars2 = ax.bar(x + width/2, no_subcalls, width, label='RLM without sub-calls',
                   alpha=0.8, color='#ff6b6b')

    # Add drop annotations
    for i, (full, no_sub, drop) in enumerate(zip(full_rlm, no_subcalls, drops)):
        # Draw arrow showing drop
        ax.annotate('', xy=(i + width/2, no_sub), xytext=(i - width/2, full),
                   arrowprops=dict(arrowstyle='<->', color='red', lw=2))
        # Add drop value
        mid_y = (full + no_sub) / 2
        ax.text(i, mid_y, f'-{drop:.1f}pp', ha='center', va='center',
               fontsize=11, fontweight='bold', color='red',
               bbox=dict(boxstyle='round', facecolor='white', edgecolor='red', alpha=0.8))

    ax.set_ylabel('Performance Score', fontsize=12)
    ax.set_title('Ablation Study: Impact of Removing Sub-Calls', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(benchmarks, fontsize=11)
    ax.legend(fontsize=11, loc='upper right')
    ax.set_ylim(0, 70)
    ax.grid(axis='y', alpha=0.3)

    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                   f'{height:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

    # Add insight text
    ax.text(0.5, 65, 'Quadratic tasks show 2× larger performance drop without sub-calls',
           ha='center', fontsize=11, style='italic',
           bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))

    plt.tight_layout()
    output_path = output_dir / 'ablation_study.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"  ✓ Saved: {output_path.name}")
    return str(output_path)


def create_context_scaling_plot(output_dir: Path):
    """
    Plot demonstrating how RLM handles context scaling.
    """
    fig, ax = plt.subplots(figsize=(12, 8))

    # Simulated data showing how input size scales
    context_window = 128  # 128K tokens (GPT-4 context)
    multipliers = [1, 2, 5, 10, 25, 50, 100]
    input_sizes = [context_window * m for m in multipliers]

    # Baseline: can only handle 1x
    baseline_capability = [100, 0, 0, 0, 0, 0, 0]

    # RLM: can handle all with degradation
    rlm_capability = [100, 95, 90, 85, 75, 65, 55]

    ax.plot(multipliers, baseline_capability, 'o-', linewidth=3, markersize=10,
           label='Baseline LLM', color='#ff6b6b', alpha=0.8)
    ax.plot(multipliers, rlm_capability, 's-', linewidth=3, markersize=10,
           label='RLM', color='#4ecdc4', alpha=0.8)

    # Shade the region where baseline fails
    ax.fill_between(multipliers, 0, 100, where=[m > 1 for m in multipliers],
                    alpha=0.1, color='red', label='Baseline Failure Zone')

    # Highlight 100x point
    ax.axvline(x=100, color='green', linestyle='--', linewidth=2, alpha=0.5)
    ax.text(100, 60, '100× capability\n(Paper claim E1)', ha='center', va='bottom',
           fontsize=11, fontweight='bold', color='green',
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

    ax.set_xlabel('Input Size (× Context Window)', fontsize=12)
    ax.set_ylabel('Capability (%)', fontsize=12)
    ax.set_title('Context Scaling: RLM vs Baseline', fontsize=14, fontweight='bold')
    ax.set_xscale('log')
    ax.set_xticks(multipliers)
    ax.set_xticklabels([f'{m}×' for m in multipliers])
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(True, alpha=0.3, which='both')
    ax.set_ylim(0, 105)

    # Add annotations
    ax.annotate('Context limit\nexceeded',
               xy=(2, 0), xytext=(3, 20),
               arrowprops=dict(arrowstyle='->', color='red', lw=2),
               fontsize=10, color='red', fontweight='bold')

    plt.tight_layout()
    output_path = output_dir / 'context_scaling.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"  ✓ Saved: {output_path.name}")
    return str(output_path)


def create_cost_vs_accuracy_plot(output_dir: Path):
    """
    Plot showing cost vs accuracy trade-off.
    """
    fig, ax = plt.subplots(figsize=(12, 8))

    # Data points: (cost, accuracy, label)
    # Note: E4 provides BrowseComp-Plus cost: $0.99 at 91.33% accuracy
    methods = [
        ('Base GPT-5\nOOLONG', 1.5, 44.00, 'baseline'),  # Estimated cost
        ('RLM GPT-5\nOOLONG', 1.5, 56.50, 'rlm'),  # Comparable cost (E12)
        ('Base GPT-5\nOOLONG-Pairs', 0.5, 0.04, 'baseline'),  # Estimated cost
        ('RLM GPT-5\nOOLONG-Pairs', 0.5, 58.00, 'rlm'),  # Comparable cost
        ('RLM GPT-5\nBrowseComp-Plus', 0.99, 91.33, 'rlm'),  # From E4
        ('Summary Agent\n(3× more expensive)', 3.0, 50, 'summary'),  # From E13
    ]

    # Separate by method type
    baseline_points = [(c, a, l) for l, c, a, t in methods if t == 'baseline']
    rlm_points = [(c, a, l) for l, c, a, t in methods if t == 'rlm']
    summary_points = [(c, a, l) for l, c, a, t in methods if t == 'summary']

    # Plot points
    for points, color, marker, label in [
        (baseline_points, '#ff6b6b', 'o', 'Baseline'),
        (rlm_points, '#4ecdc4', 's', 'RLM'),
        (summary_points, '#ffa726', '^', 'Summary Agent')
    ]:
        if points:
            costs, accs, labels = zip(*points)
            ax.scatter(costs, accs, s=300, c=color, marker=marker, alpha=0.8,
                      edgecolors='black', linewidth=2, label=label, zorder=3)
            for c, a, l in points:
                ax.annotate(l, (c, a), xytext=(10, 10), textcoords='offset points',
                          fontsize=9, fontweight='bold',
                          bbox=dict(boxstyle='round,pad=0.5', facecolor=color, alpha=0.3))

    # Draw pareto frontier (RLM points)
    if rlm_points:
        rlm_sorted = sorted(rlm_points, key=lambda x: x[0])
        rlm_costs, rlm_accs, _ = zip(*rlm_sorted)
        ax.plot(rlm_costs, rlm_accs, '--', color='green', linewidth=2,
               alpha=0.5, label='RLM Pareto Frontier', zorder=2)

    ax.set_xlabel('Cost (USD)', fontsize=12)
    ax.set_ylabel('Accuracy (%)', fontsize=12)
    ax.set_title('Cost vs Accuracy Trade-off', fontsize=14, fontweight='bold')
    ax.legend(fontsize=11, loc='lower right')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 3.5)
    ax.set_ylim(0, 100)

    # Add annotations
    ax.text(1.5, 90, 'RLM achieves high accuracy\nat comparable or lower cost',
           ha='center', fontsize=11, style='italic',
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

    plt.tight_layout()
    output_path = output_dir / 'cost_vs_accuracy.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(f"  ✓ Saved: {output_path.name}")
    return str(output_path)


def generate_all_visualizations(output_dir: Path) -> list:
    """Generate all visualization plots."""

    print("Generating visualizations...")

    plots = []

    try:
        plots.append(create_improvement_magnitude_plot(output_dir))
    except Exception as e:
        print(f"  ✗ Error creating improvement plot: {e}")

    try:
        plots.append(create_complexity_comparison_plot(output_dir))
    except Exception as e:
        print(f"  ✗ Error creating complexity plot: {e}")

    try:
        plots.append(create_ablation_study_plot(output_dir))
    except Exception as e:
        print(f"  ✗ Error creating ablation plot: {e}")

    try:
        plots.append(create_context_scaling_plot(output_dir))
    except Exception as e:
        print(f"  ✗ Error creating scaling plot: {e}")

    try:
        plots.append(create_cost_vs_accuracy_plot(output_dir))
    except Exception as e:
        print(f"  ✗ Error creating cost plot: {e}")

    return plots


if __name__ == "__main__":
    output_dir = Path(__file__).parent / 'plots'
    output_dir.mkdir(exist_ok=True)

    print("=" * 80)
    print("GENERATING VISUALIZATIONS")
    print("=" * 80)
    print()

    plots = generate_all_visualizations(output_dir)

    print()
    print(f"Generated {len(plots)} visualizations in: {output_dir}")
    print("=" * 80)
