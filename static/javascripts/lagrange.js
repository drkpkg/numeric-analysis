$(function(){
    initValidate();
});

function initValidate(board){
  $('#form')
  .form({
    onSuccess: function(event, fields) {
        SubmitForm(fields);
        event.preventDefault();
    },
    on: 'blur',
    fields: {
      lx: {
        identifier  : 'lx',
        rules: [
          {
            type   : 'empty',
            prompt : 'Ingrese valor'
          }
        ]
      },
      ly: {
        identifier  : 'ly',
        rules: [
          {
            type   : 'empty',
            prompt : 'Ingrese valor'
          }
        ]
      }
    }
  });
}

function SubmitForm(fields) {
    var valid = $(".ui.form").form('is valid');
    $.ajax({
        url: '/calcular_lagrange',
        type: 'POST',
        data: fields,
        success: function(data){
            $('#solution').val(data.sections);
        }
    });
}