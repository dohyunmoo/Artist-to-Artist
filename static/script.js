// const startButton = document.getElementById("game-start");
// const startInput = document.getElementById("start-input");
// const targetInput = document.getElementById("target-input");

// startButton.addEventListener("click", function() {

//     const startValue = startInput.value.trim();
//     const targetValue = targetInput.value.trim();

//     if (!startValue || !targetValue) {
//         console.error("Please enter both start and target values");
//         return;  // Exit the function if validation fails
//     }

//     fetch("/game", {
//         method: "POST",
//         headers: { "Content-Type": "application/json" },
//         body: JSON.stringify({
//             start_artist: startValue,
//             target_artist: targetValue
//         })
//     })
//     .then(response => response.json())
//     .then(data => {
//         console.log(data)
//     })
//     .catch(error => console.error(error));
// });
