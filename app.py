import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from pathlib import Path

# ==============================
# Page configuration
# ==============================

st.set_page_config(
    page_title="NBA Lineup Optimization Dashboard",
    page_icon="🏀",
    layout="wide"
)

# ==============================
# Load data
# ==============================

DATA_DIR = Path("data/processed")

@st.cache_data
def load_data():
    summary = pd.read_csv(DATA_DIR / "dashboard_summary.csv")
    players = pd.read_csv(DATA_DIR / "dashboard_players.csv")
    lineups = pd.read_csv(DATA_DIR / "dashboard_lineups.csv")
    pairs = pd.read_csv(DATA_DIR / "dashboard_pairs.csv")
    high_value = pd.read_csv(DATA_DIR / "dashboard_high_value_lineups.csv")
    underused = pd.read_csv(DATA_DIR / "dashboard_underused_lineups.csv")

    return summary, players, lineups, pairs, high_value, underused


summary, players, lineups, pairs, high_value, underused = load_data()

# ==============================
# Header
# ==============================

st.title("🏀 NBA Player Impact & Lineup Optimization Dashboard")

st.markdown(
    """
    This dashboard explores player impact, lineup performance, and player-pair synergy
    using reconstructed lineup stints from NBA play-by-play data.
    """
)

# ==============================
# KPI cards
# ==============================

st.subheader("Project Summary")

kpi_cols = st.columns(4)

summary_dict = dict(zip(summary["metric"], summary["value"]))

kpi_cols[0].metric(
    "Players Analyzed",
    summary_dict.get("Reliable players", 0)
)

kpi_cols[1].metric(
    "Reliable Lineups",
    summary_dict.get("Reliable lineups", 0)
)

kpi_cols[2].metric(
    "Reliable Pairs",
    summary_dict.get("Reliable player pairs", 0)
)

kpi_cols[3].metric(
    "High-Value Lineups",
    summary_dict.get("High-value lineups", 0)
)

st.divider()

# ==============================
# Sidebar filters
# ==============================

st.sidebar.header("Filters")

min_player_duration = st.sidebar.slider(
    "Minimum player duration",
    min_value=0,
    max_value=int(players["total_duration"].max()),
    value=0,
    step=60
)

min_lineup_duration = st.sidebar.slider(
    "Minimum lineup duration",
    min_value=0,
    max_value=int(lineups["total_duration"].max()),
    value=0,
    step=60
)

min_pair_duration = st.sidebar.slider(
    "Minimum pair duration",
    min_value=0,
    max_value=int(pairs["total_duration"].max()),
    value=0,
    step=60
)

filtered_players = players[players["total_duration"] >= min_player_duration].copy()
filtered_lineups = lineups[lineups["total_duration"] >= min_lineup_duration].copy()
filtered_pairs = pairs[pairs["total_duration"] >= min_pair_duration].copy()

# ==============================
# Tabs
# ==============================

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Player Impact",
    "Lineup Performance",
    "Pair Synergy",
    "High-Value Lineups",
    "Underused Watchlist"
])

# ==============================
# Tab 1 — Player Impact
# ==============================

with tab1:
    st.header("Player Impact")

    st.markdown(
        """
        Players are ranked by time-normalized impact. Higher values indicate stronger
        net scoring outcomes while the player was on the court.
        """
    )

    top_players = filtered_players.sort_values(
        "impact_per_60_sec", ascending=False
    ).head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_players["player_name"], top_players["impact_per_60_sec"])
    ax.set_xlabel("Impact per 60 Seconds")
    ax.set_title("Top Player Impact")
    ax.invert_yaxis()
    st.pyplot(fig)

    st.dataframe(
        filtered_players.sort_values("impact_per_60_sec", ascending=False),
        use_container_width=True
    )

# ==============================
# Tab 2 — Lineup Performance
# ==============================

with tab2:
    st.header("Lineup Performance")

    st.markdown(
        """
        Lineups are evaluated using net points per 60 seconds and total duration.
        The most useful lineups combine positive impact with meaningful playing time.
        """
    )

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(
        filtered_lineups["total_duration"],
        filtered_lineups["net_per_60"],
        alpha=0.7
    )
    ax.axhline(0, linestyle="--", linewidth=1)
    ax.set_xlabel("Total Duration (seconds)")
    ax.set_ylabel("Net Points per 60 Seconds")
    ax.set_title("Lineup Usage vs Performance")
    st.pyplot(fig)

    st.dataframe(
        filtered_lineups.sort_values("net_per_60", ascending=False),
        use_container_width=True
    )

# ==============================
# Tab 3 — Pair Synergy
# ==============================

with tab3:
    st.header("Player Pair Synergy")

    st.markdown(
        """
        Pair synergy measures how two-player combinations perform together.
        Results should be interpreted alongside total duration and stint count.
        """
    )

    filtered_pairs["pair_name"] = (
        filtered_pairs["player_1_name"].astype(str)
        + " + "
        + filtered_pairs["player_2_name"].astype(str)
    )

    top_pairs = filtered_pairs.sort_values(
        ["impact_per_60", "total_duration"],
        ascending=[False, False]
    ).head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_pairs["pair_name"], top_pairs["impact_per_60"])
    ax.set_xlabel("Impact per 60 Seconds")
    ax.set_title("Top Player Pair Synergies")
    ax.invert_yaxis()
    st.pyplot(fig)

    st.dataframe(
        filtered_pairs.sort_values(
            ["impact_per_60", "total_duration"],
            ascending=[False, False]
        ),
        use_container_width=True
    )

# ==============================
# Tab 4 — High-Value Lineups
# ==============================

with tab4:
    st.header("High-Value Lineups")

    st.markdown(
        """
        High-value lineups combine positive performance with meaningful usage.
        These are strong candidates for deeper analysis.
        """
    )

    st.dataframe(
        high_value.sort_values("net_per_60", ascending=False),
        use_container_width=True
    )

# ==============================
# Tab 5 — Underused Watchlist
# ==============================

with tab5:
    st.header("Underused Lineup Watchlist")

    st.markdown(
        """
        These lineups showed positive performance but were not among the highest-usage units.
        They should be treated as exploratory candidates, not definitive recommendations.
        """
    )

    if len(underused) == 0:
        st.info("No underused lineup candidates were identified under the current criteria.")
    else:
        st.dataframe(
            underused.sort_values("net_per_60", ascending=False),
            use_container_width=True
        )

# ==============================
# Footer
# ==============================

st.divider()

st.markdown(
    """
    **Note:** This dashboard is based on a single-game prototype. Metrics are descriptive
    and should not be interpreted as definitive player or lineup evaluations.
    """
)