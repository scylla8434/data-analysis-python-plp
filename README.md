```markdown
# 📊 Pandas & Matplotlib Data Analysis Project

This project demonstrates how to load, explore, analyze, and visualize a time-series dataset using **pandas** and **matplotlib** (with optional **seaborn** styling). We generate a synthetic “monthly air passengers” dataset spanning **2000–2025**, then produce descriptive statistics, group summaries, and four distinct plots.

---


## 🛠️ Requirements

- Python 3.7+  
- Packages:
  ```bash
  pip install pandas numpy matplotlib seaborn
  ```
- VS Code (optional, for integrated debugging & interactive runs)

---

## ⚙️ Setup

1. **Clone or download** this repository.  
2. **Open** the folder in VS Code:
   ```bash
   code path/to/data-analysis-python-plp
   ```
3. **(Optional)** Create & activate a virtual environment:
   ```bash
   python3 -m venv venv
   # macOS/Linux
   source venv/bin/activate
   # Windows
   .\venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

---

## 🔄 Data Generation

On first run, `analysis.py` will detect that `data/flights.csv` is missing and automatically:
1. Generates monthly timestamps from January 2000 through December 2025.  
2. Creates synthetic passenger counts with:
   - A linear upward trend  
   - Seasonal (sinusoidal) variation  
   - Random noise  
3. Saves the result to `data/flights.csv`.

---

## ▶️ Running the Analysis

### As a Script

```bash
python analysis.py
```

You’ll see:
- Data-loading messages  
- `.head()`, `.info()`, missing-value checks  
- Descriptive statistics & group summaries  
- Four plots, one after another  
- Printed observations at the end

### In VS Code Debug / Interactive Mode

- **Debug**: Press **F5** (uses `.vscode/launch.json`)  
- **Interactive cells**: Add `# %%` in `analysis.py` to break it into runnable cells—click the gutter ▶️ to run inline.

---

## 📈 What You’ll Get

1. **Data loading & exploration**  
2. **Basic analysis**  
   - Descriptive stats: mean, median, std, etc.  
   - Group-by “year” summaries  
3. **Visualizations**  
   - **Line chart**: monthly passengers over time  
   - **Bar chart**: average monthly passengers per year  
   - **Histogram**: distribution of passenger counts  
   - **Scatter plot**: year vs. passengers  
4. **Findings** printed to console

---

## 📝 Customization

- To use your own CSV:
  1. Place it in `data/` or elsewhere.  
  2. Edit the `csv_path` variable at the top of `analysis.py`.  
  3. Ensure it has columns like `year`, `month`, and one numeric column.  
- Adjust plot styles or add new analyses as desired.

---

## 📚 References

- **pandas** documentation: https://pandas.pydata.org/  
- **matplotlib** documentation: https://matplotlib.org/  
- **seaborn** documentation: https://seaborn.pydata.org/

