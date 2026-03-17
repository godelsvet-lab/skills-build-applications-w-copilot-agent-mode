import React from 'react';
import { Link, Navigate, Route, Routes } from 'react-router-dom';

import logo from './assets/octofitapp-small.png';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

const navItems = [
  { to: '/users', label: 'Users' },
  { to: '/teams', label: 'Teams' },
  { to: '/activities', label: 'Activities' },
  { to: '/workouts', label: 'Workouts' },
  { to: '/leaderboard', label: 'Leaderboard' },
];

function App() {
  return (
    <div className="app-shell min-vh-100">
      <header className="container py-4">
        <div className="brand-row d-flex align-items-center gap-3 mb-3">
          <img src={logo} alt="OctoFit logo" className="app-logo" />
          <div>
            <h1 className="display-6 fw-bold mb-1">OctoFit Tracker</h1>
            <p className="lead mb-0">Fitness tracking for teams and schools</p>
          </div>
        </div>

        <nav className="navbar navbar-expand-lg navbar-dark app-nav rounded-4 shadow-sm px-3">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            {navItems.map((item) => (
              <li className="nav-item" key={item.to}>
                <Link className="nav-link" to={item.to}>
                  {item.label}
                </Link>
              </li>
            ))}
          </ul>
        </nav>
      </header>

      <main className="container pb-5">
        <Routes>
          <Route path="/" element={<Navigate to="/users" replace />} />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
