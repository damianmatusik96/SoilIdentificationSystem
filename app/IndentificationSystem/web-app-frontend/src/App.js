import React from 'react';
import DataTables from './file-component/DataTables'
import TopBar from './top-bar-component/TopBar'
import {BrowserRouter as Router, Route} from "react-router-dom";
import ChartsPanel from "./chart-component/ChartsPanel";
import {ListGroup} from "react-bootstrap";
// import "./index.css"

const GetStarted = () => (
    <div className="App">
        <main className='content-component'>
            <DataTables/>
        </main>
    </div>
);

const About = () => (
    <div>
        <main className='charts-component'>
            <ChartsPanel/>
        </main>
    </div>
);

const Home = () => (
    <ListGroup>
        <ListGroup.Item variant="light">
            <h1>Soil identification system</h1>
        </ListGroup.Item>
        <ListGroup.Item variant="light">
            <h2>System supports construction engineers in the process of identifying soil layers. The main assumption
                while creating the software was to combine artificial intelligence algorithms with a web application
                that would significantly save time and money in designing buildings structures.
            </h2>
            <h2>
                Click "Get started" and enjoy
            </h2>
        </ListGroup.Item>
        <ListGroup.Item variant="light">
            <h3>Created for Engineer's Thesis by Damian Matusik</h3>
        </ListGroup.Item>
    </ListGroup>
);

const App = () => (
    <Router>
        <header className="App-header">
            <TopBar style={{margin: 5,}}/>
        </header>
        <div className="App">
            <Route exact path="/" component={Home}/>
            <Route path="/get-started" component={GetStarted}/>
            <Route path="/results" component={About}/>
        </div>
    </Router>

);
export default App;
