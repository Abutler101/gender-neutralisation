import React from 'react';
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
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css"
                      integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
                      crossOrigin="anonymous"/>
                <h2 className="display-4 text-center">Neutralise Gendered Language in Your Text</h2>
                <ApiInteraction endpointUrl={apiPath}/>
            </header>
        </div>
    );
}

export default App;
