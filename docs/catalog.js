const table = document.getElementById("classTable");
const tbody = table.getElementsByTagName("tbody")[0];

function loadJSON(path) {
    let xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open("GET", path, async=false);
    xobj.send(null);
    return JSON.parse(xobj.responseText);
}

const classes = loadJSON("https://ujan-r.github.io/registration/classes.json");

let seen = Object.create(null);
const courses = classes.filter(c => {
    let key = `${c.subject} ${c.code}`;
    if (!seen[key]) {
        seen[key] = true;
        return true;
    }
})

let visibleCourses = courses;


function appendRow(subject, code, title) {
    let row = tbody.insertRow(table.rows.length - 1);
    let cells = [row.insertCell(), row.insertCell(), row.insertCell()];

    cells[0].appendChild(document.createTextNode(subject));
    cells[1].appendChild(document.createTextNode(code));
    cells[2].appendChild(document.createTextNode(title));
}

function updateTable() {
    clearTable();
    visibleCourses.forEach(c => {
        appendRow(c.subject, c.code, c.title);
    });
}

function clearTable() {
    tbody.innerHTML = "";
}

updateTable();
