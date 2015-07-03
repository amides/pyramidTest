from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    ContactModel,
    )


# @view_config(route_name='home', renderer='templates/mytemplate.pt')
# def my_view(request):
#     try:
#         one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
#     except DBAPIError:
#         return Response(conn_err_msg, content_type='text/plain', status_int=500)
#     return {'one': one, 'project': 'simpleTest'}

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'MyProyect'}

@view_config(route_name='formsaved',renderer='templates/mytemplate.pt')
def form_save_view(request):
    name = request.params['nombre']
    lastName = request.params['apellido']
    email = request.params['email']
    telephoneNumber = request.params['telefono']
    address = request.params['direccion']

    contact = ContactModel(name = name,
                    last_name = lastName,
                    telephone = telephoneNumber,
                    email = email,
                    address=address )

    DBSession.add(contact)   
    DBSession.flush()

    return {'project': 'MyProyect'}



