import React, { Component } from 'react';
import { gql, useQuery } from '@apollo/client';

const GET_FIGHTERS = gql`

query {
  allFighters {
    edges {
      node {
        id
        name
        weapon {
          id
          name
          targetType
        }
        group {
          id
          name
        }
        
      }
    }
  }
}

`;

function DisplayFighters() {

    const { loading, error, data } = useQuery(GET_FIGHTERS);
  
  
    if (loading) return <p>Loading...</p>;
  
    if (error) return <p>Error :(</p>;
  
    console.log(data);
  
    return data.allFighters.edges.map(({ node}) => (
  
      <div key={node.id}>
  
        <p><u>{node.name}</u> from group
          <strong> {node.group.name} </strong>
          using <u>{node.weapon.name} </u>
          with target type <strong>{node.weapon.targetType}</strong></p>
  
        <br />
  
        <br />
  
      </div>
  
    ));
  
  };

export class Fighters extends Component {
  render() {
    return (
      <div>
        <DisplayFighters />
      </div>
    )
  }
};

export default Fighters
