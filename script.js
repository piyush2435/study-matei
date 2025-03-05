function fetchMaterial() {
    let selectedClass = document.getElementById("classSelect").value;
    
    fetch(`/get_material?class=${selectedClass}`)
        .then(response => response.json())
        .then(data => {
            let contentDiv = document.getElementById("content");
            contentDiv.innerHTML = ""; // Clear old content
            
            if (data.files.length === 0) {
                contentDiv.innerHTML = "<p>No study materials available.</p>";
            } else {
                data.files.forEach(file => {
                    let link = document.createElement("a");
                    link.href = file;
                    link.innerText = file.split("/").pop();
                    link.target = "_blank";
                    link.style.display = "block";
                    contentDiv.appendChild(link);
                });
            }
        })
        .catch(error => console.error("Error fetching data:", error));
}
