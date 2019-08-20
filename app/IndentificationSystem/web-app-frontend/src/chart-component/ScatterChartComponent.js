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
                {   backgroundColor: 'red',
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
                    datasets:[
                        {
                            label: 'My First dataset',
                            fill: false,
                            backgroundColor: 'rgba(75,192,192,0.4)',
                            pointBorderColor: 'rgba(75,192,192,1)',
                            pointBackgroundColor: '#fff',
                            pointBorderWidth: 1,
                            pointHoverRadius: 5,
                            pointHoverBackgroundColor: 'rgba(75,192,192,1)',
                            pointHoverBorderColor: 'rgba(220,220,220,1)',
                            pointHoverBorderWidth: 2,
                            pointRadius: 1,
                            pointHitRadius: 10,
                            data:[{
                                x: Object.values(data.param_1)[0],
                                y: Object.values(data.param_2)[0]
                            },
                                {
                                x: Object.values(data.param_1)[1],
                                y: Object.values(data.param_2)[1]
                            },

                                {
                                x: Object.values(data.param_1)[2],
                                y: Object.values(data.param_2)[2]
                            },

                                {
                                x: Object.values(data.param_1)[3],
                                y: Object.values(data.param_2)[3]
                            },
                            {
                                x: Object.values(data.param_1)[4],
                                y: Object.values(data.param_2)[4]
                            },
                            {
                                x: Object.values(data.param_1)[5],
                                y: Object.values(data.param_2)[5]
                            },
                            {
                                x: Object.values(data.param_1)[6],
                                y: Object.values(data.param_2)[6]
                            },
                            {
                                x: Object.values(data.param_1)[7],
                                y: Object.values(data.param_2)[7]
                            },
                            {
                                x: Object.values(data.param_1)[8],
                                y: Object.values(data.param_2)[8]
                            },
                            {
                                x: Object.values(data.param_1)[9],
                                y: Object.values(data.param_2)[9]
                            },
                            {
                                x: Object.values(data.param_1)[10],
                                y: Object.values(data.param_2)[10]
                            },
                            {
                                x: Object.values(data.param_1)[11],
                                y: Object.values(data.param_2)[11]
                            },
                            {
                                x: Object.values(data.param_1)[12],
                                y: Object.values(data.param_2)[12]
                            },
                            {
                                x: Object.values(data.param_1)[13],
                                y: Object.values(data.param_2)[13]
                            },
                            {
                                x: Object.values(data.param_1)[14],
                                y: Object.values(data.param_2)[14]
                            },
                            {
                                x: Object.values(data.param_1)[15],
                                y: Object.values(data.param_2)[15]
                            },
                            {
                                x: Object.values(data.param_1)[16],
                                y: Object.values(data.param_2)[16]
                            },
                            {
                                x: Object.values(data.param_1)[17],
                                y: Object.values(data.param_2)[17]
                            },
                            {
                                x: Object.values(data.param_1)[18],
                                y: Object.values(data.param_2)[18]
                            },
                            {
                                x: Object.values(data.param_1)[19],
                                y: Object.values(data.param_2)[19]
                            },
                            {
                                x: Object.values(data.param_1)[20],
                                y: Object.values(data.param_2)[20]
                            },
                            {
                                x: Object.values(data.param_1)[21],
                                y: Object.values(data.param_2)[21]
                            },
                            {
                                x: Object.values(data.param_1)[22],
                                y: Object.values(data.param_2)[22]
                            },
                            {
                                x: Object.values(data.param_1)[23],
                                y: Object.values(data.param_2)[23]
                            },
                            {
                                x: Object.values(data.param_1)[24],
                                y: Object.values(data.param_2)[24]
                            },
                            {
                                x: Object.values(data.param_1)[25],
                                y: Object.values(data.param_2)[25]
                            },
                            {
                                x: Object.values(data.param_1)[26],
                                y: Object.values(data.param_2)[26]
                            },
                            {
                                x: Object.values(data.param_1)[27],
                                y: Object.values(data.param_2)[27]
                            },
                            {
                                x: Object.values(data.param_1)[28],
                                y: Object.values(data.param_2)[28]
                            },
                            {
                                x: Object.values(data.param_1)[29],
                                y: Object.values(data.param_2)[29]
                            },
                            {
                                x: Object.values(data.param_1)[30],
                                y: Object.values(data.param_2)[30]
                            },
                            {
                                x: Object.values(data.param_1)[31],
                                y: Object.values(data.param_2)[31]
                            },
                            {
                                x: Object.values(data.param_1)[32],
                                y: Object.values(data.param_2)[32]
                            },
                            {
                                x: Object.values(data.param_1)[33],
                                y: Object.values(data.param_2)[33]
                            },
                            {
                                x: Object.values(data.param_1)[34],
                                y: Object.values(data.param_2)[34]
                            },
                            {
                                x: Object.values(data.param_1)[35],
                                y: Object.values(data.param_2)[35]
                            },
                            {
                                x: Object.values(data.param_1)[36],
                                y: Object.values(data.param_2)[36]
                            },
                            {
                                x: Object.values(data.param_1)[37],
                                y: Object.values(data.param_2)[37]
                            },
                            {
                                x: Object.values(data.param_1)[38],
                                y: Object.values(data.param_2)[38]
                            },
                            {
                                x: Object.values(data.param_1)[39],
                                y: Object.values(data.param_2)[39]
                            },
                                {
                                x: Object.values(data.param_1)[40],
                                y: Object.values(data.param_2)[40]
                            }],
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