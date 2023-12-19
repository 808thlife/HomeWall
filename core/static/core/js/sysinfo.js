document.addEventListener("DOMContentLoaded", async () => {

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


	

      var ctx = document.getElementById('stackedArea').getContext('2d');
      var myChart = new Chart(ctx, {
          type: 'line',
          data: {
              labels: ['10s', '8s', '6s', '4s', '2s'],
              datasets: [{
                  label: 'CPU usage',
                  data: [0, 20, 40, 10, 15],
                  backgroundColor: 'rgba(75, 192, 192, 0.5)',
                  borderColor: 'rgba(75, 192, 192, 1)',
                  borderWidth: 2,
                  fill: true,
              }, ]
          },
          options: {
              scales: {
                  y: {
                      title: {
                          display: true,
                          text: 'Percentage %'
                      },
                      ticks: {
                          beginAtZero: true,
                          stepSize: 20,
                          suggestedMax: 100, // Use suggestedMax instead of max
                          formatter: function(value) {
                              return value + '%';
                          }
                      }
                  },
                  x: {
                      stacked: true
                  }
              },
              layout: {
                  padding: {
                      left: 20,
                      right: 20,
                      top: 20,
                      bottom: 20
                  }
              },
              plugins: {
                  legend: {
                      position: 'top',
                  },
              }
          }
      }); 

    let cpuArr = myChart.data.datasets[0].data
    console.log(myChart.data.datasets[0].data)
    cpuArr[0] = 100
    myChart.data.datasets[0].data[1] = cpuArr
    console.log(cpuArr[0])
    cpuArr[1] = 80
    myChart.update()




      //end of the DOM
  });