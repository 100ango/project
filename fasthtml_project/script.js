const container = document.getElementById("code-wrapper");
const copyButton = document.getElementById("copy-button");
const tick = document.getElementById("check");
const range = document.createRange();

copyButton.addEventListener("click", handleImageClick);

function handleImageClick(event) {

 

    tick.style.display = "inline";
    try{
        document.execCommand("copy");
    }catch(err) {
        console.error("Unable to copy text:", err);
    }

    setTimeout(function() {
        tick.style.display = "none";
    }, 3000);
}