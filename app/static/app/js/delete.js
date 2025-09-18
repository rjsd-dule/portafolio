function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

export function deleteItem(endpoint, id) {
    if (!confirm(`¿Seguro que desea eliminar este registro ${id}?`)) return;

    const csrftoken = getCookie('csrftoken');

    fetch(`/${endpoint}/${id}/delete/`, {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken,
            "Content-Type": "application/json",
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert(data.message);
            const row = document.getElementById(`row-${id}`);
            if (row) row.remove();
        } else {
            alert(data.message || "Error al eliminar el registro");
        }
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Error al eliminar el registro");
    });
}

document.addEventListener("click", function (e) {
    const btn = e.target.closest(".delete-btn");
    if (btn) {
        e.preventDefault();
        const id = btn.dataset.id;
        const endpoint = btn.dataset.endpoint;
        deleteItem(endpoint, id);
    }
});


document.addEventListener("DOMContentLoaded", function () {
    const addBtn = document.getElementById("addnew");

    if (addBtn) {
        addBtn.addEventListener("click", function () {
            const endpoint = addBtn.dataset.endpoint; 
            window.location.href = `/${endpoint}/new/`; 
        });
    }
});
