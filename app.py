from flask import Flask, render_template, request
import plotly.express as px
import pandas as pd
import numpy as np
import json
import plotly

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/")
def index():
    # Load the coffee export data
    df = pd.read_csv("coffee_exports.csv")

    # Optional: print(df.head()) to see column names if unsure
    # Example assumes you have columns like 'Country', 'Year', 'Export'

    # Create a box plot using actual data
    fig = px.box(df, x="Country", y="Export_Tons", title="Coffee Exports by Country")



    # Match dark theme layout
    fig.update_layout(
        plot_bgcolor='#1a1c23',
        paper_bgcolor='#1a1c23',
        font_color='#ffffff',
        autosize=True,
        margin=dict(t=50, l=50, r=50, b=50),
        height=600
    )
    fig.update_xaxes(showgrid=False, color='#cccccc')
    fig.update_yaxes(showgrid=False, color='#cccccc')

    graph_html = fig.to_html(full_html=False)
    return render_template("index.html", graph=graph_html)


if __name__ == "__main__":
    app.run(debug=True)