import React from 'react';
import {Navbar, Nav, Row, Container, Card, Button, Col} from "react-bootstrap";

const openWindowFunction = () => (
    console.log('dupa')
);

const sendDataFunction = () => (
    console.log('dupa dup')
);

const FileTable = ({title, text, openWindow, sendData}) => {
    return (
        <Card>
          <Card.Header as="h5">{title}</Card.Header>
          <Card.Body>
            <Card.Text>
                {text}
            </Card.Text>
                <Button variant="dark"
                        onClick={openWindow}
                        style={{margin:5,}}>
                    Upload Files
                    <input type='file'/>
                </Button>
                <Button variant="dark" onClick={sendData} style={{margin:5,}}>Button</Button>
          </Card.Body>
        </Card>
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
                                    openWindow={openWindowFunction}
                                    sendData={sendDataFunction}
                                />
                            </Col>
                            <Col>
                                <FileTable
                                    title='Siemano'
                                    text='tutaj jakas tabelka na pliki'
                                    openWindow={openWindowFunction}
                                    sendData={sendDataFunction}
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
      <header className="App-header" >
          <TopBar style={{margin: 5,}}/>
      </header>
      <DataTables/>
  </div>

);
export default App;
