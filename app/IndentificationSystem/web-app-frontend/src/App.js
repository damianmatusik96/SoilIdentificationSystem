import React from 'react';
import DataTables from './file-component/DataTables'
import TopBar from './top-bar-component/TopBar'


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
