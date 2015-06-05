var myCodeMirror = CodeMirror(document.getElementById("editor"), {

  value: ["var placeholder = ",
          "'text'"].join("\n"),
  mode:  {name: "python"},
  lineNumbers: true,
  gutters: ["CodeMirror-lint-markers"],
  // lint: true,
  theme: "solarized dark",
  autoCloseBrackets: true,
  matchBrackets: true
});

function loadProblems() {
  var indexURL = "https://api.github.com/repos/Grae-Drake/Python_Euler/contents/";
  var repoData = $.get(indexURL, function() {

    var responseText = JSON.parse(repoData["responseText"]);
    var problemList = [];
    for (var i = 0 ; i < responseText.length ; i++) {
      if (responseText[i]["name"].indexOf("Problem") > -1) {
        problemList.push(responseText[i]["name"]);
      }
    }

    for (var i = 0 ; i < problemList.length ; i++) {
      $(".problem-selector").append(
        ["<button data-problemName='",
        problemList[i],
        "'>",
        problemList[i].split("_").pop().split(".")[0],
        "</button>"].join("")
        );
    }
    
    myCodeMirror.setValue("Choose a problem to display..."));

  });
});

$(document).ready(function (){

  loadProblems()

  $(".CodeMirror").on("click", function() {
    console.log(myCodeMirror.getValue());
  });

  $(".problem-selector").on("click", "button", function(){

    var problemPath = ["Python_Euler", "/", this.getAttribute("data-problemName")].join("");
    console.log(problemPath);
    var problemData = $.get(problemPath, function() {
      console.log(problemData["responseText"]);
      myCodeMirror.setValue(problemData["responseText"]);
    });

  });

  $("button[name='Index']").on("click", function(){



});