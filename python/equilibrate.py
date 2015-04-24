import numpy as np 
import simtk.openmm as mm
import simtk.openmm.app as app
import simtk.unit as u

eu = u.kilocalories_per_mole
temperature = 288 * u.kelvin
pressure = 1.0 * u.atmosphere
friction = 1.0 / u.picosecond

pdb = app.PDBFile('resi-1-15.pdb')

forcefield = app.ForceField('amber99sb.xml',"tip3p.xml")
system = forcefield.createSystem(pdb.topology, nonbondedMethod=app.PME,nonbondedCutoff=0.95 * u.nanometer, constraints=app.HAngles)

barostat = mm.MonteCarloBarostat(pressure, temperature)
system.addForce(barostat)
integrator = mm.LangevinIntegrator(temperature, friction, 0.001*u.picoseconds)

simulation = app.Simulation(pdb.topology, system, integrator)
simulation.context.setPositions(pdb.positions)

simulation.reporters.append(app.PDBReporter("equil.pdb", 10000))
print("running")
simulation.step(100000)
