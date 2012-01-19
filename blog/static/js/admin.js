$(document).ready(function() {
    $("textarea").ckeditor({
			  toolbar :
			  [
            ['Bold', 'Italic', '-', 'Link', 'Unlink','-', 'Image'],
			  ],
        filebrowserBrowseUrl : '/images/',
        filebrowserUploadUrl : '/images/new/'
    });

    // Only do this if we're adding a new one
    if (document.location.pathname.indexOf('add') != -1) {
        $("select#id_author option[selected]").removeAttr("selected");
        $("select#id_author option[value=" + user_id + "]").attr("selected", "selected");
    }
});

