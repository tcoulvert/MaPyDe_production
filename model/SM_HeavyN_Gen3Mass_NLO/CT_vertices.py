# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.2.0 for Linux x86 (64-bit) (September 11, 2017)
# Date: Fri 23 Mar 2018 19:49:39


from object_library import all_vertices, all_CTvertices, Vertex, CTVertex
import particles as P
import CT_couplings as C
import lorentz as L


V_1 = CTVertex(name = 'V_1',
               type = 'R2',
               particles = [ P.g, P.g, P.g ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVV2 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(0,0,0):C.R2GC_199_49,(0,0,1):C.R2GC_199_50})

V_2 = CTVertex(name = 'V_2',
               type = 'R2',
               particles = [ P.g, P.g, P.g, P.g ],
               color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
               lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
               loop_particles = [ [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ] ],
               couplings = {(2,1,0):C.R2GC_162_29,(2,1,1):C.R2GC_162_30,(0,1,0):C.R2GC_162_29,(0,1,1):C.R2GC_162_30,(6,1,0):C.R2GC_165_34,(6,1,1):C.R2GC_204_56,(4,1,0):C.R2GC_160_25,(4,1,1):C.R2GC_160_26,(3,1,0):C.R2GC_160_25,(3,1,1):C.R2GC_160_26,(8,1,0):C.R2GC_161_27,(8,1,1):C.R2GC_161_28,(7,1,0):C.R2GC_166_36,(7,1,1):C.R2GC_203_55,(5,1,0):C.R2GC_160_25,(5,1,1):C.R2GC_160_26,(1,1,0):C.R2GC_160_25,(1,1,1):C.R2GC_160_26,(11,0,0):C.R2GC_164_32,(11,0,1):C.R2GC_164_33,(10,0,0):C.R2GC_164_32,(10,0,1):C.R2GC_164_33,(9,0,1):C.R2GC_163_31,(2,2,0):C.R2GC_162_29,(2,2,1):C.R2GC_162_30,(0,2,0):C.R2GC_162_29,(0,2,1):C.R2GC_162_30,(4,2,0):C.R2GC_160_25,(4,2,1):C.R2GC_160_26,(3,2,0):C.R2GC_160_25,(3,2,1):C.R2GC_160_26,(8,2,0):C.R2GC_161_27,(8,2,1):C.R2GC_205_57,(6,2,0):C.R2GC_200_51,(6,2,1):C.R2GC_200_52,(7,2,0):C.R2GC_166_36,(7,2,1):C.R2GC_166_37,(5,2,0):C.R2GC_160_25,(5,2,1):C.R2GC_160_26,(1,2,0):C.R2GC_160_25,(1,2,1):C.R2GC_160_26,(2,3,0):C.R2GC_162_29,(2,3,1):C.R2GC_162_30,(0,3,0):C.R2GC_162_29,(0,3,1):C.R2GC_162_30,(4,3,0):C.R2GC_160_25,(4,3,1):C.R2GC_160_26,(3,3,0):C.R2GC_160_25,(3,3,1):C.R2GC_160_26,(8,3,0):C.R2GC_161_27,(8,3,1):C.R2GC_202_54,(6,3,0):C.R2GC_165_34,(6,3,1):C.R2GC_165_35,(7,3,0):C.R2GC_201_53,(7,3,1):C.R2GC_162_30,(5,3,0):C.R2GC_160_25,(5,3,1):C.R2GC_160_26,(1,3,0):C.R2GC_160_25,(1,3,1):C.R2GC_160_26})

V_3 = CTVertex(name = 'V_3',
               type = 'R2',
               particles = [ P.t__tilde__, P.b, P.G__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_214_60,(0,1,0):C.R2GC_215_61})

V_4 = CTVertex(name = 'V_4',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_196_45})

V_5 = CTVertex(name = 'V_5',
               type = 'R2',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.b, P.g] ] ],
               couplings = {(0,0,0):C.R2GC_195_44})

V_6 = CTVertex(name = 'V_6',
               type = 'R2',
               particles = [ P.b__tilde__, P.t, P.G__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS3, L.FFS5 ],
               loop_particles = [ [ [P.b, P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_216_62,(0,1,0):C.R2GC_213_59})

V_7 = CTVertex(name = 'V_7',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.G0 ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_217_63})

V_8 = CTVertex(name = 'V_8',
               type = 'R2',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS2 ],
               loop_particles = [ [ [P.g, P.t] ] ],
               couplings = {(0,0,0):C.R2GC_218_64})

V_9 = CTVertex(name = 'V_9',
               type = 'R2',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               loop_particles = [ [ [P.g, P.u] ] ],
               couplings = {(0,0,0):C.R2GC_170_41})

V_10 = CTVertex(name = 'V_10',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_170_41})

V_11 = CTVertex(name = 'V_11',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_170_41})

V_12 = CTVertex(name = 'V_12',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_167_38})

V_13 = CTVertex(name = 'V_13',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_167_38})

V_14 = CTVertex(name = 'V_14',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_167_38})

V_15 = CTVertex(name = 'V_15',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_168_39})

V_16 = CTVertex(name = 'V_16',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_168_39})

V_17 = CTVertex(name = 'V_17',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_168_39})

V_18 = CTVertex(name = 'V_18',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_168_39})

V_19 = CTVertex(name = 'V_19',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_168_39})

V_20 = CTVertex(name = 'V_20',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_168_39})

V_21 = CTVertex(name = 'V_21',
                type = 'R2',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_187_42})

V_22 = CTVertex(name = 'V_22',
                type = 'R2',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_187_42})

V_23 = CTVertex(name = 'V_23',
                type = 'R2',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_187_42})

V_24 = CTVertex(name = 'V_24',
                type = 'R2',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_187_42})

V_25 = CTVertex(name = 'V_25',
                type = 'R2',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_187_42})

V_26 = CTVertex(name = 'V_26',
                type = 'R2',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_187_42})

V_27 = CTVertex(name = 'V_27',
                type = 'R2',
                particles = [ P.u__tilde__, P.u, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_144_21,(0,1,0):C.R2GC_131_1})

V_28 = CTVertex(name = 'V_28',
                type = 'R2',
                particles = [ P.c__tilde__, P.c, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_144_21,(0,1,0):C.R2GC_131_1})

V_29 = CTVertex(name = 'V_29',
                type = 'R2',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_144_21,(0,1,0):C.R2GC_131_1})

V_30 = CTVertex(name = 'V_30',
                type = 'R2',
                particles = [ P.d__tilde__, P.d, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_145_22,(0,1,0):C.R2GC_132_2})

V_31 = CTVertex(name = 'V_31',
                type = 'R2',
                particles = [ P.s__tilde__, P.s, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_145_22,(0,1,0):C.R2GC_132_2})

V_32 = CTVertex(name = 'V_32',
                type = 'R2',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_145_22,(0,1,0):C.R2GC_132_2})

V_33 = CTVertex(name = 'V_33',
                type = 'R2',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_192_43,(0,2,0):C.R2GC_192_43,(0,1,0):C.R2GC_169_40,(0,3,0):C.R2GC_169_40})

V_34 = CTVertex(name = 'V_34',
                type = 'R2',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_169_40})

V_35 = CTVertex(name = 'V_35',
                type = 'R2',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.R2GC_169_40})

V_36 = CTVertex(name = 'V_36',
                type = 'R2',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.R2GC_169_40})

V_37 = CTVertex(name = 'V_37',
                type = 'R2',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_209_58,(0,2,0):C.R2GC_209_58,(0,1,0):C.R2GC_169_40,(0,3,0):C.R2GC_169_40})

V_38 = CTVertex(name = 'V_38',
                type = 'R2',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_169_40})

V_39 = CTVertex(name = 'V_39',
                type = 'R2',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV2, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.g] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.R2GC_198_48,(0,1,0):C.R2GC_135_3,(0,1,3):C.R2GC_135_4,(0,2,1):C.R2GC_197_46,(0,2,2):C.R2GC_197_47})

V_40 = CTVertex(name = 'V_40',
                type = 'R2',
                particles = [ P.g, P.g, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_136_5,(0,0,1):C.R2GC_136_6})

V_41 = CTVertex(name = 'V_41',
                type = 'R2',
                particles = [ P.g, P.g, P.W__minus__, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b, P.t], [P.c, P.s], [P.d, P.u] ] ],
                couplings = {(0,0,0):C.R2GC_148_24,(0,1,0):C.R2GC_148_24,(0,2,0):C.R2GC_148_24})

V_42 = CTVertex(name = 'V_42',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.Z ],
                color = [ 'Identity(2,3)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_140_13,(0,0,1):C.R2GC_140_14,(0,1,0):C.R2GC_140_13,(0,1,1):C.R2GC_140_14,(0,2,0):C.R2GC_140_13,(0,2,1):C.R2GC_140_14})

V_43 = CTVertex(name = 'V_43',
                type = 'R2',
                particles = [ P.g, P.g, P.Z, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_143_19,(0,0,1):C.R2GC_143_20,(0,1,0):C.R2GC_143_19,(0,1,1):C.R2GC_143_20,(0,2,0):C.R2GC_143_19,(0,2,1):C.R2GC_143_20})

V_44 = CTVertex(name = 'V_44',
                type = 'R2',
                particles = [ P.a, P.a, P.g, P.g ],
                color = [ 'Identity(3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_138_9,(0,0,1):C.R2GC_138_10,(0,1,0):C.R2GC_138_9,(0,1,1):C.R2GC_138_10,(0,2,0):C.R2GC_138_9,(0,2,1):C.R2GC_138_10})

V_45 = CTVertex(name = 'V_45',
                type = 'R2',
                particles = [ P.g, P.g, P.g, P.Z ],
                color = [ 'd(1,2,3)', 'f(1,2,3)' ],
                lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(1,0,0):C.R2GC_142_17,(1,0,1):C.R2GC_142_18,(0,1,0):C.R2GC_141_15,(0,1,1):C.R2GC_141_16,(0,2,0):C.R2GC_141_15,(0,2,1):C.R2GC_141_16,(0,3,0):C.R2GC_141_15,(0,3,1):C.R2GC_141_16})

V_46 = CTVertex(name = 'V_46',
                type = 'R2',
                particles = [ P.a, P.g, P.g, P.g ],
                color = [ 'd(2,3,4)' ],
                lorentz = [ L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b], [P.d], [P.s] ], [ [P.c], [P.t], [P.u] ] ],
                couplings = {(0,0,0):C.R2GC_139_11,(0,0,1):C.R2GC_139_12,(0,1,0):C.R2GC_139_11,(0,1,1):C.R2GC_139_12,(0,2,0):C.R2GC_139_11,(0,2,1):C.R2GC_139_12})

V_47 = CTVertex(name = 'V_47',
                type = 'R2',
                particles = [ P.g, P.g, P.H, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_137_7,(0,0,1):C.R2GC_137_8})

V_48 = CTVertex(name = 'V_48',
                type = 'R2',
                particles = [ P.g, P.g, P.G0, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.R2GC_137_7,(0,0,1):C.R2GC_137_8})

V_49 = CTVertex(name = 'V_49',
                type = 'R2',
                particles = [ P.g, P.g, P.G__minus__, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VVSS1 ],
                loop_particles = [ [ [P.b, P.t] ] ],
                couplings = {(0,0,0):C.R2GC_147_23})

V_50 = CTVertex(name = 'V_50',
                type = 'UV',
                particles = [ P.g, P.g, P.g ],
                color = [ 'f(1,2,3)' ],
                lorentz = [ L.VVV1, L.VVV2, L.VVV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,1,0):C.UVGC_199_44,(0,1,1):C.UVGC_199_45,(0,1,4):C.UVGC_199_46,(0,2,2):C.UVGC_150_1,(0,0,3):C.UVGC_151_2})

V_51 = CTVertex(name = 'V_51',
                type = 'UV',
                particles = [ P.g, P.g, P.g, P.g ],
                color = [ 'd(-1,1,3)*d(-1,2,4)', 'd(-1,1,3)*f(-1,2,4)', 'd(-1,1,4)*d(-1,2,3)', 'd(-1,1,4)*f(-1,2,3)', 'd(-1,2,3)*f(-1,1,4)', 'd(-1,2,4)*f(-1,1,3)', 'f(-1,1,2)*f(-1,3,4)', 'f(-1,1,3)*f(-1,2,4)', 'f(-1,1,4)*f(-1,2,3)', 'Identity(1,2)*Identity(3,4)', 'Identity(1,3)*Identity(2,4)', 'Identity(1,4)*Identity(2,3)' ],
                lorentz = [ L.VVVV10, L.VVVV2, L.VVVV3, L.VVVV5 ],
                loop_particles = [ [ [P.b] ], [ [P.b], [P.c], [P.d], [P.s], [P.t], [P.u] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(2,1,3):C.UVGC_161_9,(2,1,4):C.UVGC_161_8,(0,1,3):C.UVGC_161_9,(0,1,4):C.UVGC_161_8,(6,1,0):C.UVGC_203_58,(6,1,2):C.UVGC_203_59,(6,1,3):C.UVGC_204_63,(6,1,4):C.UVGC_204_64,(6,1,5):C.UVGC_203_62,(4,1,3):C.UVGC_160_6,(4,1,4):C.UVGC_160_7,(3,1,3):C.UVGC_160_6,(3,1,4):C.UVGC_160_7,(8,1,3):C.UVGC_161_8,(8,1,4):C.UVGC_161_9,(7,1,0):C.UVGC_203_58,(7,1,2):C.UVGC_203_59,(7,1,3):C.UVGC_203_60,(7,1,4):C.UVGC_203_61,(7,1,5):C.UVGC_203_62,(5,1,3):C.UVGC_160_6,(5,1,4):C.UVGC_160_7,(1,1,3):C.UVGC_160_6,(1,1,4):C.UVGC_160_7,(11,0,3):C.UVGC_164_12,(11,0,4):C.UVGC_164_13,(10,0,3):C.UVGC_164_12,(10,0,4):C.UVGC_164_13,(9,0,3):C.UVGC_163_10,(9,0,4):C.UVGC_163_11,(2,2,3):C.UVGC_161_9,(2,2,4):C.UVGC_161_8,(0,2,3):C.UVGC_161_9,(0,2,4):C.UVGC_161_8,(4,2,3):C.UVGC_160_6,(4,2,4):C.UVGC_160_7,(3,2,3):C.UVGC_160_6,(3,2,4):C.UVGC_160_7,(8,2,0):C.UVGC_205_65,(8,2,2):C.UVGC_205_66,(8,2,3):C.UVGC_205_67,(8,2,4):C.UVGC_205_68,(8,2,5):C.UVGC_205_69,(6,2,0):C.UVGC_200_47,(6,2,3):C.UVGC_200_48,(6,2,4):C.UVGC_200_49,(6,2,5):C.UVGC_200_50,(7,2,1):C.UVGC_165_14,(7,2,3):C.UVGC_166_16,(7,2,4):C.UVGC_166_17,(5,2,3):C.UVGC_160_6,(5,2,4):C.UVGC_160_7,(1,2,3):C.UVGC_160_6,(1,2,4):C.UVGC_160_7,(2,3,3):C.UVGC_161_9,(2,3,4):C.UVGC_161_8,(0,3,3):C.UVGC_161_9,(0,3,4):C.UVGC_161_8,(4,3,3):C.UVGC_160_6,(4,3,4):C.UVGC_160_7,(3,3,3):C.UVGC_160_6,(3,3,4):C.UVGC_160_7,(8,3,0):C.UVGC_202_53,(8,3,2):C.UVGC_202_54,(8,3,3):C.UVGC_202_55,(8,3,4):C.UVGC_202_56,(8,3,5):C.UVGC_202_57,(6,3,1):C.UVGC_165_14,(6,3,3):C.UVGC_165_15,(6,3,4):C.UVGC_163_10,(7,3,0):C.UVGC_200_47,(7,3,3):C.UVGC_201_51,(7,3,4):C.UVGC_201_52,(7,3,5):C.UVGC_200_50,(5,3,3):C.UVGC_160_6,(5,3,4):C.UVGC_160_7,(1,3,3):C.UVGC_160_6,(1,3,4):C.UVGC_160_7})

V_52 = CTVertex(name = 'V_52',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.G__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_214_81,(0,0,2):C.UVGC_214_82,(0,0,1):C.UVGC_214_83,(0,1,0):C.UVGC_215_84,(0,1,2):C.UVGC_215_85,(0,1,1):C.UVGC_215_86})

V_53 = CTVertex(name = 'V_53',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_196_37})

V_54 = CTVertex(name = 'V_54',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_195_36})

V_55 = CTVertex(name = 'V_55',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.G__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS3, L.FFS5 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_216_87,(0,0,2):C.UVGC_216_88,(0,0,1):C.UVGC_216_89,(0,1,0):C.UVGC_213_78,(0,1,2):C.UVGC_213_79,(0,1,1):C.UVGC_213_80})

V_56 = CTVertex(name = 'V_56',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.G0 ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS1 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_217_90})

V_57 = CTVertex(name = 'V_57',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.H ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFS2 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_218_91})

V_58 = CTVertex(name = 'V_58',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_170_21,(0,1,0):C.UVGC_153_4,(0,2,0):C.UVGC_153_4})

V_59 = CTVertex(name = 'V_59',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_170_21,(0,1,0):C.UVGC_153_4,(0,2,0):C.UVGC_153_4})

V_60 = CTVertex(name = 'V_60',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_170_21,(0,1,0):C.UVGC_207_71,(0,2,0):C.UVGC_207_71})

V_61 = CTVertex(name = 'V_61',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_167_18,(0,1,0):C.UVGC_155_5,(0,2,0):C.UVGC_155_5})

V_62 = CTVertex(name = 'V_62',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_167_18,(0,1,0):C.UVGC_155_5,(0,2,0):C.UVGC_155_5})

V_63 = CTVertex(name = 'V_63',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.a ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_167_18,(0,1,0):C.UVGC_190_31,(0,2,0):C.UVGC_190_31})

V_64 = CTVertex(name = 'V_64',
                type = 'UV',
                particles = [ P.u__tilde__, P.u, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.u] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_168_19,(0,1,0):C.UVGC_171_22,(0,1,1):C.UVGC_171_23,(0,1,2):C.UVGC_171_24,(0,1,3):C.UVGC_171_25,(0,1,5):C.UVGC_171_26,(0,1,4):C.UVGC_171_27,(0,2,0):C.UVGC_171_22,(0,2,1):C.UVGC_171_23,(0,2,2):C.UVGC_171_24,(0,2,3):C.UVGC_171_25,(0,2,5):C.UVGC_171_26,(0,2,4):C.UVGC_171_27})

V_65 = CTVertex(name = 'V_65',
                type = 'UV',
                particles = [ P.c__tilde__, P.c, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.c, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_168_19,(0,1,0):C.UVGC_171_22,(0,1,1):C.UVGC_171_23,(0,1,3):C.UVGC_171_24,(0,1,4):C.UVGC_171_25,(0,1,5):C.UVGC_171_26,(0,1,2):C.UVGC_171_27,(0,2,0):C.UVGC_171_22,(0,2,1):C.UVGC_171_23,(0,2,3):C.UVGC_171_24,(0,2,4):C.UVGC_171_25,(0,2,5):C.UVGC_171_26,(0,2,2):C.UVGC_171_27})

V_66 = CTVertex(name = 'V_66',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.t] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_168_19,(0,1,0):C.UVGC_171_22,(0,1,1):C.UVGC_171_23,(0,1,2):C.UVGC_171_24,(0,1,3):C.UVGC_171_25,(0,1,5):C.UVGC_171_26,(0,1,4):C.UVGC_208_72,(0,2,0):C.UVGC_171_22,(0,2,1):C.UVGC_171_23,(0,2,2):C.UVGC_171_24,(0,2,3):C.UVGC_171_25,(0,2,5):C.UVGC_171_26,(0,2,4):C.UVGC_208_72})

V_67 = CTVertex(name = 'V_67',
                type = 'UV',
                particles = [ P.d__tilde__, P.d, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.d, P.g] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,2):C.UVGC_168_19,(0,1,0):C.UVGC_171_22,(0,1,1):C.UVGC_171_23,(0,1,3):C.UVGC_171_24,(0,1,4):C.UVGC_171_25,(0,1,5):C.UVGC_171_26,(0,1,2):C.UVGC_171_27,(0,2,0):C.UVGC_171_22,(0,2,1):C.UVGC_171_23,(0,2,3):C.UVGC_171_24,(0,2,4):C.UVGC_171_25,(0,2,5):C.UVGC_171_26,(0,2,2):C.UVGC_171_27})

V_68 = CTVertex(name = 'V_68',
                type = 'UV',
                particles = [ P.s__tilde__, P.s, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.g, P.s] ], [ [P.t] ] ],
                couplings = {(0,0,4):C.UVGC_168_19,(0,1,0):C.UVGC_171_22,(0,1,1):C.UVGC_171_23,(0,1,2):C.UVGC_171_24,(0,1,3):C.UVGC_171_25,(0,1,5):C.UVGC_171_26,(0,1,4):C.UVGC_171_27,(0,2,0):C.UVGC_171_22,(0,2,1):C.UVGC_171_23,(0,2,2):C.UVGC_171_24,(0,2,3):C.UVGC_171_25,(0,2,5):C.UVGC_171_26,(0,2,4):C.UVGC_171_27})

V_69 = CTVertex(name = 'V_69',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.g ],
                color = [ 'T(3,2,1)' ],
                lorentz = [ L.FFV1, L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b] ], [ [P.b, P.g] ], [ [P.c], [P.d], [P.s], [P.u] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,1):C.UVGC_168_19,(0,1,0):C.UVGC_171_22,(0,1,2):C.UVGC_171_23,(0,1,3):C.UVGC_171_24,(0,1,4):C.UVGC_171_25,(0,1,5):C.UVGC_171_26,(0,1,1):C.UVGC_191_32,(0,2,0):C.UVGC_171_22,(0,2,2):C.UVGC_171_23,(0,2,3):C.UVGC_171_24,(0,2,4):C.UVGC_171_25,(0,2,5):C.UVGC_171_26,(0,2,1):C.UVGC_191_32})

V_70 = CTVertex(name = 'V_70',
                type = 'UV',
                particles = [ P.d__tilde__, P.u, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_187_28,(0,0,1):C.UVGC_187_29})

V_71 = CTVertex(name = 'V_71',
                type = 'UV',
                particles = [ P.s__tilde__, P.c, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_187_28,(0,0,1):C.UVGC_187_29})

V_72 = CTVertex(name = 'V_72',
                type = 'UV',
                particles = [ P.b__tilde__, P.t, P.W__minus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_210_74,(0,0,2):C.UVGC_210_75,(0,0,1):C.UVGC_187_29})

V_73 = CTVertex(name = 'V_73',
                type = 'UV',
                particles = [ P.u__tilde__, P.d, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.d, P.g], [P.g, P.u] ], [ [P.d, P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_187_28,(0,0,1):C.UVGC_187_29})

V_74 = CTVertex(name = 'V_74',
                type = 'UV',
                particles = [ P.c__tilde__, P.s, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.c, P.g], [P.g, P.s] ], [ [P.c, P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_187_28,(0,0,1):C.UVGC_187_29})

V_75 = CTVertex(name = 'V_75',
                type = 'UV',
                particles = [ P.t__tilde__, P.b, P.W__plus__ ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2 ],
                loop_particles = [ [ [P.b, P.g] ], [ [P.b, P.g, P.t] ], [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_210_74,(0,0,2):C.UVGC_210_75,(0,0,1):C.UVGC_187_29})

V_76 = CTVertex(name = 'V_76',
                type = 'UV',
                particles = [ P.t__tilde__, P.t, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_211_76,(0,1,0):C.UVGC_212_77})

V_77 = CTVertex(name = 'V_77',
                type = 'UV',
                particles = [ P.b__tilde__, P.b, P.Z ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FFV2, L.FFV3 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_193_34,(0,1,0):C.UVGC_194_35})

V_78 = CTVertex(name = 'V_78',
                type = 'UV',
                particles = [ P.b__tilde__, P.b ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.b, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_192_33,(0,2,0):C.UVGC_192_33,(0,1,0):C.UVGC_189_30,(0,3,0):C.UVGC_189_30})

V_79 = CTVertex(name = 'V_79',
                type = 'UV',
                particles = [ P.c__tilde__, P.c ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.c, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_169_20,(0,1,0):C.UVGC_152_3,(0,2,0):C.UVGC_152_3})

V_80 = CTVertex(name = 'V_80',
                type = 'UV',
                particles = [ P.d__tilde__, P.d ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.d, P.g] ] ],
                couplings = {(0,0,0):C.UVGC_169_20,(0,1,0):C.UVGC_152_3,(0,2,0):C.UVGC_152_3})

V_81 = CTVertex(name = 'V_81',
                type = 'UV',
                particles = [ P.s__tilde__, P.s ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.s] ] ],
                couplings = {(0,0,0):C.UVGC_169_20,(0,1,0):C.UVGC_152_3,(0,2,0):C.UVGC_152_3})

V_82 = CTVertex(name = 'V_82',
                type = 'UV',
                particles = [ P.t__tilde__, P.t ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF2, L.FF3, L.FF4, L.FF5 ],
                loop_particles = [ [ [P.g, P.t] ] ],
                couplings = {(0,0,0):C.UVGC_209_73,(0,2,0):C.UVGC_209_73,(0,1,0):C.UVGC_206_70,(0,3,0):C.UVGC_206_70})

V_83 = CTVertex(name = 'V_83',
                type = 'UV',
                particles = [ P.u__tilde__, P.u ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.FF1, L.FF3, L.FF5 ],
                loop_particles = [ [ [P.g, P.u] ] ],
                couplings = {(0,0,0):C.UVGC_169_20,(0,1,0):C.UVGC_152_3,(0,2,0):C.UVGC_152_3})

V_84 = CTVertex(name = 'V_84',
                type = 'UV',
                particles = [ P.g, P.g ],
                color = [ 'Identity(1,2)' ],
                lorentz = [ L.VV1, L.VV3 ],
                loop_particles = [ [ [P.b] ], [ [P.g] ], [ [P.ghG] ], [ [P.t] ] ],
                couplings = {(0,0,0):C.UVGC_198_40,(0,0,1):C.UVGC_198_41,(0,0,2):C.UVGC_198_42,(0,0,3):C.UVGC_198_43,(0,1,0):C.UVGC_197_38,(0,1,3):C.UVGC_197_39})

