import React from 'react';
import DataTables from './file-component/DataTables'
import TopBar from './top-bar-component/TopBar'
import {
    Route,
    BrowserRouter as Router,
    Link
} from "react-router-dom";

const Home = () => (
    <div className="App">
        <header className="App-header">
            <TopBar style={{margin: 5,}}/>
        </header>
        <main className='content-component'>
            <DataTables/>
        </main>
    </div>
);

const About = () => (
    <h1>Hello</h1>
);

const App = () => (
      <Router>
        <div className="App">
          <Route exact path="/" component={Home} />
          <Route path="/about" component={About} />
        </div>
      </Router>

);
export default App;
