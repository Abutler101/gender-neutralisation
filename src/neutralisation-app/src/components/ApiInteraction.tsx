import React, {useState} from 'react';

interface Props {
    endpointUrl: string;
}

interface ApiResponse {
  input_word_count: number;
  input_char_count: number;
  output_word_count: number;
  output_char_count: number;
  truncated: boolean;
  neutralised_text: string;
}

const calculateRows = () => {
  // Returns number of rows that would take up 40% of the screen height
  const screenHeight = window.innerHeight;
  return Math.floor(screenHeight * 0.75 / 20); // each row is roughly 20px in height
}


const ApiInteraction: React.FC<Props> = ({endpointUrl}) => {
    const [input, setInput] = useState('');
    const [apiResult, setApiResult] = useState<ApiResponse>();
    const [rows, setRows] = useState(calculateRows());

    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setInput(event.target.value);
    };

    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        const response = await fetch(
            endpointUrl,
            {method: 'POST', body: JSON.stringify({ text: input }), headers: { 'Content-Type': 'application/json' }}
        );
        const data = await response.json();
        setApiResult(data);
    };

    return (
        <div style={{
            display: 'flex',
            flexDirection: 'row',
            alignItems: 'center',
            justifyContent: 'center',
            height: '75%',
            width: '100%'
        }}>
            <form onSubmit={handleSubmit}>
                <textarea
                    placeholder="Enter text here"
                    value={input}
                    onChange={(event) => setInput(event.currentTarget.value)}
                    style={{
                        backgroundColor: '#f0f0f0',
                        borderRadius: '5px',
                        padding: '10px',
                        width: '40vw',
                        height: '40vh',
                        resize: 'none',
                        marginLeft: '30px',
                        outline: '1px solid'
                    }}
                    rows={rows}
                />
                <button type="submit" style={{
                    width: '200px',
                    height: '50px',
                    fontSize: '20px',
                    marginTop: '30px',
                    alignSelf: "center"}}>
                    Submit
                </button>
            </form>
            <div style={{
                    borderRadius: '5px',
                    padding: '10px',
                    backgroundColor: '#f0f0f0',
                    width: '40vw',
                    height: '40vh',
                    minHeight:'100%',
                    marginRight: '30px',
                    outline: '1px solid'
                }}>
                {apiResult?.neutralised_text}
            </div>
        </div>
    );
};

export default ApiInteraction;