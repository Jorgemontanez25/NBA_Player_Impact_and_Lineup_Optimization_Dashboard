import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="NBA Lineup Optimization Dashboard",
    page_icon="🏀",
    layout="wide"
)

DATA_DIR = Path("data/processed")


@st.cache_data
def load_data():
    return {
        "summary": pd.read_csv(DATA_DIR / "dashboard_summary.csv"),
        "players": pd.read_csv(DATA_DIR / "dashboard_players.csv"),
        "lineups": pd.read_csv(DATA_DIR / "dashboard_lineups.csv"),
        "pairs": pd.read_csv(DATA_DIR / "dashboard_pairs.csv"),
        "model_results": pd.read_csv(DATA_DIR / "dashboard_model_results.csv"),
        "feature_importance": pd.read_csv(DATA_DIR / "dashboard_feature_importance.csv"),
        "teams": pd.read_csv(DATA_DIR / "matchup_teams.csv"),
        "rosters": pd.read_csv(DATA_DIR / "matchup_team_rosters.csv"),
        "recommendations": pd.read_csv(DATA_DIR / "matchup_recommendation_lineups.csv"),
        "opponent_profiles": pd.read_csv(DATA_DIR / "matchup_opponent_player_profiles.csv"),
    }


data = load_data()

summary = data["summary"]
players = data["players"]
lineups = data["lineups"]
pairs = data["pairs"]
model_results = data["model_results"]
feature_importance = data["feature_importance"]
teams = data["teams"]
rosters = data["rosters"]
recommendations = data["recommendations"]
opponent_profiles = data["opponent_profiles"]


def clean_lineup_names(lineup_display):
    if pd.isna(lineup_display):
        return []
    return [name.strip() for name in str(lineup_display).split("|")]


def create_court_html(home_team, away_team, home_players, away_players):
    home_positions = [
        ("11%", "45%"),
        ("23%", "24%"),
        ("23%", "66%"),
        ("36%", "35%"),
        ("36%", "58%"),
    ]

    away_positions = [
        ("78%", "45%"),
        ("66%", "24%"),
        ("66%", "66%"),
        ("53%", "35%"),
        ("53%", "58%"),
    ]

    html = """
    <html>
    <head>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: transparent;
        }

        .court {
            background: linear-gradient(90deg, #b96d32 0%, #d8914a 50%, #b96d32 100%);
            border: 4px solid white;
            border-radius: 18px;
            height: 430px;
            position: relative;
            box-shadow: 0px 4px 18px rgba(0,0,0,0.35);
            overflow: hidden;
        }

        .half-line {
            position: absolute;
            left: 50%;
            top: 0;
            width: 4px;
            height: 100%;
            background: white;
            opacity: 0.85;
        }

        .center-circle {
            position: absolute;
            left: calc(50% - 55px);
            top: calc(50% - 55px);
            width: 110px;
            height: 110px;
            border: 4px solid white;
            border-radius: 50%;
            opacity: 0.85;
        }

        .paint-left {
            position: absolute;
            left: 0;
            top: 145px;
            width: 135px;
            height: 140px;
            border: 4px solid white;
            border-left: none;
            opacity: 0.85;
        }

        .paint-right {
            position: absolute;
            right: 0;
            top: 145px;
            width: 135px;
            height: 140px;
            border: 4px solid white;
            border-right: none;
            opacity: 0.85;
        }

        .player-dot {
            position: absolute;
            width: 130px;
            min-height: 44px;
            border-radius: 999px;
            color: white;
            text-align: center;
            padding: 8px 10px;
            font-size: 12px;
            font-weight: 700;
            border: 2px solid white;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 3px 8px rgba(0,0,0,0.35);
        }

        .home-dot {
            background: #2563eb;
        }

        .away-dot {
            background: #dc2626;
        }

        .team-label-left {
            position: absolute;
            left: 20px;
            top: 15px;
            color: white;
            font-weight: 900;
            font-size: 18px;
            text-shadow: 1px 1px 4px black;
        }

        .team-label-right {
            position: absolute;
            right: 20px;
            top: 15px;
            color: white;
            font-weight: 900;
            font-size: 18px;
            text-shadow: 1px 1px 4px black;
        }
    </style>
    </head>
    <body>
    """

    html += f"""
    <div class="court">
        <div class="team-label-left">{home_team}</div>
        <div class="team-label-right">{away_team}</div>
        <div class="half-line"></div>
        <div class="center-circle"></div>
        <div class="paint-left"></div>
        <div class="paint-right"></div>
    """

    for player, (left, top) in zip(home_players, home_positions):
        html += f"""
        <div class="player-dot home-dot" style="left:{left}; top:{top};">
            {player}
        </div>
        """

    for player, (left, top) in zip(away_players, away_positions):
        html += f"""
        <div class="player-dot away-dot" style="left:{left}; top:{top};">
            {player}
        </div>
        """

    html += """
    </div>
    </body>
    </html>
    """

    return html


# ==============================
# Header
# ==============================

st.title("🏀 NBA Player Impact & Lineup Optimization Dashboard")

st.markdown(
    """
    Multi-game NBA analytics dashboard for player impact, lineup performance,
    pair synergy, predictive modeling, and matchup-based lineup recommendations.
    """
)

st.info(
    "Prototype note: recommendations are decision-support signals based on reconstructed historical stints, not definitive coaching instructions."
)

summary_dict = dict(zip(summary["metric"], summary["value"]))

k1, k2, k3, k4 = st.columns(4)
k1.metric("Reliable Players", int(summary_dict.get("Reliable players", 0)))
k2.metric("Reliable Lineups", int(summary_dict.get("Reliable lineups", 0)))
k3.metric("Reliable Pairs", int(summary_dict.get("Reliable player pairs", 0)))
k4.metric("Models Evaluated", int(summary_dict.get("Models evaluated", 0)))

st.divider()

tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏀 Matchup Recommender",
    "Player Impact",
    "Lineup Performance",
    "Pair Synergy",
    "Modeling",
    "Feature Importance"
])


# ==============================
# Matchup Recommender
# ==============================

with tab0:
    st.header("🏀 Matchup-Based Lineup Recommender")

    st.markdown(
        """
        Select your team, select the opponent, define the opponent starting five, and receive
        recommended lineups based on historical lineup performance, player impact, and reliability.
        """
    )

    team_names = sorted(teams["team_name"].dropna().unique())

    col_a, col_b = st.columns(2)

    with col_a:
        selected_team = st.selectbox("Your Team", team_names)

    with col_b:
        opponent_team_options = [team for team in team_names if team != selected_team]
        selected_opponent = st.selectbox("Opponent Team", opponent_team_options)

    selected_team_id = teams.loc[
        teams["team_name"] == selected_team, "team_id"
    ].iloc[0]

    opponent_team_id = teams.loc[
        teams["team_name"] == selected_opponent, "team_id"
    ].iloc[0]

    opponent_roster = (
        rosters[rosters["team_id"].astype(str) == str(opponent_team_id)]
        .sort_values("player_name")
    )

    opponent_players = opponent_roster["player_name"].dropna().unique().tolist()

    st.subheader("Opponent Starting Lineup")

    selected_opponent_players = st.multiselect(
        "Select exactly 5 opponent players",
        opponent_players,
        default=opponent_players[:5] if len(opponent_players) >= 5 else opponent_players,
        max_selections=5
    )

    if len(selected_opponent_players) != 5:
        st.warning("Please select exactly 5 opponent players to generate a matchup recommendation.")
    else:
        opponent_profiles_selected = opponent_profiles[
            opponent_profiles["player_name"].isin(selected_opponent_players)
        ]

        opponent_strength = opponent_profiles_selected["impact_per_60_sec"].mean()

        team_recommendations = recommendations[
            recommendations["team_id"].astype(str) == str(selected_team_id)
        ].copy()

        if team_recommendations.empty:
            st.warning("No historical lineup candidates found for this team in the processed sample.")
        else:
            team_recommendations["matchup_adjusted_score"] = (
                team_recommendations["recommendation_score"]
                + team_recommendations["avg_player_impact"]
                - opponent_strength
            )

            recommended = (
                team_recommendations
                .sort_values(
                    ["matchup_adjusted_score", "total_duration"],
                    ascending=[False, False]
                )
                .head(5)
                .copy()
            )

            best_lineup = recommended.iloc[0]
            best_players = clean_lineup_names(best_lineup["lineup_display"])

            st.subheader("Recommended Matchup View")

            components.html(
                create_court_html(
                    selected_team,
                    selected_opponent,
                    best_players,
                    selected_opponent_players
                ),
                height=460,
                scrolling=False
            )

            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Best Score", round(best_lineup["matchup_adjusted_score"], 2))
            c2.metric("Net per 60", round(best_lineup["net_per_60"], 2))
            c3.metric("Avg Player Impact", round(best_lineup["avg_player_impact"], 3))
            c4.metric("Historical Duration", int(best_lineup["total_duration"]))

            st.subheader("Top Recommended Lineups")

            display_cols = [
                "team_name",
                "lineup_display",
                "net_per_60",
                "avg_player_impact",
                "total_duration",
                "total_stints",
                "recommendation_score",
                "matchup_adjusted_score"
            ]

            available_cols = [col for col in display_cols if col in recommended.columns]

            st.dataframe(
                recommended[available_cols],
                use_container_width=True,
                hide_index=True
            )

            st.subheader("Recommendation Score Comparison")

            fig, ax = plt.subplots(figsize=(10, 5))
            labels = [f"Lineup {i+1}" for i in range(len(recommended))]
            ax.bar(labels, recommended["matchup_adjusted_score"])
            ax.set_ylabel("Matchup Adjusted Score")
            ax.set_title("Top Recommended Lineups")
            st.pyplot(fig)


# ==============================
# Player Impact
# ==============================

with tab1:
    st.header("Player Impact")

    min_player_duration = st.slider(
        "Minimum player duration",
        min_value=0,
        max_value=int(players["total_duration"].max()),
        value=0,
        step=100
    )

    filtered_players = players[
        players["total_duration"] >= min_player_duration
    ].copy()

    top_players = (
        filtered_players
        .sort_values("impact_per_60_sec", ascending=False)
        .head(15)
    )

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_players["player_name"], top_players["impact_per_60_sec"])
    ax.set_xlabel("Impact per 60")
    ax.set_title("Top Player Impact")
    ax.invert_yaxis()
    st.pyplot(fig)

    player_cols = [
        "player_name",
        "impact_per_60_sec",
        "total_duration",
        "total_stints",
        "total_net_points"
    ]

    st.dataframe(
        filtered_players[player_cols].sort_values("impact_per_60_sec", ascending=False),
        use_container_width=True,
        hide_index=True
    )


# ==============================
# Lineup Performance
# ==============================

with tab2:
    st.header("Lineup Performance")

    min_lineup_duration = st.slider(
        "Minimum lineup duration",
        min_value=0,
        max_value=int(lineups["total_duration"].max()),
        value=0,
        step=10
    )

    filtered_lineups = lineups[
        lineups["total_duration"] >= min_lineup_duration
    ].copy()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(
        filtered_lineups["total_duration"],
        filtered_lineups["net_per_60"],
        alpha=0.7
    )
    ax.axhline(0, linestyle="--", linewidth=1)
    ax.set_xlabel("Total Duration")
    ax.set_ylabel("Net per 60")
    ax.set_title("Lineup Usage vs Performance")
    st.pyplot(fig)

    st.dataframe(
        filtered_lineups.sort_values(
            ["net_per_60", "total_duration"],
            ascending=[False, False]
        ),
        use_container_width=True,
        hide_index=True
    )


# ==============================
# Pair Synergy
# ==============================

with tab3:
    st.header("Player Pair Synergy")

    min_pair_duration = st.slider(
        "Minimum pair duration",
        min_value=0,
        max_value=int(pairs["total_duration"].max()),
        value=0,
        step=100
    )

    filtered_pairs = pairs[
        pairs["total_duration"] >= min_pair_duration
    ].copy()

    if "pair_name" not in filtered_pairs.columns:
        filtered_pairs["pair_name"] = (
            filtered_pairs["player_1_name"].astype(str)
            + " + "
            + filtered_pairs["player_2_name"].astype(str)
        )

    top_pairs = (
        filtered_pairs
        .sort_values(["impact_per_60", "total_duration"], ascending=[False, False])
        .head(15)
    )

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_pairs["pair_name"], top_pairs["impact_per_60"])
    ax.set_xlabel("Impact per 60")
    ax.set_title("Top Player Pair Synergies")
    ax.invert_yaxis()
    st.pyplot(fig)

    st.dataframe(
        filtered_pairs.sort_values(
            ["impact_per_60", "total_duration"],
            ascending=[False, False]
        ),
        use_container_width=True,
        hide_index=True
    )


# ==============================
# Modeling
# ==============================

with tab4:
    st.header("Lineup Performance Modeling")

    st.markdown(
        """
        This section compares machine learning models trained to estimate lineup performance.
        Lower RMSE and MAE indicate better predictive accuracy, while higher R² indicates stronger explained variance.
        """
    )

    st.dataframe(
        model_results.sort_values("rmse"),
        use_container_width=True,
        hide_index=True
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(model_results["model"], model_results["rmse"])
    ax.set_ylabel("RMSE")
    ax.set_title("Model Error Comparison")
    plt.xticks(rotation=20)
    st.pyplot(fig)


# ==============================
# Feature Importance
# ==============================

with tab5:
    st.header("Model Feature Importance")

    if "importance" in feature_importance.columns:
        value_col = "importance"
    elif "coefficient" in feature_importance.columns:
        value_col = "coefficient"
    else:
        value_col = None

    st.dataframe(
        feature_importance,
        use_container_width=True,
        hide_index=True
    )

    if value_col:
        top_features = (
            feature_importance
            .sort_values(value_col, ascending=False)
            .head(15)
        )

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.barh(top_features["feature"], top_features[value_col])
        ax.set_xlabel(value_col.capitalize())
        ax.set_title("Top Modeling Features")
        ax.invert_yaxis()
        st.pyplot(fig)


st.divider()

st.markdown(
    """
    **Methodology note:** This dashboard is based on reconstructed multi-game lineup stints.
    Results should be interpreted as analytical decision-support signals rather than definitive coaching recommendations.
    """
)