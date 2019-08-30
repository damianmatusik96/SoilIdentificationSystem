import React from 'react';
import {Button, Card, Col, Container, Row, Table} from "react-bootstrap";
import SubmitComponent from "./SubmittComponent";
import {Link} from "react-router-dom";


const FileTable = ({onClick, title, type, filenames}) => (
    <div>
        <Card bg="dark" text="white">
            <Card.Header as="h5">{title}</Card.Header>
            <Card.Body>
                <Card.Text>
                    <Table striped bordered hover variant="dark">
                        <thead>
                        <tr>
                            <th></th>
                            <th>Filename</th>
                        </tr>
                        </thead>
                        <tbody>
                        {filenames.map((fname, index) => (
                            <tr>
                                <td>{index + 1}</td>
                                <td>{fname}</td>
                            </tr>
                        ))}
                        </tbody>
                    </Table>
                </Card.Text>
                <SubmitComponent onClick={onClick} type={type}/>
            </Card.Body>
        </Card>
    </div>

);

class DataTables extends React.Component {
    state = {
        predictFiles: [],
        dataTestingFiles: []
    };

    onPredictFilesAdd = (files, e) => {
        this.onChange(files, e);
        this.setState(
            {
                predictFiles: [
                    ...this.state.predictFiles,
                    ...Array.from(files).map(({name}) => name)
                ]
            }
        )

    };
    onDataTestingFilesAdd = (files, e) => {
        this.onChange(files, e);
        this.setState(
            {
                dataTestingFiles: [
                    ...this.state.dataTestingFiles,
                    ...Array.from(files).map(({name}) => name)
                ]
            }
        )

    };
    onChange = (files, e) => {
        // e.preventDefault();// Stop form submit
        const formData = new FormData();
        formData.append('file', files[0]);
        console.warn("msg", formData);
        this.setState({file: formData});
        this.fileUpload(formData)
    };

    fileUpload = (formData) => {
        const url = 'http://localhost:5000/save/' + this.state.type;
        console.log(this.state.type);
        return fetch(url, {method: 'POST', body: formData})
            .then(response => console.log(response.data));

    };

    render() {
        return (
            <section>
                <Container>
                    <Row>
                        <Col>
                            <FileTable
                                title='Data for generate average profile'
                                text='tutaj jakas tabelka na pliki'
                                type='train'
                                filenames={this.state.predictFiles}
                                onClick={this.onPredictFilesAdd}
                            />
                        </Col>
                        <Col>
                            <FileTable
                                title='Data for testing'
                                text='tutaj jakas tabelka na pliki'
                                type='predict'
                                filenames={this.state.dataTestingFiles}
                                onClick={this.onDataTestingFilesAdd}
                            />
                        </Col>
                    </Row>
                    <Link to='/results'>
                        <div className='Button'>
                            <Button variant="dark" size="lg" block>
                                Generate profile
                            </Button>
                        </div>
                    </Link>
                </Container>

            </section>
        );
    }
}

export default DataTables;