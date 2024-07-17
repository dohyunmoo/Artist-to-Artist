function sendArtistInfo(chosenArtist) {
    const artistName = chosenArtist.getAttribute("artistName");
    const artistUrl = chosenArtist.getAttribute("imageUrl");

    fetch("/game", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            name: artistName,
            url: artistUrl,
            confirm: "1"
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("response: ", data);
    })
    .catch(error => {
        console.error("Error: ", error);
    });
}


function start() {
    const startArtist = document.getElementById("start-input");
    const targetArtist = document.getElementById("target-input");

    fetch("/game", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            name: [startArtist.value, targetArtist.value],
            url: "",
            confirm: "0"
        })
    })
    .then(response => {
        console.log(response.text());
    })
    .catch(error => {
        console.error("Error: ", error);
    });
}