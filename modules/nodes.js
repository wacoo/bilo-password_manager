function createElement(type, cls, id) {
    const element = document.createElement(type);
    if(cls) {
        for(let i = 0; i < cls.length; i += 1) {
            element.classList.add(cls[i]);
        }        
    }
    if(id) {
        element.id = id;
    }
        
    return element;    
}


function createBox(parent, data,idx) {
    const topBar = createElement('div', ['top-bar'], null);
    const h3 = createElement('h3', null, null);
    const cred_wrapper = createElement('div', ['cred_wrapper'], null);
    h3.innerHTML = data.title[idx];

    topBar.appendChild(h3);
    parent.appendChild(topBar);
    console.log(data);
    for(let i = 0; i < 3; i += 1) {
        const box = createElement('div', ['box'], null);
        const img = createElement('img', null, null);
        const p = createElement('p', null, null);

        img.src = data.image[idx];
        if (idx === 0) {
            p.innerHTML = data.result.credentials[0].url;
        } else {
            p.innerHTML = data.result.notes['22'][1];
        }
        

        box.appendChild(img);
        box.appendChild(p);
        cred_wrapper.appendChild(box);        
    }
    parent.appendChild(cred_wrapper);
}

export { createBox };
    