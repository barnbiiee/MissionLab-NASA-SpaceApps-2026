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

## NASA event / preparation note

The public NASA Space Apps website lists the 2026 hackathon as November 14–15 with project submission opening November 14 at 9 AM and closing November 15 at 11:59 PM local time. **Check the official rules for whether work prepared before the event is eligible as a competition submission.** Use this scaffold as practice/reference and make the actual competition project in accordance with the organizers' rules. Do not state that work was completed during the hackathon unless that is true.

## Publish / submission checklist

- [ ] Confirm eligibility and pre-event-work rules with organizers
- [ ] Both team members run and understand the code
- [ ] Test failed and successful builds
- [ ] Update and honestly document what was built during the event
- [ ] Add team member contributions
- [ ] Create public repository (e.g. GitHub) if allowed
- [ ] Record a short original demonstration, if required
- [ ] Put project link, real sources, and properly licensed assets in submission
- [ ] Submit before the deadline through your team's official project page
