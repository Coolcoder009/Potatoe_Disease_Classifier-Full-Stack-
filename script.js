document.getElementById('customButton').addEventListener('click', function() {
    document.getElementById('imageInput').click(); // Trigger the file input click
});
async function uploadAndPredict() {
    const inputElement = document.getElementById('imageInput');
    if (inputElement.files.length === 0) {
        alert('Please select an image file first.');
        return;
    }

    const file = inputElement.files[0];
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('http://localhost:8000/predict/', {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            throw new Error(`Server responded with a status of ${response.status}`);
        }

        const result = await response.json();

        // Display result in a pop-up box
        const resultPopup = document.createElement('div');
        resultPopup.classList.add('result-popup');
        resultPopup.innerHTML = `
            <div class="popup-content">
                <span class="close-btn" onclick="closePopup()">&times;</span>
                <p>Prediction: ${result.class}</p>
                <button onclick="closePopup()">OK</button>
            </div>
        `;
        document.body.appendChild(resultPopup);
    } catch (error) {
        console.error("Failed to send data to the backend:", error);
        alert("Failed to send data to the backend. Please check the console for more details.");
    }
}

function closePopup() {
    const resultPopup = document.querySelector('.result-popup');
    if (resultPopup) {
        resultPopup.remove();
    }
}
