$(document).ready(function() {
     $(document).on('click', '#submit_login', function() {
        
        Sijax.request('sijax_login', [Sijax.getFormValues('#form_login')])
        return false;
     });

     $(document).on('click', '#submit_todo', function() {
        
        Sijax.request('sijax_todo_add', [Sijax.getFormValues('#form_todo')])
        return false;
     });
});