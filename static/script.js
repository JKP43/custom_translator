// Function to resize textarea based on its content
function autoResizeTextarea() {
    const textarea = document.getElementById('textToTranslate');
    textarea.style.height = 'auto'; // Reset the height to auto to recalculate
    textarea.style.height = textarea.scrollHeight + 'px'; // Set the height to the scroll height
}

// Event listener for textarea input to resize automatically
document.getElementById('textToTranslate').addEventListener('input', autoResizeTextarea);

// Submit handler for the translation form
document.getElementById('translateForm').addEventListener('submit', async (event) => {
    event.preventDefault();
    
    const textToTranslate = document.getElementById('textToTranslate').value;
    const fromLanguage = document.getElementById('fromLanguage').value;
    const toLanguage = document.getElementById('toLanguage').value;
    
    const response = await fetch('/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: textToTranslate, from_language: fromLanguage, to_language: toLanguage })
    });
    
    const result = await response.json();
    document.getElementById('translatedText').innerHTML = `<pre>${result.translated_text}</pre>`;
    
    // Automatically resize textarea after translation if needed
    autoResizeTextarea();
    
});

// Event listener for the download button
document.getElementById('downloadButton').addEventListener('click', async (event) => {
    event.preventDefault();

    // Send a GET request to the /download route
    const response = await fetch('/download');
    const blob = await response.blob();

    // Create a temporary download link and click it programmatically
    const downloadLink = document.createElement('a');
    downloadLink.href = URL.createObjectURL(blob);
    downloadLink.download = '/tmp/translated_text.txt';
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
});

// // Event listener for the download button
// document.getElementById('downloadButton').addEventListener('click', (event) => {
//     event.preventDefault();

//     const translatedText = document.getElementById('translatedText').innerText;
//     const blob = new Blob([translatedText], {type: "text/plain;charset=utf-8"});
//     const url = URL.createObjectURL(blob);

//     // Create a temporary download link and click it programmatically
//     const downloadLink = document.createElement('a');
//     downloadLink.href = url;
//     downloadLink.download = 'translated_text.txt';
//     document.body.appendChild(downloadLink);
//     downloadLink.click();
//     document.body.removeChild(downloadLink);
// });
