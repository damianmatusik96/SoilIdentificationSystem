import React from 'react';
import DataTables from './file-component/DataTables'
import TopBar from './top-bar-component/TopBar'
import {Route, BrowserRouter as Router} from "react-router-dom";
import ChartsPanel from "./chart-component/ChartsPanel";

const GetStarted = () => (
    <div className="App">
        <main className='content-component'>
            <DataTables/>
            <ChartsPanel/>
        </main>
    </div>
);

const About = () => (
    <h1>Siemano</h1>
);

const Home = () => (
  <h1>Home</h1>
);

const App = () => (
      <Router>
          <header className="App-header">
            <TopBar style={{margin: 5,}}/>
        </header>
        <div className="App">
            <Route exact path="/" component={Home}/>
          <Route path="/get-started" component={GetStarted} />
          <Route path="/about" component={About} />
        </div>
      </Router>

);
export default App;
