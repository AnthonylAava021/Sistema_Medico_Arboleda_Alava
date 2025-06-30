@app.route('/caja/registrar', methods=['POST'])
def registrar_movimiento_caja():
    data = request.get_json()
    
    try:
        movimiento = DiarioCaja.registrar_movimiento(
            descripcion=data['descripcion'],
            monto=data['monto'],
            tipo=data['tipo'],
            factura_id=data.get('factura_id'),
            cuenta_id=data.get('cuenta_id')
        )
        
        return jsonify({
            "message": "Movimiento registrado exitosamente",
            "movimiento_id": movimiento.id
        }), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400