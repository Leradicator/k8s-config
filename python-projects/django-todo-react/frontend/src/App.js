import React, { Component } from "react";
import Fighters from "./Components/Fighters";

import { useQuery, gql } from '@apollo/client';

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
