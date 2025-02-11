function getCurrentSemester() {
    const currentDate = new Date();
    
    const semesters = [
        { start: new Date(2023, 8, 2), end: new Date(2023, 11, 18), num: 1 },
        { start: new Date(2024, 1, 2), end: new Date(2024, 5, 18), num: 2 },
        { start: new Date(2024, 8, 2), end: new Date(2024, 11, 18), num: 3 },
        { start: new Date(2025, 1, 2), end: new Date(2025, 5, 18), num: 4 },
        { start: new Date(2025, 8, 2), end: new Date(2025, 11, 18), num: 5 },
        { start: new Date(2026, 1, 2), end: new Date(2026, 5, 18), num: 6 },
        { start: new Date(2026, 8, 2), end: new Date(2026, 11, 18), num: 7 },
        { start: new Date(2027, 1, 2), end: new Date(2027, 5, 18), num: 8 },
        { start: new Date(2027, 8, 2), end: new Date(2027, 11, 18), num: 9 },
        { start: new Date(2028, 1, 2), end: new Date(2028, 5, 18), num: 10 },
    ];
    
    for (let sem of semesters) {
        if (currentDate >= sem.start && currentDate <= sem.end) {
            return sem.num;
        }
    }
    
    for (let sem of semesters) {
        if (currentDate < sem.start) {
            return `Break before Semester ${sem.num}`;
        }
    }
    
    return "No semester found";
}

module.exports = getCurrentSemester;