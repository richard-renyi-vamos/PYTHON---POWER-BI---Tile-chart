import pandas as pd
import plotly.graph_objects as go

# Sample data
data = {
    'Category': ['Category A', 'Category B', 'Category C'],
    'Value': [250, 400, 300]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a tile chart using Plotly
fig = go.Figure(go.Indicator(
    mode = "number+gauge",
    value = df['Value'][0],
    title = {'text': df['Category'][0]},
    gauge = {
        'axis': {'range': [None, 500]},
        'bar': {'color': "green"},
        'steps' : [
            {'range': [0, 250], 'color': "lightgray"},
            {'range': [250, 400], 'color': "gray"}],
        'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 490}
    }))

fig.update_layout(title="Tile Chart Example", title_x=0.5)

# Display the chart
fig.show()
