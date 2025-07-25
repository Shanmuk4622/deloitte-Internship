"""
Deloitte Australia Technology Consulting Simulation
Author: BONALA SHANMUKESH
Date: 2025-07-17

This solution simulates a technology consultant's approach to analyze
a client's IT systems, assess department-specific pain points, score
technological fit, and generate recommendations with justifications.
"""

import pandas as pd
import random
import matplotlib.pyplot as plt

# -------------------------------------------
# Step 1: Load Simulated Client Department Data
# -------------------------------------------

departments = ['HR', 'Finance', 'IT', 'Marketing', 'Operations', 'Logistics', 'Procurement']
current_tools = ['Excel', 'SAP', 'Legacy System', 'Mailchimp', 'Manual Process', 'Zoho', 'No Tool']
pain_points = [
    'Manual data entry',
    'High cost and licensing issues',
    'Security vulnerabilities',
    'Low customer engagement',
    'No process standardization',
    'Inefficient vendor communication',
    'Lack of analytics & reporting'
]

data = {
    "Department": departments,
    "Current_Tool": random.choices(current_tools, k=len(departments)),
    "Pain_Point": random.choices(pain_points, k=len(departments))
}

df = pd.DataFrame(data)

# -------------------------------------------
# Step 2: Define Technology Options & Scores
# -------------------------------------------

tech_options = {
    "Odoo ERP": {"Cost": 8, "EaseOfUse": 7, "Integration": 9, "Scalability": 8},
    "Oracle NetSuite": {"Cost": 6, "EaseOfUse": 7, "Integration": 9, "Scalability": 9},
    "Zoho One": {"Cost": 9, "EaseOfUse": 8, "Integration": 8, "Scalability": 7},
    "Salesforce": {"Cost": 5, "EaseOfUse": 6, "Integration": 10, "Scalability": 9},
    "Microsoft Power Platform": {"Cost": 7, "EaseOfUse": 9, "Integration": 8, "Scalability": 8},
    "Custom Cloud Solution": {"Cost": 4, "EaseOfUse": 6, "Integration": 9, "Scalability": 10}
}

# Normalize scores
def compute_score(metrics):
    return round(sum(metrics.values()) / len(metrics), 2)

recommendations = {}
for tool, scores in tech_options.items():
    recommendations[tool] = compute_score(scores)

# -------------------------------------------
# Step 3: Assign Best Recommendation
# -------------------------------------------

def recommend_best_tool(current_tool, pain_point):
    if 'manual' in pain_point.lower() or 'no' in current_tool.lower():
        return "Odoo ERP"
    elif 'engagement' in pain_point.lower():
        return "Salesforce"
    elif 'security' in pain_point.lower():
        return "Microsoft Power Platform"
    elif 'vendor' in pain_point.lower():
        return "Zoho One"
    elif 'legacy' in current_tool.lower():
        return "Oracle NetSuite"
    else:
        return max(recommendations, key=recommendations.get)

df["Recommended_Tool"] = df.apply(
    lambda row: recommend_best_tool(row["Current_Tool"], row["Pain_Point"]),
    axis=1
)

df["Tool_Score"] = df["Recommended_Tool"].map(recommendations)

# -------------------------------------------
# Step 4: Generate Report
# -------------------------------------------

def generate_consulting_report(df):
    print("\n📘 Deloitte Technology Consulting Report\n" + "-" * 60)
    for index, row in df.iterrows():
        print(f"\nDepartment: {row['Department']}")
        print(f"Current Tool: {row['Current_Tool']}")
        print(f"Pain Point: {row['Pain_Point']}")
        print(f"✅ Recommendation: {row['Recommended_Tool']} (Score: {row['Tool_Score']}/10)")
    print("\nReport generation completed.\n")

generate_consulting_report(df)

# -------------------------------------------
# Step 5: Save to CSV/Excel
# -------------------------------------------

df.to_csv("Deloitte_Tech_Recommendations.csv", index=False)
print("📁 Report saved as Deloitte_Tech_Recommendations.csv")

# -------------------------------------------
# Step 6: Visualization (Optional)
# -------------------------------------------

def plot_recommendation_distribution(df):
    plt.figure(figsize=(10, 6))
    df['Recommended_Tool'].value_counts().plot(kind='bar', color='steelblue')
    plt.title("Tool Recommendation Distribution Across Departments")
    plt.xlabel("Technology Tool")
    plt.ylabel("Number of Departments")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig("recommendation_distribution.png")
    plt.show()
    print("📊 Bar chart saved as recommendation_distribution.png")

plot_recommendation_distribution(df)
