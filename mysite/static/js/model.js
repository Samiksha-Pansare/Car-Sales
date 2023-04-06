document.addEventListener("DOMContentLoaded", () => {
  var data = JSON.parse("{{sales_2021|safe}}".replaceAll("'", '"'));
  var sales_2021 = document.getElementById("sales-2021").innerHTML;
  console.log(sales_2021)
  var xArray = [];
  var yArray = []; 
  
  var months = Object.keys(sales_2021); // xArray needs to have Python Dictionary's keys
  var sales_value_2021 = Object.values(sales_2021) // yArray needs to have Python Dictionary's values

  new Chart(document.querySelector('#lineChart'), {
    type: 'line',
    data: {
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July','August','September','October','November','December'],
      datasets: [{
        label: 'Line Chart',
        data: sales_value_2021,
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
  new Chart(document.querySelector('#nyChart'), {
      type: 'line',
      data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [{
          label: 'Line Chart',
          data: [65, 59, 80, 81, 56, 55, 40],
          fill: false,
          borderColor: 'rgb(75, 192, 192)',
          tension: 0.1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
    new Chart(document.querySelector('#pieChart'), {
      type: 'pie',
      data: {
        labels: [
          'White',
          'Black',
          'Grey'
        ],
        datasets: [{
          label: 'My First Dataset',
          data: [300, 50, 100],
          backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(54, 162, 235)',
            'rgb(255, 205, 86)'
          ],
          hoverOffset: 4
        }]
      }
    });
    new Chart(document.querySelector('#doughnutChart'), {
      type: 'doughnut',
      data: {
        labels: [
          'White',
          'Black',
          'Grey'
        ],
        datasets: [{
          label: 'My First Dataset',
          data: [300, 50, 100],
          backgroundColor: [
            'rgb(255, 99, 132)',
            'rgb(54, 162, 235)',
            'rgb(255, 205, 86)'
          ],
          hoverOffset: 4
        }]
      }
    });
});