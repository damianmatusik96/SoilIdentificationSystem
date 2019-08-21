import React from "react";
import {Button} from "react-bootstrap";
import {Scatter} from "react-chartjs-2";

class LineChartComponent extends React.Component {
    state = {
        options: {
            width: "800",
            height: "800",
        },
        chartData: {
            labels: ['Boston', 'Worcester', 'Springfield', 'Lowell', 'Cambridge', 'New Bedford'],
            datasets: [
                {
                    label: 'My First dataset',
                    backgroundColor: 'rgba(75,192,192,0.4)',
                    pointBorderColor: 'rgba(75,192,192,1)',
                    pointBackgroundColor: '#fff',
                    fill: false,
                    pointBorderWidth: 1,
                    pointHoverRadius: 5,
                    pointHoverBackgroundColor: 'rgba(75,192,192,1)',
                    pointHoverBorderColor: 'rgba(220,220,220,1)',
                    pointHoverBorderWidth: 2,
                    pointRadius: 1,
                    pointHitRadius: 10,
                    showLine: true,
                    data: [
                        {
                            x: 617594,
                            y: 181045
                        },
                        {
                            x: 106519,
                            y: 153060
                        }
                    ]
                }
            ]
        }
    };

    getProfile = () => {
        const url = "http://localhost:5000/predict";
        fetch(url)
            .then(response => response.json())
            .then((data) => this.setState({
                options: {
                    width: "800",
                    height: "800",
                    scales: {
                        yAxes: [{
                            ticks: {
                                reverse: true,
                            }
                        }]
                    }
                },
                chartData: {

                    datasets: [
                        {
                            label: 'My First dataset',
                            backgroundColor: 'rgba(75,192,192,0.4)',
                            pointBorderColor: 'rgba(75,192,192,1)',
                            pointBackgroundColor: 'rgba(75,192,192,1)',
                            borderColor: 'rgba(75,192,192,1)',
                            pointBorderWidth: 1,
                            pointHoverRadius: 5,
                            pointHoverBackgroundColor: 'rgba(75,192,192,1)',
                            pointHoverBorderColor: 'rgba(220,220,220,1)',
                            pointHoverBorderWidth: 2,
                            pointRadius: 1,
                            pointHitRadius: 10,
                            yAxes: 'reverse',
                            data: data.profile
                        }
                    ]
                },
            }));

        console.log(this.state)
    };

    render() {
        return (
            <div style={{padding: 50}}>
                <div>
                    <Button variant='dark'
                            type='submit'
                            onClick={() => this.getProfile()}>
                        Pokaz profil
                    </Button>
                </div>
                <Scatter className="chart" ref='chart' data={this.state.chartData} options={this.state.options}/>
            </div>
        )
    };
}

export default LineChartComponent;