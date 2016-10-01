CKEDITOR.editorConfig = function( config ) {
    config.toolbar = [
        { name: 'clipboard', items: ['Undo', 'Redo' ] },
        { name: 'links', items: [ 'Link', 'Unlink' ] },
        { name: 'insert', items: [ 'Image', 'Table', 'HorizontalRule', 'SpecialChar' ] },
        { name: 'tools', items: [ 'Maximize' ] },
        { name: 'basicstyles', items: [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat' ] },
        { name: 'paragraph', items: [ 'NumberedList', 'BulletedList', '-', 'Blockquote' ] }
    ];
    config.enterMode = CKEDITOR.ENTER_BR;
    config.autoParagraph = false;
};
