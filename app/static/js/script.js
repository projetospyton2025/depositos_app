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
            element.classList.add('clicked');
            location.reload();
        }
    });
}
