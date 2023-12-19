document.addEventListener("DOMContentLoaded", async () => {

    function shiftCharacters(arr, newVariable) {
        let lastIndex = arr.length - 1;
      
        for (let i = 0; i < lastIndex; i++) {
          arr[i] = arr[i + 1];
        }
      
        arr[lastIndex - 1] = newVariable;
        arr.pop(); // Remove the last element
      
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
        cpuChart.data.datasets[0].data[0] = freeRam;
        cpuChart.data.datasets[0].data[1] = usedRam;
        cpuChart.update();
        }
        
        InitalRAM();
        
    let cpuChart = new Chart(document.querySelector('#pieChart'), {
      type: 'pie',
      data: {
        labels: [
          'Free RAM',
          'Used RAM',
        ],
        datasets: [{
          label: 'My First Dataset',
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
          cpuChart.data.datasets[0].data[0] = freeRam;
          cpuChart.data.datasets[0].data[1] = usedRam;
          cpuChart.update();
        });
      }, 2000);
      


      // CPU usage






      //Cpu area graph
     
        const data = [0,0,0,0,0]
        const maxValue = Math.max.apply(null, data)
        new Chart(document.querySelector('#lineChart'), {
          type: 'line',
          data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
            datasets: [{
              label: 'Line Chart',
              data: [20, 30, 80, 15, 5, 4, 55],
              fill: true,
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
        



    
     
      //end of the DOM
    });
