function Book(title, author, year) {
  this.title = title;
  this.author = author;
  this.year = year;
  
  this.getSummary= function() {
    return `${this.title} was published by ${this.author} in ${this.year}`
  }
  
}

//Constructor initialization
let book1 = new Book('Javascrit' , 'John' , '2017');
let book2 = new Book('Javascript2' , 'Roman' , '2018');

console.log(book1.getSummary());
console.log(book2.getSummary());
