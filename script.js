# script.js - JavaScript for fetching study materials

function fetchMaterial() {
    let selectedClass = document.getElementById("classSelect").value;
    let selectedRegion = document.getElementById("regionSelect").value;
    
    fetch(`/get_material?class=${selectedClass}&region=${selectedRegion}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("content").innerHTML = data.content;
        })
        .catch(error => console.error("Error fetching data:", error));
}
