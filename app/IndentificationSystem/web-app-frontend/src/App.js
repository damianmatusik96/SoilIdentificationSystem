import React from 'react';
import {Navbar, Nav, Row, Container, Card, Button, Col} from "react-bootstrap";
import InputFiles from 'react-input-files';
import {post} from 'ajax'



class SubmitComponent extends React.Component {
    state = {
        file: 'dupa'
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
        const url = 'http://localhost:5000/uploader';
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

const FileTable = ({title, text}) => {
    return (
        <div>
           <Card>
                <Card.Header as="h5">{title}</Card.Header>
                <Card.Body>
                    <Card.Text>
                        {text}
                    </Card.Text>
                    <SubmitComponent/>
                    <Button variant="dark" type='submit' style={{margin: 5}}>Submit</Button>
                </Card.Body>
            </Card>
        </div>
    );
};

const DataTables = () => (
    <main>
        <section>
            <Container>
                <Row>
                    <Col>
                        <FileTable
                            title='Siemano'
                            text='tutaj jakas tabelka na pliki'
                        />
                    </Col>
                    <Col>
                        <FileTable
                            title='Siemano'
                            text='tutaj jakas tabelka na pliki'
                        />
                    </Col>
                </Row>
            </Container>
        </section>
    </main>
);

const TopBar = () => (
    <Navbar bg="dark" variant="dark">
        <Navbar.Brand href="#home">Navbar</Navbar.Brand>
        <Nav className="mr-auto">
            <Nav.Link href="#home">Home</Nav.Link>
            <Nav.Link href="#features">Features</Nav.Link>
            <Nav.Link href="#pricing">Pricing</Nav.Link>
        </Nav>
    </Navbar>
);


const App = () => (
    <div className="App">
        <header className="App-header">
            <TopBar style={{margin: 5,}}/>
        </header>
        <main className='content-component'>
            <DataTables/>
        </main>
    </div>

);
export default App;
