import React from 'react';
import {Button, Card, Col, Container, Row} from "react-bootstrap";
import SubmitComponent from "./SubmittComponent";
import ChartsPanel from "../chart-component/ChartsPanel";

const FileTable = ({title, text, type}) => (
    <div>
        <Card>
            <Card.Header as="h5">{title}</Card.Header>
            <Card.Body>
                <Card.Text>
                    {text}
                </Card.Text>
                <SubmitComponent type={type}/>
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
        </Container>
    </section>
);

export default DataTables;