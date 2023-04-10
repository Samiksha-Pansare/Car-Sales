Chart.defaults.global.legend.labels.usePointStyle = true;

  
  window.onload = function() {
    
    Chart.defaults.global.legend.labels.usePointStyle = true;
    var ctx = document.getElementById("visit-sale-chart").getContext("2d");

      var gradientStrokeViolet = ctx.createLinearGradient(0, 0, 0, 181);
      gradientStrokeViolet.addColorStop(0, 'rgba(218, 140, 255, 1)');
      gradientStrokeViolet.addColorStop(1, 'rgba(154, 85, 255, 1)');
      var gradientLegendViolet = 'linear-gradient(to right, rgba(218, 140, 255, 1), rgba(154, 85, 255, 1))';
      
      var gradientStrokeBlue = ctx.createLinearGradient(0, 0, 0, 360);
      gradientStrokeBlue.addColorStop(0, 'rgba(54, 215, 232, 1)');
      gradientStrokeBlue.addColorStop(1, 'rgba(177, 148, 250, 1)');
      var gradientLegendBlue = 'linear-gradient(to right, rgba(54, 215, 232, 1), rgba(177, 148, 250, 1))';

      var gradientStrokeRed = ctx.createLinearGradient(0, 0, 0, 300);
      gradientStrokeRed.addColorStop(0, 'rgba(255, 191, 150, 1)');
      gradientStrokeRed.addColorStop(1, 'rgba(254, 112, 150, 1)');
      var gradientLegendRed = 'linear-gradient(to right, rgba(255, 191, 150, 1), rgba(254, 112, 150, 1))';
    var barChartallData = {
    
        labels: [
          "Absence of OB",
          "Closeness",
          "Credibility",
          "Heritage",
          "M Disclosure",
          "Provenance",
          "Reliability",
          "Transparency"
        ],
        datasets: [
          {
            pointRadius: 0,
            fill: false,
            borderWidth: 1,
            fill: 'origin',
            label: "Mumbai",
            backgroundColor: "rgba(254, 112, 150, 1)",
            borderColor: "rgba(255, 191, 150, 1)",
            borderWidth: 1,
            data: [3, 5, 6, 7,3, 5, 6, 7]
          },
          {
            label: "Pune",
            backgroundColor: "rgba(154, 85, 255, 1)",
            borderColor: "rgba(218, 140, 255, 1)",
            borderWidth: 1,
            data: [4, 7, 3, 6, 10,7,4,6]
          },
          {
            label: "Nashik",
            backgroundColor: "rgba(54, 215, 232, 1)",
            borderColor: "rgba(177, 148, 250, 1)",
            borderWidth: 1,
            data: [10,7,4,6,9,7,3,10]
          },
          {
            label: "Nagpur",
            backgroundColor: "rgba(6, 185, 157, 1)",
            borderColor: "rgba(132, 217, 210, 1)",
            borderWidth: 1,
            data: [6,9,7,3,10,7,4,6]
          }
        ],
        options: {
            responsive: true,
            scales: {
                yAxes: [{
                    ticks: {
                        display: false,
                        min: 0,
                        stepSize: 20,
                        max: 80
                    },
                    gridLines: {
                      drawBorder: false,
                      color: '#322f2f',
                      zeroLineColor: '#322f2f'
                    }
                }],
                xAxes: [{
                    gridLines: {
                      display:false,
                      drawBorder: false,
                      color: 'rgba(0,0,0,1)',
                      zeroLineColor: 'rgba(235,237,242,1)'
                    },
                    ticks: {
                        padding: 20,
                        fontColor: "#9c9fa6",
                        autoSkip: true,
                    },
                    categoryPercentage: 0.5,
                    barPercentage: 0.5
                }]
              }
            },
            elements: {
              point: {
                radius: 0
              }
            }
      };
      
      var chartOptions = {
        responsive: true,
        legend: {
          position: "top"
        },
        title: {
          display: true,
          text: "Chart.js Bar Chart"
        },
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true
            }
          }]
        }
      }
    window.myBar = new Chart(ctx, {
      type: "bar",
      data: barChartallData,
      options: chartOptions
    });
    
  };
  