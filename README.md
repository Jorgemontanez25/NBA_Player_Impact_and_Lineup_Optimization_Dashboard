# 🏀 NBA Player Impact & Lineup Optimization Dashboard

An end-to-end basketball analytics project focused on **lineup reconstruction, player impact modeling, matchup optimization, and decision-support analytics** using NBA play-by-play data.

This project combines:
- advanced data engineering
- lineup reconstruction logic
- machine learning modeling
- interactive sports analytics visualization
- matchup-based lineup recommendation systems

Built to simulate the type of analytical workflows used in modern NBA front offices and performance departments.

---

# 🚀 Project Overview

Traditional box score statistics often fail to capture:
- lineup chemistry
- substitution impact
- contextual on-court performance
- matchup-specific optimization

This project reconstructs multi-game NBA lineup stints directly from raw play-by-play events to evaluate:

✅ Player impact  
✅ Lineup efficiency  
✅ Pair synergy  
✅ Matchup-adjusted recommendations  
✅ Predictive lineup modeling  

The final deliverable is an interactive **Streamlit dashboard** that allows users to:
- analyze player impact
- evaluate lineup performance
- explore player pair synergy
- compare machine learning models
- generate matchup-based lineup recommendations against opponents

---

# 🧠 Key Features

## 🏀 Multi-Game Lineup Reconstruction
- Rebuilt on-court lineups from raw NBA play-by-play logs
- Tracked substitutions and stint transitions
- Validated lineup continuity across games

---

## 📊 Player Impact Modeling
Players are evaluated using:
- net point differential
- possession-independent impact metrics
- time-normalized impact per 60 seconds
- stint reliability filtering

---

## 🤝 Pair Synergy Analysis
Identifies high-performing player combinations based on:
- shared stint performance
- net scoring differential
- reliability thresholds
- lineup context

---

## 📈 Machine Learning Lineup Modeling
Developed predictive models to estimate lineup performance using:
- lineup-level features
- player-level aggregated impact features
- stint duration metrics
- synergy indicators

Models evaluated:
- Linear Regression
- Ridge Regression
- Random Forest Regressor

---

## 🧩 Matchup-Based Recommendation Engine
The dashboard simulates a coaching workflow:

### User selects:
- their team
- opponent team
- opponent starting five

### The engine recommends:
- optimized historical lineups
- matchup-adjusted scoring recommendations
- high-reliability combinations

---

## 🏟️ Interactive Basketball Court Visualization
Custom court visualization dynamically displays:
- recommended lineup
- opponent lineup
- team matchup structure

Designed to mimic professional sports analytics interfaces.

---

# 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Data Processing | Pandas, NumPy |
| Database | SQLite |
| Visualization | Matplotlib, Streamlit |
| Machine Learning | Scikit-learn |
| App Framework | Streamlit |
| Version Control | Git + GitHub |

---

# 📂 Project Structure

```text
NBA_Player_Impact_and_Lineup_Optimization_Dashboard/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── notebook_01_data_loading.ipynb
│   ├── notebook_02_event_validation.ipynb
│   ├── notebook_03_multi_game_validation.ipynb
│   ├── notebook_04_stint_reconstruction.ipynb
│   ├── notebook_05_lineup_analytics.ipynb
│   ├── notebook_06_modeling.ipynb
│   ├── notebook_07_pair_synergy.ipynb
│   ├── notebook_08_dashboard_tables.ipynb
│   └── notebook_09_matchup_recommender.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 📊 Dashboard Modules

## 🏀 Matchup Recommender
- Select teams
- Choose opponent starters
- Generate recommended lineups
- Visualize matchup on a basketball court

---

## 📈 Player Impact
- Top impact players
- Reliability filtering
- Time-normalized metrics

---

## 📋 Lineup Performance
- Lineup net rating analysis
- Duration vs efficiency
- Historical lineup evaluation

---

## 🤝 Pair Synergy
- Best player combinations
- Shared impact metrics
- Reliability-adjusted pair rankings

---

## 🧠 Modeling
- Model comparison
- RMSE / MAE / R² evaluation
- Predictive performance benchmarking

---

## 🔍 Feature Importance
- Most influential lineup features
- Player impact contribution analysis
- Model interpretability

---

# ⚙️ How to Run the Project

## 1️⃣ Clone the repository

```bash
git clone https://github.com/Jorgemontanez25/NBA_Player_Impact_and_Lineup_Optimization_Dashboard.git
```

---

## 2️⃣ Navigate into the project

```bash
cd NBA_Player_Impact_and_Lineup_Optimization_Dashboard
```

---

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run the Streamlit dashboard

```bash
python -m streamlit run app.py
```

---

# 📌 Methodology Notes

- Lineups were reconstructed from play-by-play substitution events.
- Recommendations are analytical decision-support signals, not deterministic coaching instructions.
- Only regular-season style game IDs were used to reduce noise from preseason data.
- Metrics are reliability-filtered to avoid misleading low-sample conclusions.

---

# 📈 Future Improvements

Potential future expansions include:

- season-level filtering
- possession-based metrics
- deep learning lineup embeddings
- player tracking integration
- Bayesian lineup evaluation
- Monte Carlo matchup simulation
- reinforcement learning lineup optimization
- live in-game recommendation systems

---

# 🎯 Why This Project Matters

Modern sports organizations increasingly rely on:
- predictive analytics
- contextual lineup evaluation
- matchup optimization
- decision-support systems

This project demonstrates the ability to:
- work with messy sequential event data
- engineer complex sports analytics pipelines
- develop interpretable machine learning systems
- build recruiter-ready interactive analytics applications

---

# 👨‍💻 Author

## Jorge Montañez
Mechatronics Engineer | AI & Machine Learning Graduate Student | Sports Analytics Enthusiast

Focused on:
- Sports Analytics
- Machine Learning
- Data Science
- Predictive Modeling
- Decision-Support Systems

---

# ⭐ If you found this project interesting

Feel free to:
- star the repository
- fork the project
- connect on LinkedIn
- discuss sports analytics ideas

---

# 🏀 Final Note

This project was designed not only to analyze basketball data, but to simulate how modern teams can transform raw event streams into actionable competitive intelligence.