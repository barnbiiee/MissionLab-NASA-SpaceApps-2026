"""Simplified educational CubeSat mission model. Values are illustrative, not flight data."""

INSTRUMENTS = {
    'Basic camera': {'cost': 18, 'mass': 0.7, 'power': 4, 'data': 3, 'science': 30, 'description': 'Captures basic Earth imagery.'},
    'High-resolution camera': {'cost': 38, 'mass': 1.4, 'power': 10, 'data': 9, 'science': 60, 'description': 'Better scientific images but heavier, more costly, and data-intensive.'},
    'Multispectral sensor': {'cost': 32, 'mass': 1.1, 'power': 8, 'data': 7, 'science': 52, 'description': 'Observes Earth in multiple wavelength bands.'},
}
SOLAR = {
    'Compact solar panels': {'cost': 12, 'mass': 0.4, 'supply': 12, 'description': 'Light and cheap, with limited power.'},
    'Expanded solar panels': {'cost': 27, 'mass': 0.9, 'supply': 22, 'description': 'More power, but higher mass and cost.'},
}
COMMS = {
    'Basic radio': {'cost': 10, 'mass': 0.25, 'power': 2, 'capacity': 4, 'description': 'Can send a small amount of data to Earth.'},
    'High-rate radio': {'cost': 24, 'mass': 0.5, 'power': 5, 'capacity': 10, 'description': 'Can send more data, but uses more power.'},
}
LAUNCH = {
    'Economy rideshare': {'cost': 20, 'capacity': 4.0, 'description': 'Cheap ride with a strict mass limit.'},
    'Heavy rideshare': {'cost': 38, 'capacity': 5.0, 'description': 'Carries a heavier spacecraft but costs more.'},
}
BASE = {'cost': 15, 'mass': 0.8, 'power': 3}  # structure, computer, baseline operations
BUDGET = 130


def evaluate(instrument: str, panels: str, radio: str, launch: str) -> dict:
    """Evaluate basic feasibility and compute a transparent illustrative score."""
    i, p, c, l = INSTRUMENTS[instrument], SOLAR[panels], COMMS[radio], LAUNCH[launch]
    cost = BASE['cost'] + i['cost'] + p['cost'] + c['cost'] + l['cost']
    mass = BASE['mass'] + i['mass'] + p['mass'] + c['mass']
    power = BASE['power'] + i['power'] + c['power']
    generated = p['supply']
    data = i['data']
    bandwidth = c['capacity']

    checks = {
        'Budget': {'used': cost, 'limit': BUDGET, 'unit': 'credits', 'passed': cost <= BUDGET},
        'Launch mass': {'used': round(mass, 2), 'limit': l['capacity'], 'unit': 'kg', 'passed': mass <= l['capacity']},
        'Power': {'used': power, 'limit': generated, 'unit': 'W', 'passed': power <= generated},
        'Communications': {'used': data, 'limit': bandwidth, 'unit': 'data units/day', 'passed': data <= bandwidth},
    }
    feasible = all(x['passed'] for x in checks.values())
    explanations = []
    if cost > BUDGET:
        explanations.append('Your mission costs more than the budget permits. Choose cheaper hardware or launch.')
    if mass > l['capacity']:
        explanations.append('Your spacecraft exceeds the selected rideshare mass capacity. Choose lighter hardware or a larger rideshare.')
    if power > generated:
        explanations.append('Your spacecraft uses more power than its solar panels provide. Choose larger panels or lower-power instruments.')
    if data > bandwidth:
        explanations.append('The instrument produces more data than the radio can transmit. Upgrade the radio or reduce data generation.')
    if feasible:
        explanations.append('All four constraints are satisfied. Your simplified satellite is ready for a simulated mission.')

    # Score: feasible designs earn science value + efficiency bonus; unworkable missions score 0.
    spare_budget = max(0, BUDGET - cost)
    efficiency_bonus = round(20 * spare_budget / BUDGET)
    score = min(100, i['science'] + efficiency_bonus) if feasible else 0
    return {
        'feasible': feasible, 'score': score, 'checks': checks, 'cost': cost,
        'mass': round(mass, 2), 'power': power, 'power_supply': generated,
        'data': data, 'data_capacity': bandwidth, 'science': i['science'],
        'explanations': explanations,
    }
