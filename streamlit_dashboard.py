import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="Netwerk Operations Dashboard", layout="wide")

st.title("Netwerk Operations Dashboard")
st.subheader("Overzicht van clusters en externe partij")

# Simulatiegegevens
clusters = [
    {"naam": "Cluster A", "teams": 10},
    {"naam": "Cluster B", "teams": 10},
    {"naam": "Cluster C", "teams": 12},
    {"naam": "Cluster D", "teams": 11},
]

externe_partij = {"naam": "Externe Partner", "teams": 8}

# Status per cluster (placeholder random data)
statuskleuren = ["🟢", "🟠", "🟡", "🔴"]

cols = st.columns(5)
for i, cluster in enumerate(clusters):
    with cols[i]:
        st.metric(label=cluster["naam"], value=f"Teams: {cluster['teams']}")
        st.write(statuskleuren[i % len(statuskleuren)])

with cols[4]:
    st.metric(label=externe_partij["naam"], value=f"Teams: {externe_partij['teams']}")
    st.write(statuskleuren[1])

st.markdown("---")

# Kostenoverzicht (dummy data)
kosten_data = pd.DataFrame({
    'Maand': pd.date_range(start='2023-01-01', periods=6, freq='M'),
    'Cluster A': np.random.randint(80, 120, 6),
    'Cluster B': np.random.randint(80, 120, 6),
    'Cluster C': np.random.randint(80, 120, 6),
    'Cluster D': np.random.randint(80, 120, 6),
    'Extern': np.random.randint(80, 120, 6),
})

kosten_chart = alt.Chart(kosten_data.melt('Maand', var_name='Cluster', value_name='Kosten')) \
    .mark_line() \
    .encode(x='Maand:T', y='Kosten:Q', color='Cluster:N') \
    .properties(title='Kostenontwikkeling per cluster')

st.altair_chart(kosten_chart, use_container_width=True)

# Service KPI's (dummy data)
service_data = pd.DataFrame({
    'Cluster': [c['naam'] for c in clusters] + [externe_partij['naam']],
    'Klanttevredenheid': np.random.uniform(7.5, 9.5, len(clusters) + 1),
    'Gemiddelde responstijd': np.random.uniform(1, 5, len(clusters) + 1)
})

service_cols = st.columns(2)
with service_cols[0]:
    bar = alt.Chart(service_data).mark_bar().encode(
        x='Cluster:N', y='Klanttevredenheid:Q', color='Cluster:N'
    ).properties(title='Klanttevredenheid (NPS)')
    st.altair_chart(bar, use_container_width=True)

with service_cols[1]:
    line = alt.Chart(service_data).mark_bar().encode(
        x='Cluster:N', y='Gemiddelde responstijd:Q', color='Cluster:N'
    ).properties(title='Gem. Responstijd (dagen)')
    st.altair_chart(line, use_container_width=True)

st.markdown("---")

# Installaties per dag/week (dummy data)
installaties_data = pd.DataFrame({
    'Datum': pd.date_range(start='2023-01-01', periods=30),
    'Installaties': np.random.randint(50, 80, 30)
})

install_chart = alt.Chart(installaties_data).mark_area(color='skyblue') \
    .encode(x='Datum:T', y='Installaties:Q') \
    .properties(title='Dagelijkse installaties (totaal)')

st.altair_chart(install_chart, use_container_width=True)

st.markdown("---")

st.write("Selecteer een cluster voor detailinformatie:")
cluster_namen = [c['naam'] for c in clusters] + [externe_partij['naam']]
cluster_selectie = st.selectbox("Cluster", cluster_namen)

st.write(f"Details voor {cluster_selectie} (placeholder)")
