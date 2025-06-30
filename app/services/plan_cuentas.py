@app.route('/plan-cuentas/balance', methods=['GET'])
def obtener_balance():
    balance = PlanCuentas.generar_balance()
    return jsonify(balance)