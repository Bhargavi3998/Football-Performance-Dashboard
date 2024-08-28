document.addEventListener('DOMContentLoaded', function () {
    const filterForm = document.getElementById('filterForm');
    const goalSelect = document.getElementById('goal');
    const positionLabel = document.getElementById('positionLabel');
    const positionSelect = document.getElementById('position');
    const visualization = document.getElementById('visualization');

    // Show or hide the position dropdown based on selected goal
    goalSelect.addEventListener('change', function () {
        const selectedGoal = goalSelect.value;
        if (selectedGoal === 'Best CAV' || selectedGoal === 'Most Picks') {
            positionLabel.style.display = 'inline';
            positionSelect.style.display = 'inline';
        } else {
            positionLabel.style.display = 'none';
            positionSelect.style.display = 'none';
        }
    });

    filterForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const formData = new FormData(filterForm);

        fetch('/visualize', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                visualization.src = 'data:image/png;base64,' + data.plot_url;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while visualizing the data.');
        });
    });
});
