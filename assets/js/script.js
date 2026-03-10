document.addEventListener('DOMContentLoaded', () => {
    // Set the current year
    const yearSpan = document.getElementById('year');
    if (yearSpan) yearSpan.textContent = new Date().getFullYear();

    // Live Clock Function
    function updateClock() {
        const clockElement = document.getElementById('clock-display');
        if (clockElement) {
            const now = new Date();
            clockElement.textContent = "Campus Time: " + now.toLocaleTimeString();
        }
    }

    setInterval(updateClock, 1000);
    updateClock();
});