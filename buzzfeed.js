(function questions(){

  var questions = [
    {
      "question": "What animal would be your spirit guide?",
      "name": "animal",
      "answers" : {
        "Lion Turtle": 25,
        "Earth Mole": 20,
        "Sky Bison": 15,
        "Dragon": 10
      }
    },
    {
      "question": "What is your favorite color?",
      "name": "colors",
      "answers" : {
        "Blue": 25,
        "Green": 20,
        "Yellow": 15,
        "Red": 10
      }
    },
    {
      "question": "What word would you use to describe yourself?",
      "name": "word",
      "answers" : {
        "Adaptable": 25,
        "Resilient": 20,
        "Care free": 15,
        "Stubborn": 10
      }
    },
    {
      "question": "Who's your favorite superhero?",
      "name": "hero",
      "answers" : {
        "Batman": 25,
        "Wonder Woman": 20,
        "Superman": 15,
        "Black Widow": 10
      }
    },
    {
      "question": "If you could choose, which element would you bend?",
      "name": "element",
      "answers" : {
        "Water": 10,
        "Earth": 15,
        "Air": 20,
        "Fire": 25
      }
    }
  ];

  var html = "";
  for (var i = 0; i < questions.length; i++){
    html += questions[i]["question"] + "<br>";
    for (var key in questions[i]["answers"]){
      html += '<input type="radio" name="' + questions[i]["name"] + '" value="';
      html += questions[i]["answers"][key] + '">' + key + "<br>";
    }
  }

  /* TODO: set the element "survey" 's innerHTML to html'*/
  document.getElementById("quiz").innerHTML = html;
})();

function tacobell(){
  var total = 0;
  var categories = ["animal", "colors", "word", "hero", "element"];

  /* TODO:  Determine your winning "personality" */

for (var j = 0; j < categories.length; j++){
  var cat = document.getElementsByName(categories[j]);
  for (var i = 0; i < cat.length; i++){
    if (cat[i].checked){
      total += parseInt(cat[i].value);
    }
  }
}

var bender;
if (total >= 80) {
    bender = "Water Bender";
} else if (total > 65 && total < 79){
    bender = "Earth Bender";
} else if (total > 50 && total < 64){
    bender = "Air Bender";
} else if (total < 49){
    bender = "Fire Bender";
} else {
  bender = "na";
}
alert(bender);
  /*TODO: Replace the empty quotes with the result of the quiz*/
  document.getElementById("results").innerHTML = "YOU ARE A "  + bender.toUpperCase();
}
