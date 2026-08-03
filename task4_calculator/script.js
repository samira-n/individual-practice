document.addEventListener('DOMContentLoaded', () => {
    const num1 = document.getElementById('num1');
    const num2 = document.getElementById('num2');
    const resultDisplay = document.getElementById('resultDisplay');
    const buttons = document.querySelectorAll('.btn');

    function validateInputs() {
        const val1 = num1.value.trim();
        const val2 = num2.value.trim();
        
        if (val1 === '' || val2 === '') {
            resultDisplay.textContent = '❌ Введите оба числа!';
            resultDisplay.className = 'result-display error';
            return false;
        }
        
        if (isNaN(val1) || isNaN(val2)) {
            resultDisplay.textContent = '❌ Ошибка: введите числа!';
            resultDisplay.className = 'result-display error';
            return false;
        }
        
        return true;
    }

    function getNumbers() {
        return {
            a: parseFloat(num1.value),
            b: parseFloat(num2.value)
        };
    }

    function showResult(value) {
        if (typeof value === 'number' && !isNaN(value) && isFinite(value)) {
            resultDisplay.textContent = value;
            resultDisplay.className = 'result-display success';
        } else {
            resultDisplay.textContent = value;
            resultDisplay.className = 'result-display error';
        }
    }

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            if (!validateInputs()) return;
            
            const { a, b } = getNumbers();
            const operation = button.dataset.operation;
            let result;
            
            switch (operation) {
                case 'sum':
                    result = a + b;
                    break;
                case 'sub':
                    result = a - b;
                    break;
                case 'mul':
                    result = a * b;
                    break;
                case 'div':
                    if (b === 0) {
                        result = 'Деление на ноль!';
                    } else {
                        result = a / b;
                    }
                    break;
                default:
                    result = 'Неизвестная операция';
            }
            
            showResult(result);
        });
    });

    [num1, num2].forEach(input => {
        input.addEventListener('input', () => {
            if (resultDisplay.classList.contains('error')) {
                resultDisplay.textContent = '0';
                resultDisplay.className = 'result-display';
            }
        });
    });
});