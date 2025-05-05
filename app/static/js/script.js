async function getJson(file_name) {
    const response = await fetch(`../static/data/${file_name}.json`);
    const jsonData = await response.json();
    return jsonData;
  }

async function AiResponse() {
    userInput = document.getElementById('prompt').value;
    document.getElementById('prompt').value = '' 
    addMessages()
    
    // Send a POST request to the Flask route
    const response = await fetch('/prompt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ input: userInput })
    });
    
    // Get the response from the server
    AI_RESPONSE = await response.json();
    await passAiMessage();
    passAiFunctions();
}

function addMessages() {
    
    userMessage = `
        <div class="item right">
            <div class="msg">
                <p>${userInput}</p>
            </div>
        </div>
    `;

    aiMessage = `
        <div class="item">
            <div class="icon">
                <img src="../static/icon/user-icon.png" alt="User Icon">
            </div>
            <div class="msg">
                <p class = "ai-message">...</p>
            </div>
        </div>
    `;

    // Seleciona o container onde as mensagens serão adicionadas
    BOX = document.querySelector('.box');
    // Adiciona as mensagens ao container
    BOX.innerHTML += userMessage;
    BOX.innerHTML += aiMessage;
    BOX.scrollTop = BOX.scrollHeight;
}

function passAiMessage() {
    return new Promise((resolve) => {
        const aiMessages = document.querySelectorAll('.ai-message');
        aiMessage = aiMessages[aiMessages.length - 1];
        aiMessage.innerHTML = "";
        
        for (let i = 0; i < AI_RESPONSE.response.length; i++) {
            setTimeout(() => {
                aiMessage.innerHTML += AI_RESPONSE.response[i];
                BOX.scrollTop = BOX.scrollHeight;
                
                // Resolve the promise when the last character is added
                if (i === AI_RESPONSE.response.length - 1) {
                    resolve();
                }
            }, 10 * i);
        }
    });
};

function passAiFunctions() {
    BUTTONS = document.querySelector('.responseItem');
    BUTTONS.innerHTML = "";
    getJson("botOptions").then(data => {
        limitFunc = 1
        AI_RESPONSE.function.forEach(aiFunc => {
            if (Object.keys(data).includes(aiFunc) && limitFunc <= 3) {
                limitFunc += 1
                // alert(aiFunc); // debugging
                // alert(data[aiFunc][1]); // debugging
                
                funcButton = `<a class="response" target="_blank" href="${data[aiFunc][2]}">${data[aiFunc][0]}</a>`
                BUTTONS.innerHTML += funcButton;
            }
        });
    });
};

// const selectLang = (language) => {
//     if (language == "pt-BR") {
//         document.documentElement.setAttribute("lang", "pt-BR");
//         document.getElementById('prompt').placeholder = "Digite sua dúvida...";
//     } else {
//         document.documentElement.setAttribute("lang", "en");
//         document.getElementById('prompt').placeholder = "Type your question...";
//     }
// }

// window.onload = () => {
//     selectLang(navigator.language);
// };
