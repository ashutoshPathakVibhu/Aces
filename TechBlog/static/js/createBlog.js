$(function() {
    $(".bcontent").wysihtml5({
      toolbar: {
        "image": false
      }
    });
    
    $(document).on('change', '.btn-file :file', function() {
      var input = $(this);
      var numFiles = input.get(0).files ? input.get(0).files.length : 1;
      console.log(input.get(0).files);
      var label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
      input.trigger('fileselect', [numFiles, label]);
    });
    
    $('.btn-file :file').on('fileselect', function(event, numFiles, label){
      var input = $(this).parents('.input-group').find(':text');
      var log = numFiles > 1 ? numFiles + ' files selected' : label;
      
      if( input.length ) {
        input.val(log);
      } else {
        if( log ){ alert(log); }
      }
      
    });
  });