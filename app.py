import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Set page config
st.set_page_config(layout="wide", page_title="Moon Mission Visualizer")

# Create a container for centering content
container = st.container()

# Add custom CSS to center the text
container.markdown(
    """
    <style>
    .centered-text {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
        font-size: 36px;
        font-weight: bold;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the centered text
container.markdown('<div class="centered-text">Moon Mission Trajectory</div>', unsafe_allow_html=True)

# Create moon surface
phi = np.linspace(0, 2*np.pi, 100)
theta = np.linspace(0, np.pi, 100)
phi, theta = np.meshgrid(phi, theta)

r = 1
x = r * np.sin(theta) * np.cos(phi)
y = r * np.sin(theta) * np.sin(phi)
z = r * np.cos(theta)

# Create rocket trajectory
t = np.linspace(0, 1, 100)
rocket_x = 1.5 * np.cos(4*np.pi*t)
rocket_y = 1.5 * np.sin(4*np.pi*t)
rocket_z = 3 * t - 1.5

# Create the 3D plot
fig = go.Figure()

# Add moon surface
fig.add_trace(go.Surface(x=x, y=y, z=z, colorscale='Greys', showscale=False))

# Add rocket trajectory
fig.add_trace(go.Scatter3d(x=rocket_x, y=rocket_y, z=rocket_z,
                           mode='lines',
                           line=dict(color='red', width=4),
                           name='Rocket Trajectory'))

# Update layout for a space-like theme
fig.update_layout(
    scene = dict(
        xaxis = dict(visible=False),
        yaxis = dict(visible=False),
        zaxis = dict(visible=False),
        aspectmode='data'
    ),
    width=800,
    height=800,
    margin=dict(r=0, l=0, b=0, t=0),
    scene_camera=dict(eye=dict(x=1.5, y=1.5, z=1.5)),
    paper_bgcolor='rgba(0,0,0,0.9)',
    plot_bgcolor='rgba(0,0,0,0.9)',
)

# Add a faint glow to the moon
fig.add_trace(go.Surface(x=1.01*x, y=1.01*y, z=1.01*z, 
                         colorscale=[[0, 'rgba(255,255,255,0.1)'], [1, 'rgba(255,255,255,0.3)']],
                         showscale=False, opacity=0.3))

# Display the 3D plot
st.plotly_chart(fig, use_container_width=True)

# Add explanation
st.markdown("""
# Flyby Mission

The rocket's path starts from below the Moon's south pole, spirals around it, and ends above the north pole,
representing a complex orbital maneuver.
""")
