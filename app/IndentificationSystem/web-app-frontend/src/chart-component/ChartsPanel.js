import React from 'react'
import {Col, Container, Row} from "react-bootstrap";
import ScatterChartComponent from "./ScatterChartComponent";
import LineChartComponent from "./LineChartComponent";


const ChartsPanel = () => (
    <Container>
        <Row>
            <Col>
                <LineChartComponent/>
            </Col>
            <Col>
                <ScatterChartComponent/>
            </Col>
        </Row>
        <Row>
            <Col>
                <LineChartComponent/>
            </Col>
            <Col>
                <ScatterChartComponent/>
            </Col>
        </Row>
    </Container>
);
export default ChartsPanel;