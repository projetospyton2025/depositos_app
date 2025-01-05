//# app/static/js/script.js
function toggleDeposit(element) {
    if (element.classList.contains('clicked')) return;

    const value = element.dataset.value;
    const index = element.dataset.index;

    fetch('/toggle_deposit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            value: value,
            index: index
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Adiciona a classe clicked ao elemento
            element.classList.add('clicked');
            
            // Atualiza o valor total
            fetch('/check_deposits')
                .then(response => response.json())
                .then(depositData => {
                    // Calcula o novo total
                    const deposits = depositData.deposits;
                    const total = Object.entries(deposits)
                        .filter(([_, value]) => value)
                        .reduce((sum, [key, _]) => sum + parseFloat(key.split('-')[0]), 0);
                    
                    // Atualiza a barra de progresso
                    const progressBar = document.querySelector('.progress-bar');
                    const percentage = (total / 10000) * 100;
                    progressBar.style.width = `${percentage}%`;
                    progressBar.textContent = `R$ ${total.toFixed(2)}`;
                    
                    // Atualiza o texto do total
                    const totalText = document.querySelector('.mt-2');
                    totalText.innerHTML = `Total depositado: R$ ${total.toFixed(2)} | Falta: R$ ${(10000 - total).toFixed(2)}`;
                });
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}