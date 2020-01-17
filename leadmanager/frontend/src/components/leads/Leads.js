import React, { Component } from 'react';

export class Leads extends Component {
	render() {
		let usernames = [
			{
				username: 'test...'
			}
		];
		let name = 'nice';
		console.log('running...');
		fetch('http://localhost:8000/api/users.json')
			.then(function(response) {
				if (response.status !== 200) {
					console.log(
						'Looks like there was a problem. Status Code: ' + response.status
					);
					return;
				}

				// Examine the text in the response
				response.json().then(function(data) {
					console.log(data[0].username);
					usernames = data;
					console.log(usernames[0].username);
				});
			})
			.catch(function(err) {
				console.log('Fetch Error :-S', err);
			});
		return (
			<div>
				<h1>Users List</h1>
				{/* <h1>{usernames[0].username}</h1> */}
				<h1>{name}</h1>
			</div>
		);
	}
}

export default Leads;
