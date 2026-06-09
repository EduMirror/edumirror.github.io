from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.lines import Line2D


LABELS = [
    "Peer & Group Dynamics",
    "Individual Social Cognition",
    "Classroom Culture",
    "Home-School Dynamics",
]

COUNTS = [7, 5, 3, 5]

# Cleaner, publication-friendly palette with clearer separation.
COLORS = [
    "#4F6BED",
    "#2C9AB7",
    "#3FA67A",
    "#F2A541",
]

OUTPUT_PATH = Path("assets") / "Figure3_scenario_distribution_pie.pdf"


def autopct_percent_only():
    def _formatter(pct):
        return f"{pct:.1f}%"

    return _formatter


def luminance(hex_color):
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16) / 255.0
    g = int(hex_color[2:4], 16) / 255.0
    b = int(hex_color[4:6], 16) / 255.0
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def main():
    plt.rcParams.update(
        {
            "font.family": "serif",
            "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
            "font.size": 11,
            "axes.edgecolor": "#333333",
            "text.color": "#222222",
            "figure.facecolor": "white",
            "savefig.facecolor": "white",
            "pdf.fonttype": 42,
            "ps.fonttype": 42,
        }
    )

    total = sum(COUNTS)

    fig, ax = plt.subplots(figsize=(8.2, 4.8), constrained_layout=True)

    wedges, _, autotexts = ax.pie(
        COUNTS,
        colors=COLORS,
        startangle=90,
        counterclock=False,
        autopct=autopct_percent_only(),
        pctdistance=0.72,
        radius=0.78,
        wedgeprops={"edgecolor": "white", "linewidth": 1.6, "width": 0.42},
    )

    for index, text in enumerate(autotexts):
        text.set_fontsize(15)
        text.set_fontweight("bold")
        text.set_fontfamily("DejaVu Sans")
        text.set_color("white" if luminance(COLORS[index]) < 0.55 else "#1f1f1f")

    centre_circle = Circle((0, 0), 0.36, fc="white", ec="none")
    ax.add_artist(centre_circle)
    ax.text(
        0,
        0.03,
        f"{total}",
        ha="center",
        va="center",
        fontsize=20,
        fontweight="bold",
        fontfamily="DejaVu Sans",
        color="#25344D",
    )
    ax.text(
        0,
        -0.12,
        "scenarios",
        ha="center",
        va="center",
        fontsize=10.5,
        fontweight="semibold",
        fontfamily="DejaVu Sans",
        color="#67768F",
    )

    ax.set_aspect("equal")

    legend_handles = [
        Line2D(
            [0],
            [0],
            marker="s",
            linestyle="None",
            markerfacecolor=color,
            markeredgecolor=color,
            markersize=10,
        )
        for color in COLORS
    ]

    legend_labels = [
        f"{label}: {count}"
        for label, count in zip(LABELS, COUNTS)
    ]

    ax.legend(
        legend_handles,
        legend_labels,
        loc="center left",
        bbox_to_anchor=(0.94, 0.5),
        frameon=False,
        handlelength=0.8,
        handletextpad=0.9,
        labelspacing=1.3,
        borderaxespad=0.0,
        fontsize=12.5,
    )

    for spine in ax.spines.values():
        spine.set_visible(False)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, format="pdf", bbox_inches="tight")
    plt.close(fig)

    print(f"Saved PDF figure to: {OUTPUT_PATH.resolve()}")


if __name__ == "__main__":
    main()
