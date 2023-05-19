import "./App.css"
import React, { useState } from 'react';

function App() {
  const [algorithm, setAlgorithm] = useState('shift');
  const [method, setMethod] = useState('encrypt');
  const [input, setInput] = useState('');
  const [key, setKey] = useState('');
  const [output, setOutput] = useState('');

  const handleAlgorithmChange = (event) => {
    setAlgorithm(event.target.value);
  };

  const handleMethodChange = (event) => {
    setMethod(event.target.value);
  };

  const handleInputChange = (event) => {
    setInput(event.target.value);
  };

  const handleKeyChange = (event) => {
    setKey(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    const endpoint = method === 'encrypt' ? 'https://b1d3-154-182-88-116.ngrok.io/' : 'https://b1d3-154-182-88-116.ngrok.io/';

    const data = {
      input: input,
      key: key,
      algorithm: algorithm
    };
    
    fetch(endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        setOutput(method === 'encrypt' ? data.ciphertext: data.plaintext)
      })
      .catch(error => console.error(error));
  };
  return (
    <div className="App">
      <p>Cipher Algorithms</p>
      <form onSubmit={handleSubmit}>
        <label>
          Choose Algorithm:
          <select value={algorithm} onChange={handleAlgorithmChange}>
            <option value="shift">Shift Cipher</option>
            <option value="mono">Monoalphabetic Cipher</option>
            <option value="affine">Affine Cipher</option>
            <option value="substitution">Substitution Cipher</option>
            <option value="playfair">Playfair Cipher</option>
            <option value="vigenere">Vigenere Cipher</option>
            <option value="rail">Rail Fence Cipher</option>
            <option value="row">Row Transposition Cipher</option>
          </select>
        </label>
        <br />
        <label>
          Choose Method:
          <select value={method} onChange={handleMethodChange}>
            <option value="encrypt">Encrypt</option>
            <option value="decrypt">Decrypt</option>
          </select>
        </label>
        <br />
        <label>
          {method === 'encrypt' ? 'Enter Plain Text:' : 'Enter Cipher Text:'}
          <input type="text" required value={input} onChange={handleInputChange} />
        </label>
        <br />
        <label>
          Enter Key:
          <input type="text" required value={key} onChange={handleKeyChange} />
        </label>
        <br />
        <button type="submit">{method === 'decrypt' ? 'Decryption' : 'Encryption'}</button>
        {output && (
        <h2 className="output">{output}</h2>
      )}
      {!output && (
        <h2 className="nooutput">output</h2>
      )}
      </form>
    </div>
  );
}

export default App;
