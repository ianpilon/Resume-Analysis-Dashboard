async function startResearch() {
    const topic = document.getElementById('topic').value.trim();
    if (!topic) {
        showError('Please enter a research topic');
        return;
    }

    // Show loading state
    document.getElementById('loading').classList.remove('hidden');
    document.getElementById('result').classList.add('hidden');
    document.getElementById('error').classList.add('hidden');

    try {
        const response = await fetch('/research', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ topic }),
        });

        const data = await response.json();

        if (data.success) {
            showResult(data.result);
        } else {
            showError(data.error || 'An error occurred during research');
        }
    } catch (error) {
        showError('Failed to connect to the server');
    } finally {
        document.getElementById('loading').classList.add('hidden');
    }
}

function showResult(result) {
    const resultDiv = document.getElementById('result');
    const resultContent = document.getElementById('resultContent');
    
    // Convert the result text to HTML with proper formatting
    const formattedResult = result.replace(/\n\n/g, '<br><br>')
                                 .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    resultContent.innerHTML = formattedResult;
    resultDiv.classList.remove('hidden');
}

function showError(message) {
    const errorDiv = document.getElementById('error');
    const errorMessage = document.getElementById('errorMessage');
    errorMessage.textContent = message;
    errorDiv.classList.remove('hidden');
}
