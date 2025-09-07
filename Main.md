
## Semester

```dataviewjs
var a = moment("2025-09-01"); // Semester start: September 1st, 2025
var b = moment("2025-12-19"); // Semester end: December 19th, 2025
var n = moment(); // Current moment
var t = moment().startOf('day'); // Today at start of day

let q = b.diff(a, 'days'); // Total days in semester
let p = b.diff(t, 'days'); // Days remaining from today
let r = t.diff(a, 'days'); // Days elapsed since start
let h = n.diff(a, 'hours'); // Hours elapsed since start
let i = b.diff(a, 'hours'); // Total hours in semester

let html = `<progress style="height:10px;width:80%" value="${h}" max="${i}"></progress>`;

if (r >= 0 && r <= q) {
    if (p > 0) {
        // Semester is ongoing
        html += `\n#### ${p} days left of ${q} days\n`;
        html += `${(h/i*100).toFixed(2)}% complete`;
    } else if (p === 0) {
        // Semester ends today
        html += `\n#### Semester ends today\n`;
        html += `${(h/i*100).toFixed(2)}% complete`;
    } else {
        // Semester has ended
        html += `\n#### Semester ended ${-p} days ago\n`;
        html += `100% complete`;
    }
} else if (r < 0) {
    // Before semester starts
    html += `\n#### ${-r} days to go until semester starts`;
}

dv.paragraph(html);
```



## Lectures

```dataview
table year, semester, Lecture
from "Lectures"
where contains(file.tags, "#Lecture")
```



## Assignments

```dataview
table year, semester
from "Lectures"
where contains(file.tags, "#Assignments")
```
