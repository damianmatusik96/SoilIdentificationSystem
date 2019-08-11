import React from "react";
import {Button} from "react-bootstrap";
import {Line} from "react-chartjs-2";

class ChartComponent extends React.Component {
    state = {
        chartData: {
            labels: ['Boston', 'Worcester', 'Springfield', 'Lowell', 'Cambridge', 'New Bedford'],
            datasets: [
                {
                    data: [
                        617594,
                        181045,
                        153060,
                        106519,
                        105162,
                        95072
                    ],
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
                    labels: Object.values(data.labels),
                    datasets:[
                        {
                            data: Object.values(data.param_1)
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
                <div style={{padding: 50}}>
                    <Line ref='chart' data={this.state.chartData}/>
                </div>
            </div>
        )
    };
}
export default ChartComponent;