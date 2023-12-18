// Function to fetch RAM data
function getRamAndUpdateChart(chartInstance) {
    fetch("/api/sysinfo/ram")
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            updateChartWithRamData(chartInstance, data);
        })
        .catch(error => {
            console.error('Error fetching RAM data:', error);
        });
}

// Function to update Chart.js pie chart with RAM data
function updateChartWithRamData(chartInstance, ramData) {
    const { availableRAM, usedRAM } = ramData;

    chartInstance.data.datasets[0].data = [usedRAM, availableRAM];
    chartInstance.update();
}

// Export the getRamAndUpdateChart function
window.getRamAndUpdateChart = getRamAndUpdateChart;