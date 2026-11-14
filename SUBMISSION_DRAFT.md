# Submission draft — edit after implementation and testing

**Title:** MissionLab: Build Your CubeSat

**Challenge:** Space Mission Design Game — NASA Space Apps Challenge 2026

**Tagline:** Design a science satellite, make engineering trade-offs, and discover how mission choices shape success.

## Project summary

MissionLab is a beginner-friendly educational spacecraft-design game. Players configure an Earth-observation CubeSat by selecting a scientific payload, a solar-power system, a radio and a launch option. Each choice affects budget, spacecraft mass, electricity demand, and data transmission. The game checks whether the mission satisfies each limit, then explains which trade-offs caused success or failure.

The prototype is deliberately simplified for young learners and first-time mission designers. It does not model actual satellite flight dynamics or offer real engineering specifications. All numerical inputs are illustrative game parameters.

## Problem and solution

Mission design requires balancing multiple interconnected constraints, but these trade-offs can be hard to understand from a textbook. MissionLab turns that idea into an interactive design exercise, letting users try options and immediately observe how changing one component affects the whole system.

## Technical approach

- Python functions implement component choices, accounting rules and pass/fail checks.
- Streamlit provides the interactive interface and displays results.
- Pandas presents the resource comparison table.
- Simple unit tests check several mission combinations.

## Learning outcomes

Players learn that a more capable scientific instrument is not automatically better: it may require more power, produce more data, weigh more and cost more. To succeed, the player must find a configuration that meets all constraints.

## Credits and sources

NASA *Design and Develop Science Missions* (2025); NASA *CubeSat 101* (2017); NASA *Build It Yourself* educational game; NASA Space Apps Challenge statement. All game numerical parameters are fictional. See `SOURCES.md` for full URLs and notes.

## Short demo script (about 60–90 seconds)

1. 'MissionLab helps students understand the trade-offs involved in designing a scientific space mission.'
2. 'Here we are building a satellite to observe Earth. We can choose the instrument, solar panels, radio and launch option.'
3. 'Watch what happens when I choose the high-resolution camera with compact panels and a basic radio. The design fails because the power and data demands exceed capacity.'
4. 'Now I upgrade the panels and radio and choose an appropriate launch option. The resource dashboard updates, the mission becomes feasible, and the game explains why.'
5. 'The values are educational, not actual NASA hardware specifications. The goal is to make systems-engineering choices tangible for beginners.'

## Complete before submission

- Team name and member names: [ADD]
- Who built which elements during the actual event: [ADD]
- GitHub repository URL: [ADD]
- Live deployed URL (if available): [ADD]
- Demo video / screenshots: [ADD]
- Known limitations and future improvements: [ADD]
- Participation disclosure, AI tool disclosure and licensing (as required): [ADD]

**Do not claim any untested feature or any code developed during a different time window as hackathon work without confirming the organizer's rules.**
