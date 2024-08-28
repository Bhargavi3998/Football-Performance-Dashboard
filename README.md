
# 🏈 **Football Performance Insight Tool**: Navigate Your Path to Stardom 🌟

## Overview

Welcome to the Football Performance Insight Tool, an advanced data-driven platform designed to empower aspiring football athletes and their advisors with the knowledge needed to make informed decisions about their future. This isn't just a simple dashboard—it's your gateway to understanding the hidden patterns and opportunities within the world of college football.

### Why It Matters

Choosing the right school is more than just about education—it's about setting the stage for a successful football career. Whether you're aiming to earn the highest salary, maximize your career's overall impact, or increase your chances of being drafted, this tool equips you with insights drawn from historical data to help you make the best possible decision.

### What It Offers

- **💼 Salary Analysis**: Discover which schools have historically produced the highest-earning athletes.
- **🏆 Career Approximate Value (CAV)**: Evaluate the long-term impact of a school's training on player success.
- **🎯 Draft Picks**: See which institutions have consistently seen their players picked by top teams, boosting your chances of making it to the pros.

### Who Can Benefit?

- **Athletes**: Identify the institutions that can best serve your career ambitions.
- **Parents and Advisors**: Guide your athlete with data-driven insights that align with their goals.
- **Recruiters**: Use this tool to understand the competition and identify where top talent is being cultivated.

## Features

- **Intelligent Visualizations**: The platform delivers dynamic circle plots and bar charts that elegantly highlight the top-performing schools based on user-selected criteria.
- **User-Centric Interface**: Tailored for ease of use, the tool ensures that even those without technical expertise can effortlessly explore complex datasets.
- **Multi-Criteria Analysis**: Whether you're focused on salary, career value, or draft picks, this tool provides a comprehensive view that accounts for all these critical factors.
- **Responsive Design**: The platform is designed to work seamlessly across all devices, ensuring you can access insights on the go.

## Technologies Behind the Magic

- **Python**: The backbone of our data processing and logic.
- **Flask**: Powers the robust and responsive web interface.
- **Pandas**: Handles the heavy lifting of data manipulation.
- **Matplotlib**: Delivers visually striking and informative graphics.
- **HTML/CSS/JavaScript**: Combined with Bootstrap, these technologies create a visually appealing and intuitive user interface.

## Installation and Setup

### Prerequisites

- **Python 3.x**
- **pip** (Python package installer)

### Getting Started

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/football-performance-insight-tool.git
   cd football-performance-insight-tool
   ```

2. **Create and Activate a Virtual Environment (Optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare Your Dataset**

   Place your dataset (`Book_combined.xlsx`) in the `data/` directory.

5. **Launch the Application**

   ```bash
   python app.py
   ```

6. **Access the Insight Tool**

   Open your web browser and navigate to `http://127.0.0.1:5000/` to explore the insights.

## Project Structure

```plaintext
├── app.py                  # Main application logic and routes
├── data/
│   └── Book_combined.xlsx   # The dataset used for generating insights
├── static/
│   ├── background.jpeg      # Custom background image for the tool
│   ├── styles.css           # Custom styling for the user interface
│   └── scripts.js           # JavaScript for handling frontend interactions
├── templates/
│   └── index.html           # HTML template for the main interface
├── requirements.txt         # List of dependencies
└── README.md                # You're reading it now!
```

## Key Components

- **Dynamic Circle Plots**: Visualize the top schools by salary with circle sizes proportional to their impact.
- **Bar Charts**: Quickly compare the best-performing schools based on CAV and draft picks.
- **Background Image**: Aesthetic design with a custom background image to enhance the user experience.
- **Responsive Layout**: Ensures the tool is accessible on any device, from desktops to mobile phones.

## Using the Tool

1. **Select Your Goal**: Choose from Max Salary, Best CAV, or Most Picks to determine your analysis focus.
2. **Pick a Year**: Specify the year of interest to filter the data.
3. **Choose a Position**: (If applicable) Select the player position to tailor the results further.
4. **Generate Insights**: Click "Visualize" and watch the data transform into actionable insights.

## Customization Options

- **Background and Styling**: Want to match the tool's aesthetics to your brand? Replace `background.jpeg` in the `static/` directory and tweak the `styles.css` file to make it yours.
- **Enhance Visualizations**: Feel free to dive into `app.py` to customize the visualizations and even add new ones based on your specific needs.

## Contributing

We welcome contributions! If you have ideas for enhancements or spot any issues, feel free to submit a pull request or open an issue on GitHub.

## License

This project is licensed under the MIT License. For more information, see the [LICENSE](LICENSE) file.
