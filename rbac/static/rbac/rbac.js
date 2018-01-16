  $(function () {
        $(".item_title").click(function () {
            $(this).next().toggleClass("hide")
        });
    })