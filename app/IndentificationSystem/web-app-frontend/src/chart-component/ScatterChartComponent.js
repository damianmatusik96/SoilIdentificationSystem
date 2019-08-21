import React from "react";
import {Button} from "react-bootstrap";
import {Scatter} from "react-chartjs-2";

class ScatterChartComponent extends React.Component {
    state = {
        chartData: {
            type: 'scatter',
            label: 'My First dataset',
            fill: false,
            backgroundColor: 'blue',
            datasets: [
                {
                    backgroundColor: 'red',
                    data: [{
                        x: 10,
                        y: 25
                    }],
                }
            ]
        }
    };

    getProfile = () => {
        const url = "http://localhost:5000/predict";
        fetch(url)
            .then(response => response.json())
            .then((data) => this.setState({
                chartData: {
                    type: 'scatter',
                    datasets: [
                        {
                            label: 'My First dataset',
                            fill: false,
                            backgroundColor: 'rgba(75,192,192,0.4)',
                            pointBorderColor: 'rgba(75,192,192,1)',
                            pointBackgroundColor: 'rgba(75,192,192,1)',
                            pointHoverBackgroundColor: 'rgba(75,192,192,1)',
                            pointHoverBorderColor: 'rgba(220,220,220,1)',
                            pointRadius: 4,
                            data: data.groups.group1,
                        },
                        {
                            label: 'My First dataset',
                            fill: false,
                            backgroundColor: 'green',
                            pointBorderColor: 'green',
                            pointBackgroundColor: 'green',
                            pointHoverBackgroundColor: 'green',
                            pointHoverBorderColor: 'green',
                            pointRadius: 4,
                            data: data.groups.group2,
                        },
                        {
                            label: 'My First dataset',
                            fill: false,
                            backgroundColor: 'red',
                            pointBorderColor: 'red',
                            pointBackgroundColor: 'red',
                            pointHoverBackgroundColor: 'red',
                            pointHoverBorderColor: 'red',
                            pointRadius: 4,
                            data: data.groups.group3,
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
                <Scatter ref='chart' data={this.state.chartData}/>
            </div>
        )
    };
}

export default ScatterChartComponent;