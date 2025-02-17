function simplifyText(doctorNotes) {
    let replacements = {
        "hypertension": "high blood pressure",
        "myocardial infarction": "heart attack",
        "neoplasm": "tumor",
        "fracture": "broken bone",
        "benign": "non-cancerous",
        "malignant": "cancerous"
    };

    let simplifiedText = doctorNotes;

    Object.keys(replacements).forEach((key) => {
        let regex = new RegExp("\\b" + key + "\\b", "gi");
        simplifiedText = simplifiedText.replace(regex, replacements[key]);
    });

    return simplifiedText;
}

// Example usage
let doctorNotes = "The patient has a benign neoplasm and mild hypertension.";
console.log(simplifyText(doctorNotes));

function saveNotes() {
    let notes = document.getElementById("textInput").value;
    localStorage.setItem("doctorNotes", notes);
    alert("Notes saved successfully!");
}

document.getElementById("saveBtn").addEventListener("click", saveNotes);

function downloadNotes() {
    let notes = document.getElementById("textInput").value;
    let blob = new Blob([notes], { type: "text/plain" });
    let link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "Doctor_Notes.txt";
    link.click();
}
// Add this to the Save button
document.getElementById("saveBtn").insertAdjacentHTML("afterend", '<button id="downloadBtn">📥 Download Notes</button>');
document.getElementById("downloadBtn").addEventListener("click", downloadNotes);


// Load saved notes when the page loads
document.addEventListener("DOMContentLoaded", () => {
    let savedNotes = localStorage.getItem("doctorNotes");
    if (savedNotes) {
        document.getElementById("textInput").value = savedNotes;
    }
});
