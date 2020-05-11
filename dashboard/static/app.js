function toggle_hide_album(element, genre){
    if(document.getElementsByClassName("selected-chip").length === 0){
        toggle_hide_albums(true)
    }
    element.classList.toggle("selected-chip");
    let elements = document.getElementsByClassName("card")
    for (let element of elements){
        let genre_attribute = element.getAttribute("data-genres");
        if(genre_attribute.includes(genre)){
            element.classList.toggle("hidden-card");
        }
    }
    if(document.getElementsByClassName("selected-chip").length === 0){
        toggle_hide_albums(false)
    }
}    
  
function toggle_hide_albums(hide){
    let elements = document.getElementsByClassName("card")
    for (let element of elements){
        element.classList.toggle("hidden-card", hide);
    }
}