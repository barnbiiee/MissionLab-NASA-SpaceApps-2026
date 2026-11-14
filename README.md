Play MissionLab

Try our interactive CubeSat mission design game here:

https://missionlab-nasa-spaceapps-2026-krtj7ai5ekc5eme9vkv2im.streamlit.app/

For the best experience, we recommend opening the game in Google Chrome.

# MissionLab — Build Your CubeSat

An educational **Space Mission Design Game** prototype for the 2026 NASA Space Apps Challenge. Players choose a science instrument, solar panels, communications system and rideshare launch vehicle. They must satisfy **budget, mass, power, and data-downlink** constraints. The game explains success/failure and provides an illustrative score.

> **Important:** All component specifications, budget points, launch capacities and scoring values are fictional game parameters. They are **not NASA-validated engineering data**, and the app does not calculate a real probability of mission success.

## Run on your laptop

1. Install Python 3.10 or newer. Open this folder in VS Code.
2. Open a terminal (Terminal → New Terminal).
3. (Recommended) Create a virtual environment:
   - macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate`
   - Windows PowerShell: `py -m venv .venv; .venv\Scripts\Activate.ps1`
4. Install packages: `python -m pip install -r requirements.txt`
5. Run: `python -m streamlit run app.py`
6. The terminal will show a local address, commonly `http://localhost:8501`. Open it in your browser.

## Test game calculations

`python -m unittest -v test_mission_logic.py`

## Files

- `app.py`: Streamlit user interface, dashboard, simulation, feedback and sources
- `mission_logic.py`: component catalogue, resource rules and scoring
- `test_mission_logic.py`: automated basic tests
- `SUBMISSION_DRAFT.md`: project description, demonstration outline and contribution checklist
- `SOURCES.md`: source acknowledgments and assumptions

## Gameplay and constraints

- **Goal:** Design an Earth-observation CubeSat.
- **Choices:** 3 science instruments, 2 solar configurations, 2 radios, 2 rideshare launch options.
- **Budget:** Total component + baseline spacecraft + launch costs must be ≤130 game credits.
- **Mass:** Spacecraft mass must not exceed selected rideshare capacity.
- **Power:** Baseline spacecraft + instrument + radio usage must not exceed selected solar panel generation.
- **Downlink:** Instrument daily generated data must not exceed selected radio capacity.
- **Result:** A feasible design receives a scientific-value + budget-efficiency score; an infeasible one receives 0 and recommendations.

**Scope intentionally excluded:** Real orbital dynamics, trajectory optimization, multiplayer, real launch pricing, geolocation, physical reliability prediction. This is a minimal educational game, not engineering advice.


