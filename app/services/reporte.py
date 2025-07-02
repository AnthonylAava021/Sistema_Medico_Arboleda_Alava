@app.route('/reporte/historial-clinico/<int:paciente_id>', methods=['GET'])
def obtener_historial_clinico(paciente_id):
    # Implementación para devolver PDF del historial
    pass

@app.route('/reporte/ventas', methods=['GET'])
def reporte_ventas():
    fecha_inicio = request.args.get('fecha_inicio')
    fecha_fin = request.args.get('fecha_fin')
    
    ventas = Reporte.filtrar_ventas(fecha_inicio, fecha_fin)
    total = sum(factura.calcular_total() for factura in ventas)
    
    return jsonify({
        "ventas": [v.to_dict() for v in ventas],
        "total": total,
        "cantidad": len(ventas)
    })