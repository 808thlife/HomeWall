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
      
      //end of the DOM
  });