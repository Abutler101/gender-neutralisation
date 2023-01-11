import React from 'react';
import logo from './logo.svg';
import './App.css';
import ApiInteraction from "./components/ApiInteraction";

function App() {
    const host = "192.168.58.244" // process.env.REACT_APP_API_HOST || '0.0.0.0';
    const port = 8095 // process.env.REACT_APP_API_PORT || '8095';
    const endpoint = "";
    const apiPath = `http://${host}:${port}/${endpoint}`;

    return (
        <div className="App">
            <header className="App-header">
                <ApiInteraction endpointUrl={apiPath}/>
            </header>
        </div>
    );
}

export default App;
