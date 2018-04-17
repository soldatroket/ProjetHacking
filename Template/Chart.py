#!/usr/bin/env python
#coding: utf8

#Fonction qui permmet d'afficher le grpahique des résultats

def Display(title, Label, Liste, Typegraph):
	Name=[]
	Score=[]

	for data in Liste:
		Name.append(data[0])
		Score.append(data[1])
	print '''<div class="col-lg-10">
		<div class="row"><div class="col-lg-12">
<canvas id="myChart" style="width:100%;"></canvas>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.1/Chart.js"></script>
<script>
var ctx = document.getElementById("myChart").getContext('2d');
var myChart = new Chart(ctx, {
    type: '''+"'"+Typegraph+"'"+''',
    data: {
        labels: '''
	print Name
	print ''' ,
        datasets: [{
            label: " '''+Label+''' " ,
            data: '''
	print Score
	print ''' ,
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
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }]
        },
	title: {
		display: true,
		text:'''+"'"+title+"'"+'''
	}
    }
}).Bar(myChart, {animation:false});
</script></div></div></div>'''
