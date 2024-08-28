from flask import Flask, render_template, request, jsonify
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import matplotlib

# Use a non-GUI backend suitable for server environments
matplotlib.use('Agg')

# Load the data
book_combined = pd.read_excel('data/Book_combined.xlsx')

app = Flask(__name__)

# Map dropdown selections to actual DataFrame columns
goal_mapping = {
    "Max Salary": "Salary",
    "Best CAV": "CAV",
    "Most Picks": "Pick"
}

def get_aggregated_top_schools(df, year, goal_column, position=None):
    # Filter data by year
    filtered_df = df[df['Year'] == year]
    
    # Further filter by position if provided
    if position:
        filtered_df = filtered_df[filtered_df['Pos'] == position]

    # Group by School and aggregate
    aggregated_df = filtered_df.groupby('School').agg({
        'Salary': 'mean',
        'CAV': 'mean',
        'Pick': 'sum'
    }).reset_index()

    # Get top 3 schools based on the selected goal
    top_schools = aggregated_df.nlargest(3, goal_column)

    # If there are fewer than 3 schools, pad with placeholders
    while top_schools.shape[0] < 3:
        top_schools = top_schools.append({'School': 'N/A', 'Salary': 0, 'CAV': 0, 'Pick': 0}, ignore_index=True)

    return top_schools

@app.route('/')
def index():
    # Unique years for dropdown
    years = book_combined['Year'].unique().tolist()
    positions = ['QB', 'WR', 'RB', 'DB', 'OL', 'LB']  # Example positions
    return render_template('index.html', years=years, positions=positions)

@app.route('/visualize', methods=['POST'])
def visualize():
    try:
        goal = request.form.get('goal')
        year = request.form.get('year')
        position = request.form.get('position')  # Only applicable for Best CAV and Most Picks
        print(f"Received Goal: {goal}, Year: {year}, Position: {position}")

        # Map the selected goal to the actual column name
        if goal not in goal_mapping:
            return jsonify({'error': 'Invalid goal selection.'}), 400

        actual_goal_column = goal_mapping[goal]
        print(f"Using column: {actual_goal_column}")

        # Convert relevant columns to numeric, coercing errors to NaN
        book_combined['Salary'] = pd.to_numeric(book_combined['Salary'], errors='coerce')
        book_combined['CAV'] = pd.to_numeric(book_combined['CAV'], errors='coerce')
        book_combined['Pick'] = pd.to_numeric(book_combined['Pick'], errors='coerce')
        print("Converted columns to numeric")

        # Get the top 3 schools based on grouping and aggregation logic
        top_schools = get_aggregated_top_schools(book_combined, float(year), actual_goal_column, position)
        print(f"Top Schools Data:\n{top_schools}")

        if goal == "Max Salary":
            # Circle plot setup
            plt.figure(figsize=(10, 6))

            # Dynamically determine x positions based on the number of valid schools
            valid_schools = top_schools[top_schools['School'] != 'N/A']
            x_positions = list(range(1, len(valid_schools) + 1))  # Positions only for valid data

            # Plot translucent circles (only for valid rows)
            for i, (index, row) in enumerate(valid_schools.iterrows()):
                circle_size = row[actual_goal_column] / 1e6 * 1000  # Dynamic circle size based on the goal
                plt.scatter(x_positions[i], 1, s=circle_size, alpha=0.3, color='blue')
                plt.text(x_positions[i], 1, row['School'], ha='center', va='center', fontsize=12, color='black', fontweight='bold')
                plt.text(x_positions[i], 0.6, f"Salary: ${row['Salary']/1e6:.1f}M", ha='center', fontsize=10, color='black')

            plt.xlim(0, len(valid_schools) + 1)  # Set x-axis limits to space the circles
            plt.ylim(0, 2)  # Set y-axis limits to avoid text overlap
            plt.axis('off')  # Turn off the axis
            plt.title(f'Top 3 Schools by {goal} in {year}', fontsize=16)

        elif goal == "Best CAV" and position:
            plt.figure(figsize=(8, 6))
            plt.bar(top_schools['School'], top_schools['CAV'], color='green')
            plt.xlabel('School')
            plt.ylabel('CAV')
            plt.title(f'Best CAV for {position} in {year}')

        elif goal == "Most Picks" and position:
            plt.figure(figsize=(8, 6))
            plt.bar(top_schools['School'], top_schools['Pick'], color='orange')
            plt.xlabel('School')
            plt.ylabel('Picks')
            plt.title(f'Most Picks for {position} in {year}')

        # Save the plot to a BytesIO object
        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight')
        plt.close()  # Clear the figure
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        print(f"Generated plot URL: {plot_url[:50]}...")  # Print first 50 characters for verification

        return jsonify({'plot_url': plot_url})

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
