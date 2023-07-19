function deleteNote(noteId){
    fetch("/delete-note">{
        method: "POST",
        body: JSON.stringify({noteId: noteId})
    }).then((_res) => {
        window.location.href = "/"
    })
}

function copyTextValue() {
    var e = document.getElementById("index-disciplinas");
    var val = e.options[e.selectedIndex].value;
    document.getElementById("curso").value = val;
}