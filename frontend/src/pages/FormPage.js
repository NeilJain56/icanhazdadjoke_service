import React, { useState } from 'react';

function FormPage() {
  const [number, setNumber] = useState('');
  const [text, setText] = useState('');
  const [response, setResponse] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setResponse([]);
    setError(null);
    setLoading(true);
    try {
      const res = await fetch(`http://127.0.0.1:5000/get_jokes?num_jokes=${number}&search_term=${text}`);
      const data = await res.json();

      if (data.error) {
        setError(data.error);
      } else {
        const jokes = data.jokes || [];
        jokes.forEach((joke, index) => {
          setTimeout(() => {
            setResponse(prevResponse => [...prevResponse, joke]);
          }, index * 5000); // 5-second delay for each joke
        });
      }
    } catch (error) {
      console.error('Error:', error);
      setError('An error occurred while fetching the data.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="w-full h-full max-w-4xl p-8 bg-base-100 shadow-2xl flex">
        {/* Left Side: Form */}
        <div className="w-1/2 flex flex-col justify-center">
          <div className="card-body w-full">
            <h2 className="card-title text-center">Submit A Number Of Jokes And A Search Term</h2>
            <form onSubmit={handleSubmit}>
              <div className="form-control">
                <label className="label">
                  <span className="label-text">Number</span>
                </label>
                <input
                  type="number"
                  value={number}
                  onChange={(e) => setNumber(e.target.value)}
                  className="input input-bordered"
                  required
                /> 
              </div>
              <div className="form-control mt-4">
                <label className="label">
                  <span className="label-text">Search Term</span>
                </label>
                <input
                  type="text"
                  value={text}
                  onChange={(e) => setText(e.target.value)}
                  className="input input-bordered"
                  required
                />
              </div>
              <div className="form-control mt-6">
                <button type="submit" className="btn btn-primary w-full" disabled={loading}>
                  Submit
                </button>
              </div>
            </form>
          </div>
        </div>

        {/* Right Side: Response Display */}
        <div className="w-1/2 flex flex-col justify-center">
          <div className="card-body w-full">
            <h2 className="card-title text-center">API Response</h2>
            <div className="text-center mt-4">
              {loading && <p>Loading...</p>}
              {error ? (
                <p className="text-red-500">{error}</p>
              ) : (
                response.map((joke, index) => (
                  <div key={index} className="mt-2">
                    <p>{joke}</p>
                    {index < response.length - 1 && <hr className="my-4 border-t border-gray-300" />}
                  </div>
                ))
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default FormPage;
