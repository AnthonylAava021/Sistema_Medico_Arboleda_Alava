from flask import request, jsonify
from flask_restx import Namespace, Resource, fields, reqparse
from app.services.usuario_servicio import registrar_usuario, login_usuario
from app.model.usuario import UserRole, Usuario
from app.configuracion_base import db
from flask_jwt_extended import jwt_required, get_jwt_identity

api = Namespace('usuarios', description='Gestión de usuarios')

user_model = api.model('Usuario', {
    'id': fields.Integer(readonly=True),
    'username': fields.String(required=True),
    'email': fields.String(required=True),
    'role': fields.String(enum=[role.value for role in UserRole], default=UserRole.PACIENTE.value)
})

register_parser = reqparse.RequestParser()
register_parser.add_argument('username', type=str, required=True, help='Nombre de usuario')
register_parser.add_argument('email', type=str, required=True, help='Email')
register_parser.add_argument('password', type=str, required=True, help='Contraseña')
register_parser.add_argument('role', type=str, choices=[role.value for role in UserRole], default=UserRole.PACIENTE.value)

login_parser = reqparse.RequestParser()
login_parser.add_argument('username', type=str, required=True, help='Nombre de usuario')
login_parser.add_argument('password', type=str, required=True, help='Contraseña')

@api.route('/register')
class Register(Resource):
    @api.expect(register_parser)
    @api.marshal_with(user_model, code=201)
    def post(self):
        args = register_parser.parse_args()
        try:
            usuario = registrar_usuario(args['username'], args['email'], args['password'], args['role'])
            return usuario, 201
        except ValueError as e:
            api.abort(400, str(e))

@api.route('/login')
class Login(Resource):
    @api.expect(login_parser)
    def post(self):
        args = login_parser.parse_args()
        token = login_usuario(args['username'], args['password'])
        if not token:
            api.abort(401, 'Usuario o contraseña incorrectos')
        return {'access_token': token}, 200

@api.route('/me')
class PerfilUsuario(Resource):
    @jwt_required()
    @api.marshal_with(user_model)
    def get(self):
        user_id = get_jwt_identity()
        usuario = Usuario.query.get(user_id)
        if not usuario:
            api.abort(404, 'Usuario no encontrado')
        return usuario
