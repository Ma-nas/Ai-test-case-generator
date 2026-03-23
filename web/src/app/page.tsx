'use client';

import { useState } from 'react';
import { Play, Code2, BugPlay, ShieldCheck, FileCheck2, Loader2, Copy, CheckCircle2 } from 'lucide-react';

export default function Home() {
  const [code, setCode] = useState('');
  const [apiKey, setApiKey] = useState('');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [copied, setCopied] = useState(false);

  const handleGenerate = async () => {
    if (!code.trim()) {
      setError('Please enter some Python code to test.');
      return;
    }
    
    setLoading(true);
    setError('');
    setOutput('');

    try {
      const response = await fetch('/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code, apiKey }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Something went wrong');
      }

      setOutput(data.result);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleCopy = () => {
    if (!output) return;
    navigator.clipboard.writeText(output);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <main className="container">
      <header>
        <h1>AI Test Case Generator</h1>
        <p className="subtitle">
          Instantly generate robust pytest assertions, edge cases, and boundary checks from your Python logic using Google GenAI.
        </p>
      </header>

      <div className="workspace">
        {/* Left Side: Input */}
        <div className="glass-panel editor-section">
          <div className="section-title">
            <Code2 className="text-accent" />
            <span>Python Source Code</span>
          </div>
          
          <textarea
            className="input-area"
            placeholder="# Paste your python function or code here...&#10;def divide(a, b):&#10;    if b == 0:&#10;        raise ValueError('Cannot divide by zero')&#10;    return a / b"
            value={code}
            onChange={(e) => setCode(e.target.value)}
          />

          <div className="controls">
            <input
              type="password"
              placeholder="Gemini API Key (Optional if configured)"
              value={apiKey}
              onChange={(e) => setApiKey(e.target.value)}
            />
            <button 
              className="btn" 
              onClick={handleGenerate}
              disabled={loading || !code.trim()}
            >
              {loading ? (
                <>
                  <Loader2 className="btn-icon spin" />
                  Generating...
                </>
              ) : (
                <>
                  <Play className="btn-icon" />
                  Generate Tests
                </>
              )}
            </button>
          </div>
        </div>

        {/* Right Side: Output */}
        <div className="glass-panel editor-section">
          <div className="section-title">
            <ShieldCheck className="text-accent" />
            <span>Generated Test Suite</span>
          </div>
          
          <div className="output-area">
            {loading ? (
              <div className="output-placeholder">
                <BugPlay size={48} className="spin text-accent" />
                <p>Analyzing logic and formatting tests...</p>
              </div>
            ) : error ? (
              <div className="output-placeholder error-text">
                <p>{error}</p>
              </div>
            ) : output ? (
              <>
                <button className="copy-btn" onClick={handleCopy} title="Copy Code">
                  {copied ? <CheckCircle2 size={18} className="text-success" /> : <Copy size={18} />}
                </button>
                <pre>{output}</pre>
              </>
            ) : (
              <div className="output-placeholder">
                <FileCheck2 size={48} />
                <p>Your generated pytest suite will appear here.</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </main>
  );
}
