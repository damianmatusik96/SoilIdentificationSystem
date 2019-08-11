import React from "react";
import {Button, Card, Col, Container, Row} from "react-bootstrap";
import SubmitComponent from "./SubmittComponent";
import ChartComponent from "../chart-component/ChartComponent";

const FileTable = ({title, text, type}) => (
    <div>
        <Card>
            <Card.Header as="h5">{title}</Card.Header>
            <Card.Body>
                <Card.Text>
                    {text}
                </Card.Text>
                <SubmitComponent type={type}/>
                <Button variant="dark" type='submit' style={{margin: 5}}>Submit</Button>
            </Card.Body>
        </Card>
    </div>

);

const DataTables = () => (
    <section>
        <Container>
            <Row>
                <Col>
                    <FileTable
                        title='Siemano'
                        text='tutaj jakas tabelka na pliki'
                        type='train'
                    />
                </Col>
                <Col>
                    <FileTable
                        title='Siemano'
                        text='tutaj jakas tabelka na pliki'
                        type='predict'
                    />
                </Col>
            </Row>
            <Row>
                <ChartComponent/>
            </Row>
        </Container>
    </section>
);

export default DataTables;