# My attempt at solving this problem while being really bad @ math
from sys import argv
import json

def main():
    if len(argv) != 3:
        print("Utilisation : python solve.py [fichier d'input] [fichier d'output]")
        exit(1)
    with open(argv[1]) as fp:
        inpt = json.load(fp)
    #
    # Initialization
    #
    # general_parameters
    P_max = inpt['general_parameters']['maximum_power']
    c_0 = inpt['general_parameters']['curtailing_cost']
    c_p = inpt['general_parameters']['curtailing_penalty']
    c_max = inpt['general_parameters']['maximum_curtailing']
    cost_f_t = inpt['general_parameters']['fixed_cost_cable']
    cost_l_t = inpt['general_parameters']['variable_cost_cable']
    v_0_x = inpt['general_parameters']['main_land_station']['x']
    v_0_y = inpt['general_parameters']['main_land_station']['y']
    # substation_types
    S = inpt['substation_types']
    # land_substation_cable_types
    Q_0 = inpt['land_substation_cable_types']
    # substation_substation_cable_types
    Q_s = inpt['substation_substation_cable_types']
    # substation_locations
    V_s = inpt['substation_locations']
    # wind_turbines
    V_t = inpt['wind_turbines']
    # our output
    output = {"substations": [],
              "substation_substation_cables": [],
              "turbines": []
              }

    #
    # Do things, idk...
    #
    total_costs(1, 2, 3, V_s, S)

    #
    # Write output
    #
    with open(argv[2], 'w') as fp:
        json.dump(output, fp)


def total_costs(x, y, z, lV_s, lS):
    construction_cost = 0
    for v in lV_s:
        for s in lS:
            print('ui ', end='')


if __name__ == "__main__":
    main()
