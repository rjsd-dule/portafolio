$(document).ready(function() {
    const table = $('#dataTable').DataTable({
        responsive: true,
        scrollX: true,
        autoWidth: false,
        pageLength: 5,
        lengthMenu: [5, 10, 25, 50],
        language: {
            search: "",
            lengthMenu: "Mostrar _MENU_ registros",
            info: "Mostrando _START_ a _END_ de _TOTAL_",
            paginate: {
                first: "Primero",
                last: "Último",
                next: "›",
                previous: "‹"
            },
            emptyTable: "No hay registros aún"
        },
        dom: '<"top flex justify-between mb-2"lf>rt<"bottom"ip>',
    });

    $('#dataTable_filter input').attr('placeholder', 'Buscar ...');

    

});
