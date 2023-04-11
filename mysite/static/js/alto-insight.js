// var my_var = {{region_wise}};

// console.log(my_var)
const data = JSON.parse(document.getElementById('data').textContent);
console.log(data)

const color_wise = Object.values(data["color_wise"])
console.log(color_wise)

const year_wise = Object.values(data["year_wise"])
console.log(year_wise)

const mumbai = Object.values(data["region_wise"]["Mumbai"])
console.log(mumbai)
const pune = Object.values(data["region_wise"]["Pune"])
console.log(pune)
const nashik = Object.values(data["region_wise"]["Nashik"])
console.log(nashik)
const nagpur = Object.values(data["region_wise"]["Nagpur"])
console.log(nagpur)

$(function () {
    /* ChartJS
     * -------
     * Data and config for chartjs
     */
    'use strict';
    var data = {
      labels: ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"],
      datasets: [{
        label: 'Number of Sales',
        data: year_wise,
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
          'rgba(255,99,132,1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1,
        fill: false
      }]
    };
    var dataDark = {
      labels: ["2013", "2014", "2014", "2015", "2016", "2017"],
      datasets: [{
        label: '# of Votes',
        data: [10, 19, 3, 5, 2, 3],
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
          'rgba(255,99,132,1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1,
        fill: false
      }]
    };
    var multiLineData = {
      labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
      datasets: [{
        label: 'Dataset 1',
        data: [12, 19, 3, 5, 2, 3],
        borderColor: [
          '#587ce4'
        ],
        borderWidth: 2,
        fill: false
      },
      {
        label: 'Dataset 2',
        data: [5, 23, 7, 12, 42, 23],
        borderColor: [
          '#ede190'
        ],
        borderWidth: 2,
        fill: false
      },
      {
        label: 'Dataset 3',
        data: [15, 10, 21, 32, 12, 33],
        borderColor: [
          '#f44252'
        ],
        borderWidth: 2,
        fill: false
      }
      ]
    };
    var options = {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true
          }
        }]
      },
      legend: {
        display: false
      },
      elements: {
        point: {
          radius: 0
        }
      }
  
    };
    var optionsDark = {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true
          },
          gridLines: {
            color: '#322f2f',
            zeroLineColor: '#322f2f'
          }
        }],
        xAxes: [{
          ticks: {
            beginAtZero: true
          },
          gridLines: {
            color: '#322f2f',
          }
        }],
      },
      legend: {
        display: false
      },
      elements: {
        point: {
          radius: 0
        }
      }
  
    };
    var doughnutPieData = {
      datasets: [{
        data: color_wise,
        backgroundColor: [
          'rgba(255, 99, 132, 0.5)',
          'rgba(54, 162, 235, 0.5)',
          'rgba(255, 206, 86, 0.5)',
          'rgba(75, 192, 192, 0.5)',
          'rgba(153, 102, 255, 0.5)',
          'rgba(255, 159, 64, 0.5)'
        ],
        borderColor: [
          'rgba(255,99,132,1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)'
        ],
      }],
  
      // These labels appear in the legend and in the tooltips when hovering different arcs
      labels: [
        'Black',
        'Grey',
        'White',
      ]
    };
    var doughnutPieOptions = {
      responsive: true,
      animation: {
        animateScale: true,
        animateRotate: true
      }
    };
    var areaData = {
      labels: ["2013", "2014", "2015", "2016", "2017"],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
          'rgba(255,99,132,1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1,
        fill: true, // 3: no fill
      }]
    };
  
    var areaDataDark = {
      labels: ["2013", "2014", "2015", "2016", "2017"],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)'
        ],
        borderColor: [
          'rgba(255,99,132,1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)'
        ],
        borderWidth: 1,
        fill: true, // 3: no fill
      }]
    };
  
    var areaOptions = {
      plugins: {
        filler: {
          propagate: true
        }
      }
    }
  
    var areaOptionsDark = {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true
          },
          gridLines: {
            color: '#322f2f',
            zeroLineColor: '#322f2f'
          }
        }],
        xAxes: [{
          ticks: {
            beginAtZero: true
          },
          gridLines: {
            color: '#322f2f',
          }
        }],
      },
      plugins: {
        filler: {
          propagate: true
        }
      }
    }
  
    var multiAreaData = {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
      datasets: [{
        label: 'Facebook',
        data: [8, 11, 13, 15, 12, 13, 16, 15, 13, 19, 11, 14],
        borderColor: ['rgba(255, 99, 132, 0.5)'],
        backgroundColor: ['rgba(255, 99, 132, 0.5)'],
        borderWidth: 1,
        fill: true
      },
      {
        label: 'Twitter',
        data: [7, 17, 12, 16, 14, 18, 16, 12, 15, 11, 13, 9],
        borderColor: ['rgba(54, 162, 235, 0.5)'],
        backgroundColor: ['rgba(54, 162, 235, 0.5)'],
        borderWidth: 1,
        fill: true
      },
      {
        label: 'Linkedin',
        data: [6, 14, 16, 20, 12, 18, 15, 12, 17, 19, 15, 11],
        borderColor: ['rgba(255, 206, 86, 0.5)'],
        backgroundColor: ['rgba(255, 206, 86, 0.5)'],
        borderWidth: 1,
        fill: true
      }
      ]
    };
  
    var multiAreaOptions = {
      plugins: {
        filler: {
          propagate: true
        }
      },
      elements: {
        point: {
          radius: 0
        }
      },
      scales: {
        xAxes: [{
          gridLines: {
            display: false
          }
        }],
        yAxes: [{
          gridLines: {
            display: false
          }
        }]
      }
    }
  
    var scatterChartData = {
      datasets: [{
        label: 'First Dataset',
        data: [{
          x: -10,
          y: 0
        },
        {
          x: 0,
          y: 3
        },
        {
          x: -25,
          y: 5
        },
        {
          x: 40,
          y: 5
        }
        ],
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)'
        ],
        borderColor: [
          'rgba(255,99,132,1)'
        ],
        borderWidth: 1
      },
      {
        label: 'Second Dataset',
        data: [{
          x: 10,
          y: 5
        },
        {
          x: 20,
          y: -30
        },
        {
          x: -25,
          y: 15
        },
        {
          x: -10,
          y: 5
        }
        ],
        backgroundColor: [
          'rgba(54, 162, 235, 0.2)',
        ],
        borderColor: [
          'rgba(54, 162, 235, 1)',
        ],
        borderWidth: 1
      }
      ]
    }
  
    var scatterChartDataDark = {
      datasets: [{
        label: 'First Dataset',
        data: [{
          x: -10,
          y: 0
        },
        {
          x: 0,
          y: 3
        },
        {
          x: -25,
          y: 5
        },
        {
          x: 40,
          y: 5
        }
        ],
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)'
        ],
        borderColor: [
          'rgba(255,99,132,1)'
        ],
        borderWidth: 1
      },
      {
        label: 'Second Dataset',
        data: [{
          x: 10,
          y: 5
        },
        {
          x: 20,
          y: -30
        },
        {
          x: -25,
          y: 15
        },
        {
          x: -10,
          y: 5
        }
        ],
        backgroundColor: [
          'rgba(54, 162, 235, 0.2)',
        ],
        borderColor: [
          'rgba(54, 162, 235, 1)',
        ],
        borderWidth: 1
      }
      ]
    }
  
    var scatterChartOptions = {
      scales: {
        xAxes: [{
          type: 'linear',
          position: 'bottom'
        }]
      }
    }
  
    var scatterChartOptionsDark = {
      scales: {
        xAxes: [{
          type: 'linear',
          position: 'bottom',
          gridLines: {
            color: '#322f2f',
            zeroLineColor: '#322f2f'
          }
        }],
        yAxes: [{
          gridLines: {
            color: '#322f2f',
            zeroLineColor: '#322f2f'
          }
        }]
      }
    }

    var barChartallData = {
    
        labels: ["2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"],
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
            data: mumbai
          },
          {
            label: "Pune",
            backgroundColor: "rgba(154, 85, 255, 1)",
            borderColor: "rgba(218, 140, 255, 1)",
            borderWidth: 1,
            data: pune
          },
          {
            label: "Nashik",
            backgroundColor: "rgba(54, 215, 232, 1)",
            borderColor: "rgba(177, 148, 250, 1)",
            borderWidth: 1,
            data: nashik
          },
          {
            label: "Nagpur",
            backgroundColor: "rgba(6, 185, 157, 1)",
            borderColor: "rgba(132, 217, 210, 1)",
            borderWidth: 1,
            data: nagpur
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
    // Get context with jQuery - using jQuery's .get() method.
    if ($("#barChart").length) {
      var barChartCanvas = $("#barChart").get(0).getContext("2d");
      // This will get the first returned node in the jQuery collection.
      var barChart = new Chart(barChartCanvas, {
        type: 'bar',
        data: data,
        options: options
      });
    }
    if ($("#barChartForecast").length) {
      var barChartCanvas = $("#barChartForecast").get(0).getContext("2d");
      // This will get the first returned node in the jQuery collection.
      var barChart = new Chart(barChartCanvas, {
        type: 'bar',
        data: data,
        options: options
      });
    }
  
    if ($("#barChartDark").length) {
      var barChartCanvasDark = $("#barChartDark").get(0).getContext("2d");
      // This will get the first returned node in the jQuery collection.
      var barChartDark = new Chart(barChartCanvasDark, {
        type: 'bar',
        data: dataDark,
        options: optionsDark
      });
    }
  
    if ($("#AllDatalineChart").length) {
      var lineChartCanvas = $("#AllDatalineChart").get(0).getContext("2d");
      var lineChart = new Chart(lineChartCanvas, {
        type: 'line',
        data: data,
        options: options
      });
    }
  
    if ($("#lineChartDark").length) {
      var lineChartCanvasDark = $("#lineChartDark").get(0).getContext("2d");
      var lineChartDark = new Chart(lineChartCanvasDark, {
        type: 'line',
        data: dataDark,
        options: optionsDark
      });
    }
  
    if ($("#linechart-multi").length) {
      var multiLineCanvas = $("#linechart-multi").get(0).getContext("2d");
      var lineChart = new Chart(multiLineCanvas, {
        type: 'line',
        data: multiLineData,
        options: options
      });
    }
  
    if ($("#areachart-multi").length) {
      var multiAreaCanvas = $("#areachart-multi").get(0).getContext("2d");
      var multiAreaChart = new Chart(multiAreaCanvas, {
        type: 'line',
        data: multiAreaData,
        options: multiAreaOptions
      });
    }
  
    if ($("#all-data-doughnutChart").length) {
      var doughnutChartCanvas = $("#all-data-doughnutChart").get(0).getContext("2d");
      var doughnutChart = new Chart(doughnutChartCanvas, {
        type: 'doughnut',
        data: doughnutPieData,
        options: doughnutPieOptions
      });
    }
  
    if ($("#pieChart").length) {
      var pieChartCanvas = $("#pieChart").get(0).getContext("2d");
      var pieChart = new Chart(pieChartCanvas, {
        type: 'pie',
        data: doughnutPieData,
        options: doughnutPieOptions
      });
    }
  
    if ($("#areaChart").length) {
      var areaChartCanvas = $("#areaChart").get(0).getContext("2d");
      var areaChart = new Chart(areaChartCanvas, {
        type: 'line',
        data: areaData,
        options: areaOptions
      });
    }
  
    if ($("#areaChartDark").length) {
      var areaChartCanvas = $("#areaChartDark").get(0).getContext("2d");
      var areaChart = new Chart(areaChartCanvas, {
        type: 'line',
        data: areaDataDark,
        options: areaOptionsDark
      });
    }
  
    if ($("#scatterChart").length) {
      var scatterChartCanvas = $("#scatterChart").get(0).getContext("2d");
      var scatterChart = new Chart(scatterChartCanvas, {
        type: 'scatter',
        data: scatterChartData,
        options: scatterChartOptions
      });
    }
  
    if ($("#scatterChartDark").length) {
      var scatterChartCanvas = $("#scatterChartDark").get(0).getContext("2d");
      var scatterChart = new Chart(scatterChartCanvas, {
        type: 'scatter',
        data: scatterChartDataDark,
        options: scatterChartOptionsDark
      });
    }
  
    if ($("#browserTrafficChart").length) {
      var doughnutChartCanvas = $("#browserTrafficChart").get(0).getContext("2d");
      var doughnutChart = new Chart(doughnutChartCanvas, {
        type: 'doughnut',
        data: browserTrafficData,
        options: doughnutPieOptions
      });
    }

    if ($("#RegionChart").length) {
        var multipleBarChartCanvas = $("#RegionChart").get(0).getContext("2d");
        var multipleBarChart= new Chart(multipleBarChartCanvas, {
          type: 'bar',
          data: barChartallData,
          options: chartOptions
        });
      }
  });