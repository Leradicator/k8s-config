import React, { Component } from "react";
import Fighters from "./Components/Fighters";

class App extends Component {

  render() {
    return (
      <main className="container">
        <h1>Fighting Game</h1>
        <Fighters />
      </main>
    );
  }
}

export default App;
