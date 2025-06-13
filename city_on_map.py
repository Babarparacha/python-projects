import plotly.express as px
import pandas as pd

# country=input("entry country to find: ")
# data={
#     'Country':[country],
#     'Values':[100]
# }
# fig=px.choropleth(
#     data,
#     locations='Country',
#     locationmode='country name',
#     color='Values',
#     color_continuous_scale='Inferno',
#     title=f"country map highlighted {country}"
# )
# fig.show()


country = input("Enter country to find: ")

data = pd.DataFrame({
    'Country': [country],
    'Values': [100]
})

fig = px.choropleth(
    data,
    locations='Country',
    locationmode='country names',
    color='Values',
    color_continuous_scale='Inferno',
    title=f"Country map highlighted: {country}"
)

fig.show()
