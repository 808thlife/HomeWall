document.addEventListener("DOMContentLoaded", async () => {

    function shiftCharacters(arr, newVariable) {
        let lastIndex = arr.length;
      
        for (let i = 0; i < lastIndex; i++) {
          arr[i] = arr[i + 1];
        }
      
        arr[lastIndex - 1] = newVariable;
        
      
        return arr;
      }
      

    async function getRam() {
        const response = await fetch("/api/sysinfo/ram", {
          method: "GET",
        });
        const data = await response.json();
        return {
          freeRam: data["availableRAM"],
          usedRam: data["usedRAM"],
        };
      }
        //initializing initual values of RAM GRAPH so it won't be empty
        async function InitalRAM(){
        const ramData = await getRam();
        const freeRam = ramData.freeRam;
        const usedRam = ramData.usedRam;
        ramChart.data.datasets[0].data[0] = freeRam;
        ramChart.data.datasets[0].data[1] = usedRam;
        ramChart.update();
        }
        
        InitalRAM();
        
    let ramChart = new Chart(document.querySelector('#pieChart'), {
      type: 'pie',
      data: {
        labels: [
          'Free RAM',
          'Used RAM',
        ],
        datasets: [{
          label: 'RAM Usage in GB',
          data: [50,100],
          backgroundColor: [
            'rgb(50, 255, 100)',
            'rgb(100, 100, 255)',
          ],
          hoverOffset: 4
        }]
      }
    });

    

    setInterval(() => {
        getRam().then(ramData => {
          const freeRam = ramData.freeRam;
          const usedRam = ramData.usedRam;
          ramChart.data.datasets[0].data[0] = freeRam;
          ramChart.data.datasets[0].data[1] = usedRam;
          ramChart.update();
        });
      }, 2000);
      


      // CPU usage
      async function getCpu() {
        const response = await fetch("/api/sysinfo/cpu", {
          method: "GET",
        });
        const data = await response.json();
        return {
          cpuPercentage: data["usageCPU"],
        };
      }

      

      //Cpu area graph
     
        const cpuDataChart = [0,0,0,0,0,0,0]
        let cpuChart = new Chart(document.querySelector('#lineChart'), {
          type: 'line',
          data: {
            labels: ['15s', '10s','8s', '6s', '4s', '2s', 'Now'],
            datasets: [{
              label: 'Line Chart',
              data: cpuDataChart,
              fill: true,
              fillColor : "#4d70a8",
              borderColor: 'rgb(75, 192, 192)',
              tension: 0.1
            }]
          },
          options: {
            scales: {
              y: {
                beginAtZero: true,
                min: 0,
                max: 100,
                stepSize: 20,
                ticks: {
                  stepSize: 20,
                  callback: function (value) {
                    return value; // This ensures only specified values (0, 20, 40, 60, 80, 100) are shown on the y-axis
                  }
                }
              }
            }
          }
        });
        
        cpuChart.canvas.addEventListener('click', () => {
          localStorage.setItem('graphState', JSON.stringify({
            zoomLevel: cpuChart.chart.getZoom(),
            selectedPoints: cpuChart.getElementsAtEventForMode(
              cpuChart.chart.panMode,
              'nearest',
              event,
              false
            )
          }));
        });

      setInterval(() => {
        getCpu().then(cpuData => {
          let cpuPercentage = cpuData.cpuPercentage;
          let data = cpuChart.data.datasets[0].data 
          shiftCharacters(data, cpuPercentage) 
          cpuChart.update();
        });
      }, 2000);
    
     
      //end of the DOM
    });
