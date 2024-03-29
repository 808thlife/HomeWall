document.addEventListener("DOMContentLoaded", ()=>{
    function updateTable() {
        fetch('/dhcp/table')  // URL of the Django view to fetch updated data
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                console.log(data)
                // Clear existing table content
                document.getElementById('device-table-body').innerHTML = '';
    
                // Iterate over received data and append rows to the table
                data.forEach(item => {
                    var row = '<tr>' +
                              '<th scope="row">' + item.ip + '</th>' +
                              '<td>' + item.mac + '</td>' +
                              '<td>' + item.hostname + '</td>' +
                              '</tr>';
                    document.getElementById('device-table-body').innerHTML += row;
                });
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    }
    
    // Call updateTable function every 5 seconds
    setInterval(updateTable, 5000);  // Adjust interval as needed
    
})