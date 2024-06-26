from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        number_of_tyres = float(request.form['number_of_tyres'])
        fixed_capital = float(request.form['fixed_capital'])
        patches_cost = float(request.form['patches_cost'])
        envelopes_cost = float(request.form['envelopes_cost'])
        other_consumables_cost = float(request.form['other_consumables_cost'])
        operating_expenses = float(request.form['operating_expenses'])
        sales_realization = float(request.form['sales_realization'])

        raw_material_cost_per_tyre = (patches_cost + envelopes_cost + other_consumables_cost) / number_of_tyres
        gross_margin = sales_realization - (raw_material_cost_per_tyre * number_of_tyres + operating_expenses)
        taxes = gross_margin * 0.12
        net_margin = gross_margin - taxes
        profit_percentage = (net_margin / sales_realization) * 100
        roi = (net_margin / fixed_capital) * 100

        return render_template('index.html', 
                               fixed_capital=fixed_capital, 
                               raw_material_cost_per_tyre=raw_material_cost_per_tyre, 
                               gross_margin=gross_margin, 
                               taxes=taxes, 
                               net_margin=net_margin, 
                               profit_percentage=profit_percentage, 
                               roi=roi,
                               number_of_tyres=number_of_tyres,
                               patches_cost=patches_cost,
                               envelopes_cost=envelopes_cost,
                               other_consumables_cost=other_consumables_cost,
                               operating_expenses=operating_expenses,
                               sales_realization=sales_realization)
    except ValueError:
        return render_template('index.html', error="Invalid input. Please enter numeric values.")
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
