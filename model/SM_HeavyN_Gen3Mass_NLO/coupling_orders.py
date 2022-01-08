# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.2.0 for Linux x86 (64-bit) (September 11, 2017)
# Date: Fri 23 Mar 2018 19:49:38


from object_library import all_orders, CouplingOrder


QCD = CouplingOrder(name = 'QCD',
                    expansion_order = 99,
                    hierarchy = 1,
                    perturbative_expansion = 1)

QED = CouplingOrder(name = 'QED',
                    expansion_order = 99,
                    hierarchy = 2)

NP = CouplingOrder(name = 'NP',
                   expansion_order = 99,
                   hierarchy = 1)

