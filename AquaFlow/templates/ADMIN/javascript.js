const monthNames = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
];

let currentDate = new Date();

function renderCalendar() {
    const daysContainer = document.getElementById('days');
    const monthName = document.getElementById('month-name');
    const currentYear = currentDate.getFullYear();
    const currentMonth = currentDate.getMonth();
    
    // Corrected template literal syntax
    monthName.textContent = `${monthNames[currentMonth]} ${currentYear}`;
    
    const firstDay = new Date(currentYear, currentMonth, 1).getDay();
    const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
    const daysInPrevMonth = new Date(currentYear, currentMonth, 0).getDate();

    daysContainer.innerHTML = "";
    
    // Fill in days from the previous month
    for (let x = firstDay; x > 0; x--) {
        const day = document.createElement('div');
        day.classList.add('inactive');
        day.textContent = daysInPrevMonth - x + 1;
        daysContainer.appendChild(day);
    }
    
    // Fill in days of the current month
    for (let i = 1; i <= daysInMonth; i++) {
        const day = document.createElement('div');
        day.textContent = i;
        daysContainer.appendChild(day);
    }

    // Calculate the number of days needed to fill the last row
    const totalBoxes = firstDay + daysInMonth;
    const totalDaysInCalendar = 42; // 6 rows of 7 days
    const remainingBoxes = totalDaysInCalendar - totalBoxes; 
    
    // Fill in days from the next month
    for (let j = 1; j <= remainingBoxes; j++) {
        const day = document.createElement('div');
        day.classList.add('inactive');
        day.textContent = j;
        daysContainer.appendChild(day);
    }
}

function changeMonth(direction) {
    currentDate.setMonth(currentDate.getMonth() + direction);
    renderCalendar();
}

document.getElementById('prev').addEventListener('click', () => changeMonth(-1));
document.getElementById('next').addEventListener('click', () => changeMonth(1));

renderCalendar();
