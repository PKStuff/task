/*
factory method to create an Object:
*/

function create(name) {
	return {
		name: name,
		print: function () {
			document.write("Hi " + name + " Object successfully created!");
		},
	};
}

const add = create('Alexa');
add.print();
