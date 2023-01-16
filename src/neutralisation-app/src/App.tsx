import React from 'react';
import './App.css';
import ApiInteraction from "./components/ApiInteraction";

function App() {
    const host = process.env.API_PUBLIC_HOST;
    const port = process.env.API_PORT || '8095';
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
