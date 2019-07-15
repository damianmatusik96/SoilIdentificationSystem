import React from "react";
import InputFiles from "react-input-files";
import {Button, Card, Col, Container, Row} from "react-bootstrap";

class SubmitComponent extends React.Component {
    state = {
        file: 'dupa',
        type: this.props.type
    };
    onChange = (files, e) => {
        const formData = new FormData();
        formData.append('file', files[0]);
        console.warn("msg", formData);
        this.setState({file: formData});
        //e.preventDefault();// Stop form submit
        this.fileUpload(formData)
    };
    fileUpload = (formData) => {
        const url = 'http://localhost:5000/save/' + this.state.type;
        console.log(this.state.type);
        // return post(url, formData).then(response => console.warn("result: ", response))
        return fetch(url, { method: 'POST', body: formData}).then(response => console.log(response));

    };
    render() {
        return (
                <InputFiles onChange={this.onChange}>
                    <Button variant="dark"
                            style={{margin: 5}}>
                        Upload files
                    </Button>
                </InputFiles>
        )
    }
}

const FileTable = ({title, text, type}) => (
        <div>
           <Card>
                <Card.Header as="h5">{title}</Card.Header>
                <Card.Body>
                    <Card.Text>
                        {text}
                    </Card.Text>
                    <SubmitComponent type={type} />
                    <Button variant="dark" type='submit' style={{margin: 5}}>Submit</Button>
                </Card.Body>
            </Card>
        </div>

);
const getProfile = () => (
    <p>Hello</p>
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
                    <Button variant='dark'
                            type='submit'
                            onClick={() => getProfile}>
                        Pokaz profil
                    </Button>
                </Row>
            </Container>
        </section>
);

export default DataTables;