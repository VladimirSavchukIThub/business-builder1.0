document.addEventListener('DOMContentLoaded', function() {
    const plotSelect = document.getElementById('plot-select');
    const businessTypeSelect = document.getElementById('business-type-select');

    // Получаем данные участков
    fetch('/get_plots')
        .then(response => response.json())
        .then(data => {
            data.forEach(plot => {
                let option = document.createElement('option');
                option.value = plot.id;
                option.textContent = `${plot.name} - ${plot.location} (${plot.size})`;
                plotSelect.appendChild(option);
            });
        });

    // Получаем данные типов бизнеса
    fetch('/get_business_types')
        .then(response => response.json())
        .then(data => {
            data.forEach(business => {
                let option = document.createElement('option');
                option.value = business.id;
                option.textContent = business.name;
                businessTypeSelect.appendChild(option);
            });
        });

    // Обработка нажатия кнопки "Перейти к конфигуратору"
    document.getElementById('config-btn').addEventListener('click', function() {
        const selectedPlot = plotSelect.value;
        const selectedBusinessType = businessTypeSelect.value;

        alert(`Вы выбрали участок с ID: ${selectedPlot} и тип бизнеса: ${selectedBusinessType}`);
    });
});
