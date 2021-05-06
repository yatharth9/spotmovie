// /* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
// function openNav() {
//   document.getElementById("mySidebar").style.width = "250px";
//   document.getElementById("main").style.marginLeft = "250px";
// }

// /* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
// function closeNav() {
//   document.getElementById("mySidebar").style.width = "0";
//   document.getElementById("main").style.marginLeft = "0";
// }
var obj = JSON.parse('[{"tconst": "tt8655594", "href_movie": "https://www.imdb.com/title/tt8655594/", "Name": "The Mongolian Connection", "Genres": "Action", "Year": "2019", "Poster": "https://m.media-amazon.com/images/M/MV5BMDMyNTYwODctMGFiNi00ODFhLWIyNjUtNzNkYjk2ZjY5YjQ1XkEyXkFqcGdeQXVyMjkyNTQ5MTA@._V1_UX182_CR0,0,182,268_AL__QL50.jpg"}, {"tconst": "tt10529130", "href_movie": "https://www.imdb.com/title/tt10529130/", "Name": "Bite Fight", "Genres": "Romance", "Year": "2016", "Poster": "https://m.media-amazon.com/images/M/MV5BNTI4MGZiM2EtMzMwMC00ODJhLWI2ZDQtZjFmZWIwY2ZhYWU0XkEyXkFqcGdeQXVyNDQwMDYzOTU@._V1_UY268_CR4,0,182,268_AL__QL50.jpg"}, {"tconst": "tt11265668", "href_movie": "https://www.imdb.com/title/tt11265668/", "Name": "KSI vs. Logan Paul II", "Genres": "Sport", "Year": "2019", "Poster": "https://m.media-amazon.com/images/M/MV5BYzIxODY0MTQtYWRhNS00M2U4LWEyOGUtYzlkM2IzZmJlMzFhXkEyXkFqcGdeQXVyOTAzODkzMjI@._V1_UY268_CR43,0,182,268_AL__QL50.jpg"}, {"tconst": "tt3400046", "href_movie": "https://www.imdb.com/title/tt3400046/", "Name": "El d�a fuera del tiempo", "Genres": "Crime", "Year": "2014", "Poster": "https://m.media-amazon.com/images/M/MV5BZGMzNDczZjItMGUwYi00MzU2LWFiMzYtNjVmNmVkMTkwYmI3XkEyXkFqcGdeQXVyMTY1NjI0Nzk@._V1_UY268_CR9,0,182,268_AL__QL50.jpg"}, {"tconst": "tt7297854", "href_movie": "https://www.imdb.com/title/tt7297854/", "Name": "Tomb Raider Legacy", "Genres": "Adventure", "Year": "2017", "Poster": "https://m.media-amazon.com/images/M/MV5BY2I5YWNjZGEtYmZiOC00YTllLTljNjEtM2YwZmJkZmVhNTZhXkEyXkFqcGdeQXVyNzk2NDAxOTQ@._V1_UY268_CR147,0,182,268_AL__QL50.jpg"}, {"tconst": "tt6851802", "href_movie": "https://www.imdb.com/title/tt6851802/", "Name": "Kuzhali", "Genres": "Action,Romance,Thriller", "Year": "2017", "Poster": "https://m.media-amazon.com/images/M/MV5BNDZhZmZiYjAtOTNmYy00M2ZjLWE4OWQtMjhlODdlOGQxNzkzXkEyXkFqcGdeQXVyMjg1NzI3MTg@._V1_UY268_CR3,0,182,268_AL__QL50.jpg"}, {"tconst": "tt1721677", "href_movie": "https://www.imdb.com/title/tt1721677/", "Name": "Fastest", "Genres": "Action,Documentary,Sport", "Year": "2011", "Poster": "https://m.media-amazon.com/images/M/MV5BMTg4NzQ3MjQ2OF5BMl5BanBnXkFtZTgwNTYwNTA2MDE@._V1_UY268_CR9,0,182,268_AL__QL50.jpg"}, {"tconst": "tt2076788", "href_movie": "https://www.imdb.com/title/tt2076788/", "Name": "A Onda da Vida", "Genres": "Adventure,Romance,Sport", "Year": "2011", "Poster": "https://m.media-amazon.com/images/M/MV5BMDBjNzFlOGEtY2QxZS00MTVjLTkzNGUtNjM5MWVhMzAyZTEwXkEyXkFqcGdeQXVyOTU3ODk4MQ@@._V1_UY268_CR9,0,182,268_AL__QL50.jpg"}]');

// var data = require('D:\Programs\templates\Try.json');
// // console.log(data);
// var obj = JSON.parse(data);
// // console.log(data);
// function readTextFile(file, callback) {
//     var rawFile = new XMLHttpRequest();
//     rawFile.overrideMimeType("application/json");
//     rawFile.open("GET", file, true);
//     rawFile.onreadystatechange = function() {
//         if (rawFile.readyState === 4 && rawFile.status == "200") {
//             callback(rawFile.responseText);
//         }
//     }
//     rawFile.send(null);
// }

// //usage:
// readTextFile("D:\Programs\templates\Try.json", function(text){
//     var data = JSON.parse(text);
//     console.log(data);
// });
//___________________________________________________________________________________________________________________________________________________________________
// function loadJSON(callback) {   

//     var xobj = new XMLHttpRequest();
//         xobj.overrideMimeType("application/json");
//     xobj.open('GET', 'D:\Programs\templates\Try.json', true); // Replace 'my_data' with the path to your file
//     xobj.onreadystatechange = function () {
//           if (xobj.readyState == 4 && xobj.status == "200") {
//             // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
//             callback(xobj.responseText);
//           }
//     };
//     xobj.send(null);  
//  }
// function init() {
//     loadJSON(function(response) {
//      // Parse JSON string into object
//        var obj = JSON.parse(response);
//     });
// //    }

// fetch('RedirectedOutput.json').then(function (response) {
//     return response.json();
// }).then(function (obj) {
//     console.log(obj);
// }).catch(function (error){
//     console.log("Data cannot be retrieved!");
//     console.error(error);
// });

// fetch('RedirectedOutput.json').then(function (response) {
//     return response.json();
// }).then(function (obj) {
//     for( var i=0; i<obj.length; i++) {
//         Append1(obj, i);
//         Append0(obj, i);
//         }
// }).catch(function (error) {
//     console.error("Data cannot be retrieved!");
//     console.error(error);
// }); 