function sendMessage(){

let input = document.getElementById("userInput").value

let messages = document.getElementById("messages")

messages.innerHTML += "<p><b>You:</b> " + input + "</p>"

let response = analyseCase(input)

messages.innerHTML += "<p><b>Bot:</b> " + response + "</p>"

document.getElementById("userInput").value = ""

}

function analyseCase(text){

text = text.toLowerCase()

if(text.includes("penetration"))
return "Possible offence: Section 3/4 POCSO (Penetrative Sexual Assault)"

if(text.includes("child") && text.includes("touch"))
return "Possible offence: Section 7/8 POCSO (Sexual Assault)"

if(text.includes("teacher") || text.includes("authority"))
return "Aggravating factor detected. May fall under Section 5 (Aggravated Penetrative Sexual Assault)"

return "Insufficient facts. Please provide more case details."

}
