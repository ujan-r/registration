const cardList = document.getElementById("classCards");
const searchBar = document.getElementById("search-bar")

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
    let key = `${c.subject} ${c.code} ${c.title}`;
    if (!seen[key]) {
        seen[key] = true;
        return true;
    }
})

let visibleCourses = courses;

let colors = new Map();
courses.forEach(course => {
    let R = Math.floor((Math.random() + 3) / 4 * 245);
    let G = Math.floor((Math.random() + 3) / 4 * 245);
    let B = Math.floor((Math.random() + 3) / 4 * 245);
    let color = (R << 16 | G << 8 | B).toString(16);
    colors.set(course, `#${color}`);
});

function updateCards() {
    classCards.innerHTML = "";
    visibleCourses.forEach(c => {
        let li = document.createElement("li");
        li.className = "card";

        li.style.backgroundColor = colors.get(c);

        let hours = c.minHours === c.maxHours ?
                    `${c.minHours} ${c.minHours === 1 ? "credit" : "credits"}` :
                    `${c.minHours} to ${c.maxHours} credits`;

        li.innerHTML =
                `<p class="title"><strong>${c.title}</strong></p>
                <p class="code"><em>${c.subject} ${c.code}</em></p>
                <p class="credits">${hours}</p>`

        cardList.appendChild(li);
    });
}

function filterCourses() {
    let text = searchBar.value.toLowerCase();

    if (text === "") {
        visibleCourses = courses;
    } else {
        visibleCourses = courses.filter(course => `${course.subject} ${course.code} ${course.title}`.toLowerCase().includes(text));
    }

    updateCards();
}


updateCards();

searchBar.oninput = () => filterCourses();
