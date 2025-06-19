let jsonData;
let currentDomainIndex = 0;
let currentTrackIndex = 0;
let currentHeaderIndex = 0;

function decodeBase64(str) {
    try {
        return atob(str);
    } catch (e) {
        return "[Invalid Base64]";
    }
}

function renderInformation(dataArray) {
    const totalDomains = dataArray.length;
    let totalUrls = 0;
    let totalVulnerable = 0;
    let totalPotential = 0;
    let totalNone = 0;

    dataArray.forEach(domain => {
        totalUrls += domain.endpoints.length;

        domain.endpoints.forEach(endpoint => {
            endpoint.payload_tests.forEach(test => {
                if (test.status === "V") {
                    totalVulnerable++;
                } else if (test.status === "P") {
                    totalPotential++;
                } else if (test.status === "N") {
                    totalNone++;
                }
            });
        });
    });

    document.querySelector(".count-domains").textContent = totalDomains;
    document.querySelector(".count-urls").textContent = totalUrls;
    document.querySelector(".count-vulnerable").textContent = totalVulnerable;
    document.querySelector(".count-potential").textContent = totalPotential;
    document.querySelector(".count-none").textContent = totalNone;
}

function renderTabs(data) {
    const tab1 = document.querySelector(".domain-tabs");
    tab1.innerHTML = "";
    data.forEach((_, i) => {
        const btn = document.createElement("button");
        btn.className = "green-box btn";
        btn.textContent = `D${i + 1}`;
        btn.addEventListener("click", () => {
            currentDomainIndex = i;
            currentTrackIndex = 0;
            currentHeaderIndex = 0;
            updateTabs();
            renderDomain();
        });
        tab1.appendChild(btn);
    });
    //updateTabs();
}

function updateTabs() {
    const tab1 = document.querySelector(".domain-tabs");
    const tab1Buttons = tab1.children;
    for (let i = 0; i < tab1Buttons.length; i++) {
        if (i === currentDomainIndex) {
            tab1Buttons[i].classList.add("white-box");
        } else {
            tab1Buttons[i].classList.remove("white-box");
        }
    }

    const tab2 = document.querySelector(".url-tabs");
    const tab2Buttons = tab2.children;
    for (let i = 0; i < tab2Buttons.length; i++) {
        if (i === currentTrackIndex) {
            tab2Buttons[i].classList.add("white-box");
        } else {
            tab2Buttons[i].classList.remove("white-box");
        }
    }

    const tab3 = document.querySelector(".header-tabs");
    const tab3Buttons = tab3.children;
    for (let i = 0; i < tab3Buttons.length; i++) {
        if (i === currentHeaderIndex) {
            tab3Buttons[i].classList.add("white-box");
        } else {
            tab3Buttons[i].classList.remove("white-box");
        }
    }
}

function renderTrackTabs(domainData) {
    const tab2 = document.querySelector(".url-tabs");
    tab2.innerHTML = "";
    domainData.endpoints.forEach((_, i) => {
        const btn = document.createElement("button");
        btn.className = "green-box btn";
        btn.textContent = `U${i + 1}`;
        btn.addEventListener("click", () => {
            currentTrackIndex = i;
            currentHeaderIndex = 0;
            updateTabs();
            renderDomain();
        });
        tab2.appendChild(btn);
    });
    updateTabs();
}

function renderHeaderTabs(endpointData) {
    const tab3 = document.querySelector(".header-tabs");
    tab3.innerHTML = "";
    endpointData.payload_tests.forEach((test, i) => {
        const btn = document.createElement("button");
        btn.classList.add("btn");

        if (test.status === "V") {
            btn.classList.add("red-box");
        } else if (test.status === "P") {
            btn.classList.add("orange-box");
        } else if (test.status === "N") {
            btn.classList.add("blue-box");
        }

        btn.textContent = `P${i + 1}`;
        btn.addEventListener("click", () => {
            currentHeaderIndex = i;
            updateTabs();
            renderDomain();
        });

        tab3.appendChild(btn);
    });

    updateTabs();
}

function renderDomain() {
    const domainData = jsonData.data[currentDomainIndex];
    const endpointData = domainData.endpoints[currentTrackIndex];
    const test = endpointData.payload_tests[currentHeaderIndex];

    document.querySelector(".info-domain").textContent = domainData.domain_name;
    document.querySelector(".info-endpoint").textContent = endpointData.url;
    document.querySelector(".info-payload").textContent = test.payload;

    document.querySelector(".response-header-initial").textContent =
        decodeBase64(test.result.original_response.header);
    document.querySelector(".response-header-final").textContent = decodeBase64(
        test.result.modified_response.header
    );
    document.querySelector(".response-body-output").textContent = decodeBase64(
        test.result.modified_response.content
    );

    renderTrackTabs(domainData);
    renderHeaderTabs(endpointData);
}

fetch("data/poisoning_result.json")
    .then(res => res.json())
    .then(data => {
        jsonData = data;
        renderInformation(data.data);
        renderTabs(data.data);
        renderDomain();
    });
