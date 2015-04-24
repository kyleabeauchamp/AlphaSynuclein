import numpy as np 
import simtk.openmm as mm
import simtk.openmm.app as app
import simtk.unit as u

eu = u.kilocalories_per_mole
temperature = 300 * u.kelvin
friction = 1.0 / u.picosecond

pdb = app.PDBFile('pdb/resi-1-15.pdb')

forcefield = app.ForceField('amber99sb.xml',"tip3p.xml")

m = app.modeller.Modeller(pdb.topology , pdb.positions )
m.addSolvent(forcefield, padding=0.7*u.nanometer)

system = forcefield.createSystem(pdb.topology, nonbondedMethod=app.PME,nonbondedCutoff=0.95 * u.nanometer, constraints=app.HAngles)

integrator = mm.LangevinIntegrator(temperature, friction, 0.004*u.picoseconds)

simulation = app.Simulation(pdb.topology, system, integrator)
simulation.context.setPositions(pdb.positions)

simulation.reporters.append(app.DCDReporter("resi-1-15.dcd", 250))
print("running")
simulation.step(100000000)
