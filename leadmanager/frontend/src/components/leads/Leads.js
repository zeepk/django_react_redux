import React, { Component } from 'react';

export class Leads extends Component {
	render() {
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
					console.log(data);
				});
			})
			.catch(function(err) {
				console.log('Fetch Error :-S', err);
			});
		return (
			<div>
				<h1>Leads List</h1>
				<h1>Leads List</h1>
				<h1>{data}</h1>
			</div>
		);
	}
}

export default Leads;
