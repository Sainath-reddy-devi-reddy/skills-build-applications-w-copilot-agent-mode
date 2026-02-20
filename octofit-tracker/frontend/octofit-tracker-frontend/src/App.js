
import logo from './logo.svg';
import octofitLogo from './octofitapp-small.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <nav className="App-nav">
        <img src={octofitLogo} className="Octofit-logo" alt="Octofit Tracker Logo" />
        <span style={{ fontWeight: 700, fontSize: '1.5rem', color: '#fff', letterSpacing: '1px', marginRight: '2rem' }}>OctoFit Tracker</span>
        <a href="#home">Home</a>
        <a href="#profile">Profile</a>
        <a href="#teams">Teams</a>
        <a href="#leaderboard">Leaderboard</a>
        <a href="#workouts">Workouts</a>
      </nav>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Welcome to OctoFit Tracker!</h1>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
