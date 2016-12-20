$(function(){
    initValidate();
});

function initValidate(){
  $('#form')
  .form({
    onSuccess: function(event, fields) {
        SubmitForm(fields);
        event.preventDefault();
    },
    on: 'blur',
    fields: {
      equation: {
        identifier  : 'equation',
        rules: [
          {
            type   : 'empty',
            prompt : 'Ingrese valor'
          }
        ]
      },
      a: {
        identifier  : 'a',
        rules: [
          {
            type   : 'empty',
            prompt : 'Ingrese valor'
          },
          {
            type: 'decimal',
            prompt: 'Tiene que ser un número'
          }
        ]
      },
      a: {
        identifier  : 'a',
        rules: [
          {
            type   : 'empty',
            prompt : 'Ingrese valor'
          },
          {
            type: 'decimal',
            prompt: 'Tiene que ser un número'
          }
        ]
      },
      level: {
        identifier  : 'level',
        rules: [
          {
            type   : 'empty',
            prompt : 'Ingrese valor'
          },
          {
            type: 'integer',
            prompt: 'Tiene que ser un número'
          }
        ]
      }
    }
  });
}

function SubmitForm(fields, board) {
    var valid = $(".ui.form").form('is valid');
    $.ajax({
        url: '/calcular_romberg',
        type: 'POST',
        data: fields,
        success: function(data){
           result = eval(data.result)
           $('#body-table').empty();
           $.each(result, function(index, element){
                var actual = '<tr>';
                $.each(element, function(i, e){
                    actual = actual + '<td>' + e + '</td>';
                });
                actual = actual + '</tr>';
                $('#body-table').append(actual);
            });
//            $('#solution').val();
        }
    });
}

function drawPoints(board, a, b, error){
    board.create('point', [a,b],{name: error+'%', withLabel:true});
}