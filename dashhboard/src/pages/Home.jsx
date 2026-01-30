
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div >
      <div><p>Welcome to Drishti: The Ultimate eye</p></div>
      <button type="button">
        <Link to="/dashboard">Goto Dashboard</Link>
      </button>
    </div>
  );
};

export default Home;
