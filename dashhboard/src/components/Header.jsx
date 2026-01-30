import { Link } from "react-router-dom";


const Header = () => {
    return (
        <nav className="header">
          <div>
            <h2>Drishti</h2>
          </div>
          <article>
            <Link to={"/"}>Home</Link>
            <Link to={"/dashboard"}>Dashboard</Link>

          </article>
        </nav>
      );
}

export default Header