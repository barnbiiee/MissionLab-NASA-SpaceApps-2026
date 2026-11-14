"""MissionLab: an educational Space Mission Design Game (not an engineering simulator)."""
import pandas as pd
import streamlit as st
from mission_logic import INSTRUMENTS, SOLAR, COMMS, LAUNCH, BUDGET, evaluate

st.set_page_config(page_title='MissionLab | Build Your CubeSat', page_icon='🛰️', layout='wide')
st.markdown('''<style>
.block-container{padding-top:2rem;max-width:1100px}
.hero{padding:22px 25px;border-radius:16px;background:linear-gradient(115deg,#132546,#2a4770);color:white;margin-bottom:22px}
.hero h1{color:white;margin:0;font-size:2.3rem}.hero p{color:#e2edff;margin:8px 0 0}
.small{font-size:.86rem;color:#677587}
</style>''', unsafe_allow_html=True)
st.markdown('<div class="hero"><h1>🛰️ MissionLab</h1><p>Build Your CubeSat · Make trade-offs · Launch your mission</p></div>', unsafe_allow_html=True)
st.write('**Your challenge:** Design an Earth-observation CubeSat that can collect and send useful science data while staying within budget, mass, power and communication limits.')
st.info('Educational simulation. Component values and scores are simplified, fictional game parameters — **not** NASA-validated engineering specifications.')

with st.sidebar:
    st.header('🧭 Mission briefing')
    st.write('**Destination:** Low Earth orbit (simplified)')
    st.write('**Objective:** Observe Earth and transmit data to scientists on the ground.')
    st.metric('Total budget', f'{BUDGET} credits')
    st.caption('Your game covers NASA-inspired space, launch, ground and user mission segments.')
    st.divider()
    st.write('**How to play**')
    st.write('1. Pick a science instrument.\n\n2. Pick solar panels and a radio.\n\n3. Choose a launch option.\n\n4. Inspect resource trade-offs and launch.')
    st.caption('NASA references and links are listed in the About section below.')

st.subheader('1 · Configure your spacecraft')
left, right = st.columns(2, gap='large')
with left:
    instrument = st.selectbox('🔭 Science instrument', list(INSTRUMENTS), index=0)
    st.caption(INSTRUMENTS[instrument]['description'])
    panels = st.selectbox('☀️ Power system', list(SOLAR), index=0)
    st.caption(SOLAR[panels]['description'])
with right:
    radio = st.selectbox('📡 Communications system', list(COMMS), index=0)
    st.caption(COMMS[radio]['description'])
    launch = st.selectbox('🚀 Launch vehicle / rideshare', list(LAUNCH), index=0)
    st.caption(LAUNCH[launch]['description'])

result = evaluate(instrument, panels, radio, launch)
st.subheader('2 · Mission resource dashboard')
cols = st.columns(4)
for col, (name, check) in zip(cols, result['checks'].items()):
    with col:
        symbol = '✅' if check['passed'] else '⚠️'
        st.metric(f'{symbol} {name}', f"{check['used']} {check['unit']}", f"Limit: {check['limit']}", delta_color='off')
        st.progress(min(float(check['used']) / float(check['limit']), 1.0))

st.caption('Each limit is an intentionally simplified teaching constraint. The model counts baseline spacecraft systems in cost, mass and power.')
resource_df = pd.DataFrame([
    {'Constraint': k, 'Used': v['used'], 'Allowed': v['limit'], 'Status': 'Pass' if v['passed'] else 'Exceeded'}
    for k, v in result['checks'].items()
])
with st.expander('🔍 See the complete resource table and design rules'):
    st.dataframe(resource_df, hide_index=True, use_container_width=True)
    st.write('**Model rules:** Costs and masses are added; the instrument and radio consume power; solar panels provide power; an instrument generates data; the radio transmits data. A mission is feasible only when all four checks pass.')
    st.write('**Score:** If feasible, science value + a budget-efficiency bonus (up to 20). If infeasible, score = 0. This score is a game mechanic, not a scientific prediction.')

st.subheader('3 · Launch and evaluate')
if st.button('🚀 Simulate mission', use_container_width=True, type='primary'):
    st.session_state['last_result'] = result
    st.session_state['last_config'] = (instrument, panels, radio, launch)

# Do not show stale results if the player adjusts their design.
if st.session_state.get('last_config') == (instrument, panels, radio, launch):
    finished = st.session_state['last_result']
    if finished['feasible']:
        st.success('🛰️ **Mission feasible!** Your satellite is launched in this simplified scenario.')
        st.markdown('**Mission timeline**')
        st.write('✅ Design approved → ✅ Launch mass checked → ✅ Solar power available → ✅ Earth observations collected → ✅ Data transmitted to ground scientists')
        st.metric('Mission score', f"{finished['score']} / 100")
    else:
        st.error('🚫 **Mission could not proceed.** Fix the highlighted design constraints and try again.')
        st.metric('Mission score', '0 / 100')
    st.markdown('**Post-mission analysis**')
    for msg in finished['explanations']:
        st.write('• ' + msg)
    st.write('**Engineering lesson:** Higher-capability science instruments can improve observations but also increase cost, mass, power draw and data volume. Try another combination and compare the outcome.')

st.divider()
with st.expander('📚 About the model, sources and limitations'):
    st.write('**What the game teaches:** Mission objectives, launch compatibility, science payload, power, downlink and resource trade-offs across mission segments.')
    st.write('**What it does not simulate:** Orbital mechanics, thermal control, batteries, radiation, ground-station visibility, launch trajectories, genuine mission probabilities or validated equipment costs.')
    st.write('**Sources / inspiration:**')
    st.markdown('- [NASA: Design and Develop Science Missions (2025)](https://www.nasa.gov/wp-content/uploads/2025/04/250323-design-and-develop-science-mission.pdf)')
    st.markdown('- [NASA: CubeSat 101 (2017)](https://www3.nasa.gov/sites/default/files/atoms/files/nasa_csli_cubesat_101_508.pdf)')
    st.markdown('- [NASA: Build It Yourself — educational game](https://science.nasa.gov/mission/webb/game-build-it-yourself/)')
    st.markdown('- [NASA Space Apps: Space Mission Design Game challenge](https://www.spaceappschallenge.org/2026/challenges/space-mission-design-game/)')
    st.caption('This independent educational project is not affiliated with or endorsed by NASA.')
