import React from 'react';
import './index.css';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col justify-center items-center">
      <header className="w-full max-w-4xl mx-auto text-center p-6">
        <h1 className="text-4xl font-bold text-blue-800">BYU CS Resume Analyzer</h1>
        <p className="text-lg text-gray-600 mt-2">Upload your resume to get instant feedback and a score based on our custom rubric.</p>
      </header>
      <main className="w-full max-w-2xl bg-white rounded-lg shadow-md p-8">
        <div className="text-center">
          <input type="file" className="text-sm text-grey-500
            file:mr-5 file:py-2 file:px-6
            file:rounded-full file:border-0
            file:text-sm file:font-medium
            file:bg-blue-50 file:text-blue-700
            hover:file:cursor-pointer hover:file:bg-amber-50
            hover:file:text-amber-700
          "/>
        </div>
      </main>
    </div>
  );
}

export default App;
