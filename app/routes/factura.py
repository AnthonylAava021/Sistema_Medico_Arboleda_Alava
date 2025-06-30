@app.route('/factura/consulta/<int:consulta_id>', methods=['POST'])
def generar_factura_consulta(consulta_id):
    data = request.get_json()
    consulta = Consulta.query.get(consulta_id)
    
    if not consulta:
        return jsonify({"error": "Consulta no encontrada"}), 404
    
    factura = Factura(
        monto=data['monto'],
        metodo_pago=data.get('metodo_pago', 'Pendiente'),
        consulta_id=consulta_id,
        usuario_id=consulta.paciente.usuario_id
    )
    
    db.session.add(factura)
    db.session.commit()
    
    return jsonify({
        "message": "Factura generada exitosamente",
        "factura_id": factura.id,
        "total": factura.calcular_total()
    }), 201