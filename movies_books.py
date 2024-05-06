import cgi
import pandas as pd

df = pd.read_csv('entertainment.csv')

"""
form = cgi.FieldStorage()
selected_location = form.getvalue('selectedLocation')

def filter_data(city, country):
    filtered_df = df[(df['City'] == city) & (df['Country'] == country)]
    return filtered_df.to_html()

result_html = filter_data(selected_location)

print(result_html)
"""

# Function to generate HTML content for movies and books based on location
def generate_html_for_location(location):
    filtered_df = df[(df['City'] == location) | (df['Country'] == location)]
    movies = filtered_df[filtered_df['Entertainment Type'] == 'Movie']['Name'].tolist()
    books = filtered_df[filtered_df['Entertainment Type'] == 'Book']['Name'].tolist()

    html_content = f'<h2>{location}</h2>'
    if movies:
        html_content += '<h3>Movies:</h3><ul>'
        for movie in movies:
            html_content += f'<li>{movie}</li>'
        html_content += '</ul>'
    if books:
        html_content += '<h3>Books:</h3><ul>'
        for book in books:
            html_content += f'<li>{book}</li>'
        html_content += '</ul>'
    return html_content

'''
# Example usage:
selected_location = 'Accra'  # Example selected location
generated_html = generate_html_for_location(selected_location)
print(generated_html)  # This will be embedded into the HTML template
'''