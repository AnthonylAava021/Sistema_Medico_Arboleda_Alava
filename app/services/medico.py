from flask import jsonify, request
from app.models import Medico, CertificadoMedico, Paciente
from datetime import datetime

@app.route('/medico/<int:medico_id>/generar-certificado', methods=['POST'])
def generar_certificado(medico_id):
    data = request.get_json()
    paciente = Paciente.query.get(data['paciente_id'])
    medico = Medico.query.get(medico_id)
    
    if not paciente or not medico:
        return jsonify({"error": "Paciente o médico no encontrado"}), 404
    
    certificado = CertificadoMedico(
        tipo=data['tipo'],
        descripcion=data['descripcion'],
        medico_id=medico_id,
        paciente_id=paciente.id
    )
    
    db.session.add(certificado)
    db.session.commit()
    
    return jsonify({
        "message": "Certificado generado exitosamente",
        "certificado_id": certificado.id
    }), 201