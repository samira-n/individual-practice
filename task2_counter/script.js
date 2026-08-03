document.addEventListener('DOMContentLoaded', () => {
    const counterDisplay = document.getElementById('counterDisplay');
    const plusBtn = document.getElementById('plusBtn');
    const minusBtn = document.getElementById('minusBtn');
    const messageBox = document.getElementById('messageBox');
    
    let count = 0;
    const MAX_VALUE = 10;
    const MIN_VALUE = -10;

    function updateUI() {
        counterDisplay.textContent = count;
        
        counterDisplay.className = 'counter-display';
        if (count > 0) {
            counterDisplay.classList.add('positive');
        } else if (count < 0) {
            counterDisplay.classList.add('negative');
        } else {
            counterDisplay.classList.add('zero');
        }
        
        plusBtn.disabled = (count >= MAX_VALUE);
        minusBtn.disabled = (count <= MIN_VALUE);
        
        if (count === MAX_VALUE || count === MIN_VALUE) {
            messageBox.textContent = 'Вы достигли экстремального значения!';
            messageBox.classList.add('show');
        } else {
            messageBox.textContent = '';
            messageBox.classList.remove('show');
        }
    }

    plusBtn.addEventListener('click', () => {
        if (count < MAX_VALUE) {
            count++;
            updateUI();
        }
    });

    minusBtn.addEventListener('click', () => {
        if (count > MIN_VALUE) {
            count--;
            updateUI();
        }
    });

    updateUI();
});