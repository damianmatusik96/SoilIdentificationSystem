import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import {Button, Card} from "react-bootstrap";

const FileTable = ({title, text, openWindow, sendData}) => {
    return (
        <Card>
          <Card.Header as="h5">{title}</Card.Header>
          <Card.Body>
            <Card.Text>
                {text}
            </Card.Text>
                <Button variant="primary" onClick={openWindow}>Open window</Button>
                <Button variant="primary" onClick={sendData}>Send some data</Button>
          </Card.Body>
        </Card>
    );
};
const openWindowFunction = () => (
    console.log('dupa')
);

const sendDataFunction = () => (
    console.log('dupa dup')
);

ReactDOM.render(<FileTable
    title='Siemano'
    text='ustaw sobie'
    openWindow={openWindowFunction}
    sendData={sendDataFunction}
/>, document.getElementById('root'));


