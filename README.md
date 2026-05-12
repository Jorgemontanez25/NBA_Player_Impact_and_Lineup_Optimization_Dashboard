# 🏀 NBA Player Impact & Matchup-Based Lineup Optimization Dashboard

An advanced NBA Sports Analytics project focused on reconstructing real lineup stints from NBA play-by-play data, evaluating player impact, modeling lineup performance, analyzing player synergies, and generating matchup-based lineup recommendations using Machine Learning.

This project combines:
- Basketball analytics
- Machine learning
- lineup reconstruction
- predictive modeling
- interactive dashboard development
- matchup intelligence concepts used in modern basketball operations

---

# 🚀 Project Overview

Modern basketball organizations rely heavily on lineup optimization, player synergy analysis, and matchup-based decision support.

This project simulates a prototype Basketball Operations Analytics Tool capable of:

✅ Reconstructing historical lineup stints from raw NBA play-by-play data  
✅ Measuring player impact during real game possessions  
✅ Evaluating lineup efficiency and reliability  
✅ Discovering high-performing player pair synergies  
✅ Training machine learning models to estimate lineup success  
✅ Generating matchup-based lineup recommendations  
✅ Visualizing optimal matchups in an interactive basketball court dashboard  

---

# 🧠 Main Features

## 🏀 Matchup-Based Lineup Recommender

The dashboard allows users to:

- Select a team
- Select an opponent
- Choose the opponent starting lineup
- Receive recommended lineups based on:
  - historical lineup performance
  - player impact
  - pair synergy
  - matchup-adjusted scoring

### Interactive Basketball Court View

The application dynamically displays:
- both teams
- starting lineups
- player positioning
- matchup visualization

This creates a much more coach-friendly and basketball-oriented experience compared to traditional tables.

---

## 📈 Player Impact Analysis

The project reconstructs lineup stints and estimates:

- total net scoring impact
- impact per 60 possessions
- lineup participation reliability
- total stint exposure

This allows the dashboard to rank players based on observed on-court impact.

---

## 🤝 Player Pair Synergy

The system evaluates:
- high-performing player duos
- net lineup contribution
- pair reliability
- historical duration

Examples:
- Kobe Bryant + Shaquille O'Neal
- Steve Nash + Amar'e Stoudemire
- Tim Duncan + Tony Parker

---

## 📊 Lineup Performance Modeling

Multiple machine learning models were trained to estimate lineup success.

Models evaluated:
- Linear Regression
- Ridge Regression
- Random Forest Regressor

Metrics analyzed:
- RMSE
- MAE
- R²

---

## 🔬 Feature Engineering

The project generates advanced basketball features including:

- lineup net rating
- player impact aggregation
- pair synergy influence
- lineup duration reliability
- matchup-adjusted scoring
- lineup consistency indicators

---

# 🧱 Data Pipeline

The project was built using a complete multi-notebook analytics workflow.

## Notebook Workflow

| Notebook | Description |
|---|---|
| notebook_01 | Database exploration |
| notebook_02 | Single-game play-by-play validation |
| notebook_03 | Multi-game play-by-play reconstruction |
| notebook_04 | Lineup stint reconstruction |
| notebook_05 | Player impact analysis |
| notebook_06 | Machine learning lineup modeling |
| notebook_07 | Team matchup recommendation engine |
| notebook_08 | Dashboard-ready data generation |
| notebook_09 | Matchup recommendation preparation |

---

# 📊 Dashboard Features

The Streamlit dashboard includes:

## 🏀 Matchup Recommender
- team selection
- opponent selection
- opponent starting lineup selection
- lineup recommendation engine
- basketball court visualization

## 📈 Player Impact
- top player impact rankings
- impact per 60 analysis
- reliability filtering

## 📋 Lineup Performance
- lineup net rating analysis
- lineup reliability visualization
- performance scatterplots

## 🤝 Pair Synergy
- top player duo rankings
- pair impact analysis
- duo reliability metrics

## 🤖 Modeling
- machine learning model comparison
- RMSE comparison
- predictive performance evaluation

## 🔍 Feature Importance
- model interpretability
- feature contribution analysis

---

# ⚠️ Current Prototype Limitations

This project represents a prototype analytics system and should be interpreted as a decision-support tool rather than definitive coaching intelligence.

Current limitations include:

- recommendations are based on historically observed lineups only
- no season-specific filtering
- no injury/fatigue context
- no salary/cap considerations
- no real-time tracking data
- lineup recommendations are constrained by processed sample size
- no possession-level spatial tracking integration

Example:
The system may not always recommend historically iconic duos (e.g., Kobe Bryant + Shaq) if the reconstructed sample does not sufficiently capture those specific lineup combinations.

---

# 🔮 Future Improvements

Potential future upgrades:

✅ Full season filtering  
✅ Playoff-only analysis  
✅ Dynamic lineup generation  
✅ Position-aware optimization  
✅ Deep Learning lineup evaluation  
✅ Possession-level tracking integration  
✅ Player clustering/archetypes  
✅ Real-time game simulation  
✅ Reinforcement learning lineup optimization  
✅ Shot quality modeling  
✅ Defensive matchup intelligence  

---

# 🛠️ Technologies Used

## Programming & Analytics
- Python
- Pandas
- NumPy
- SQLite

## Machine Learning
- Scikit-learn
- Random Forest
- Ridge Regression

## Visualization
- Matplotlib
- Streamlit

## Sports Analytics Concepts
- lineup reconstruction
- net rating
- player impact modeling
- matchup analysis
- synergy analysis

---

# 📂 Project Structure

```text
NBA_Player_Impact_and_Lineup_Optimization_Dashboard/
│
├── app.py
├── README.md
├── requirements.txt
│
├── notebooks/
│   ├── notebook_01.ipynb
│   ├── notebook_02.ipynb
│   ├── notebook_03.ipynb
│   ├── notebook_04.ipynb
│   ├── notebook_05.ipynb
│   ├── notebook_06.ipynb
│   ├── notebook_07.ipynb
│   ├── notebook_08.ipynb
│   └── notebook_09.ipynb
│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
│
└── figures/
```

---

# ▶️ Run the Dashboard

## Install dependencies

```bash
pip install -r requirements.txt
```

## Launch Streamlit app

```bash
python -m streamlit run app.py
```

---

# 🏀 Why This Project Matters

This project demonstrates practical applications of:

- Sports Analytics
- Machine Learning
- Basketball Operations
- Predictive Modeling
- Data Engineering
- Interactive Visualization
- Decision-Support Systems

The workflow mirrors many concepts used by:
- NBA analytics departments
- player development groups
- scouting teams
- performance strategy units

---

# 👨‍💻 Author

Jorge Montañez

Mechanical Engineer | AI & Machine Learning | Sports Analytics

Focused on:
- Sports Analytics
- Machine Learning
- Predictive Modeling
- Basketball Operations Intelligence

---

# ⭐ Final Note

This project evolved from a simple lineup reconstruction experiment into a much more advanced matchup-based basketball analytics prototype.

The final system demonstrates how play-by-play data, machine learning, and lineup intelligence can be combined into an interactive basketball decision-support platform.