# Visualization 2 – Map of Critical Health Violations

### 1. What software did you use to create your data visualization?
I used **Tableau Public**, a free data visualization platform that allows interactive geographic mapping.

---

### 2. Who is your intended audience?
- **Toronto residents** who want to stay informed about food safety
- **Public health officials** monitoring patterns of violations
- **Local journalists** reporting on restaurant safety

---

### 3. What information or message are you trying to convey?
This map shows the **geographic distribution of “C - Crucial” violations** across restaurants in Toronto. It allows users to see hotspots, repeat offenders, and potential areas needing increased inspections.

---

### 4. What aspects of design did you consider? How did you apply them?
- Used **clean map background** to highlight violation locations
- Added **tooltips** to display `Establishment Name`, `Infraction Details`, and `Inspection Date`
- Plotted each violation separately using `Infraction Details` on the Detail shelf to prevent overlapping

---

### 5. How did you ensure your data visualization is reproducible?
- The dataset is from the [City of Toronto Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/)
- I filtered rows where `Severity == "C - Crucial"` and included this filtered dataset in `critical_violations.csv`
- The interactive map is public:  
  🔗 [View Live Tableau Map](https://public.tableau.com/authoring/critical_violations_jittered/Sheet1#2)

---

### 6. How did you ensure that your data visualization is accessible?
- Used a light background with clear, distinguishable markers
- Included meaningful tooltips and text descriptions
- Published the map on Tableau Public for open access
- Provided a CSV and a static image (`viz2_map.png`) as alternatives

---

### 7. Who are the individuals and communities impacted by your visualization?
- **Diners and residents** who rely on clean food premises
- **Food service workers and business owners**
- **City health inspectors and decision makers**

---

### 8. How did you choose which features to include or exclude?
- Focused only on rows with **"C - Crucial"** violations
- Excluded non-critical infractions to keep attention on serious health risks
- Removed rows missing latitude/longitude to ensure map functionality

---

### 9. What ‘underwater labour’ contributed to your final data visualization?
- Data cleaning and filtering in Python
- Understanding overlapping geolocation issues in Tableau
- Exploring design adjustments to improve map readability
- Learning Tableau's interface to properly format tooltips and detail levels
