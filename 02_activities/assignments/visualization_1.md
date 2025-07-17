# Visualization 1 – Bar Chart of Top 10 Most Common Violations

### 1. What software did you use to create your data visualization?
I used **Python**, specifically the `pandas`, `seaborn`, and `matplotlib` libraries, to process and visualize the data.

---

### 2. Who is your intended audience?
The audience includes:
- **Toronto residents** who eat out frequently and care about food safety
- **Restaurant owners and staff** who want to understand common health issues
- **Toronto Public Health** professionals who oversee restaurant inspections

---

### 3. What information or message are you trying to convey with your visualization?
The bar chart shows the **10 most frequently observed food safety violations** in Toronto restaurants. It aims to highlight the most common risks so the public can be informed, and enforcement or training can be better targeted.

---

### 4. What aspects of design did you consider? How did you apply them?
- Used a **horizontal bar chart** for better readability of long violation descriptions
- Applied a **colourblind-friendly palette** (`colorblind`) for accessibility
- Used **clear axis labels and a descriptive title**
- Sorted values in **descending order** to focus attention on the most common violations

---

### 5. How did you ensure your data visualizations are reproducible?
All code used to process and visualize the data is included in the file `code_appendix.py`.  
The dataset is publicly available and linked in `dataset_link.txt`.  
Anyone with Python and the required libraries can reproduce this visualization.

---

### 6. How did you ensure that your data visualization is accessible?
- Used high-contrast colours and large fonts
- Labels are clear and avoid jargon
- Colour palette chosen is readable for colourblind viewers
- Visualization is saved as a **high-resolution PNG** (`viz1_bar_chart.png`) and can include alt text in documentation

---

### 7. Who are the individuals and communities impacted by your visualization?
- **Restaurant patrons**, especially those with health risks (e.g., allergies, weakened immune systems)
- **Small business owners** who can learn from frequent violations
- **Public health officials** who can use this insight for inspection focus

---

### 8. How did you choose which features to include or exclude?
- Focused on the `Infraction Details` column to capture the type of violation
- Filtered out any rows where `Infraction Details` was missing
- Grouped and counted the most common violations, selecting only the **top 10** for clarity

---

### 9. What ‘underwater labour’ contributed to your final data visualization?
- Cleaning and filtering the raw data
- Identifying and correcting the correct column name (`Infraction Details`)
- Choosing the right plot type, colour scheme, and layout
- Testing file saving and formatting for proper resolution and accessibility
