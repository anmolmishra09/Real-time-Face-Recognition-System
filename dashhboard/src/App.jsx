import './App.css'
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { Toaster} from "react-hot-toast";
import Header from './components/Header';
import Home from './pages/Home';
import Dashboard from './pages/Dashboard';

function App() {

  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
      </Routes>
      <Toaster />
    </Router>
  );
}

export default App
