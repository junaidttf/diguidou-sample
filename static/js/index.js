$(document).ready(function () {
    const dropdownMenu = $(".dropdown-menu");
    const dropdown = $(".dropdown");
    const dropdownIcon = $(".dropdown-icon");
    const selectedValueDisplay = $(".selected-v");
    const selectedSortValueDisplay = $(".selected-sort");

    dropdownIcon.on("click", function (event) {
        if (dropdownMenu.hasClass("show")) {
            dropdownIcon.find('#arrow-open').removeClass('d-none')
            dropdownIcon.find('#arrow-close').addClass('d-none')
        } else {
            dropdownIcon.find('#arrow-close').removeClass('d-none')
            dropdownIcon.find('#arrow-open').addClass('d-none')
        }
        event.stopPropagation();
    });

    dropdownMenu.on("click", ".dropdown-item", function (event) {
        if ($(this).parents('.dropdown-menu').hasClass('selectedSortValueDisplay')) {
            selectedSortValueDisplay.html($(this).html());
        } else {
            selectedValueDisplay.html($(this).html());
        }
        dropdownIcon.find('#arrow-close').removeClass('d-none')
        dropdownIcon.find('#arrow-open').addClass('d-none')
    });

    $(document).on("click", function (event) {
        if (!dropdown.has(event.target) && dropdownMenu.hasClass("show")) {
            dropdownIcon.find('#arrow-close').removeClass('d-none')
            dropdownIcon.find('#arrow-open').addClass('d-none')
        }
    });
});
