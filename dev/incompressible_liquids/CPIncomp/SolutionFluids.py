from __future__ import division, print_function
import numpy as np
from CPIncomp.DataObjects import SolutionData


class LiBrData(SolutionData):
    """
    Lithium Bromide solution from CoolProp 4
    Source: Patek et al.
    """
    def __init__(self):
        SolutionData.__init__(self)
        self.name = "LiBr"
        self.description = "Aqueous lithium-bromide solution "
        self.reference = "Patek2006"

        self.temperature.data         = np.array([2.73000e+02, 2.84947e+02, 2.96895e+02, 3.08842e+02, 3.20789e+02, 3.32737e+02, 3.44684e+02, 3.56632e+02, 3.68579e+02, 3.80526e+02, 3.92474e+02, 4.04421e+02, 4.16368e+02, 4.28316e+02, 4.40263e+02, 4.52211e+02, 4.64158e+02, 4.76105e+02, 4.88053e+02, 5.00000e+02]) # Kelvin
        self.concentration.data       = np.array([0.00000e+00, 3.94737e-02, 7.89474e-02, 1.18421e-01, 1.57895e-01, 1.97368e-01, 2.36842e-01, 2.76316e-01, 3.15789e-01, 3.55263e-01, 3.94737e-01, 4.34211e-01, 4.73684e-01, 5.13158e-01, 5.52632e-01, 5.92105e-01, 6.31579e-01, 6.71053e-01, 7.10526e-01, 7.50000e-01]) # mass fraction

        self.density.source             = self.density.SOURCE_EQUATION
        self.density.data               = np.array([
          [9.99737e+02, 1.02828e+03, 1.05847e+03, 1.09045e+03, 1.12439e+03, 1.16044e+03, 1.19883e+03, 1.23976e+03, 1.28349e+03, 1.33031e+03, 1.38052e+03, 1.43449e+03, 1.49262e+03, 1.55535e+03, 1.62319e+03, 1.69669e+03, 1.77644e+03, 1.86306e+03, 1.95717e+03, 2.05926e+03],
          [9.99432e+02, 1.02799e+03, 1.05820e+03, 1.09020e+03, 1.12416e+03, 1.16024e+03, 1.19866e+03, 1.23963e+03, 1.28341e+03, 1.33029e+03, 1.38057e+03, 1.43462e+03, 1.49284e+03, 1.55569e+03, 1.62367e+03, 1.69734e+03, 1.77730e+03, 1.86420e+03, 1.95864e+03, 2.06117e+03],
          [9.97273e+02, 1.02581e+03, 1.05599e+03, 1.08798e+03, 1.12191e+03, 1.15799e+03, 1.19639e+03, 1.23736e+03, 1.28115e+03, 1.32803e+03, 1.37834e+03, 1.43242e+03, 1.49070e+03, 1.55364e+03, 1.62173e+03, 1.69556e+03, 1.77573e+03, 1.86292e+03, 1.95775e+03, 2.06081e+03],
          [9.93706e+02, 1.02219e+03, 1.05233e+03, 1.08426e+03, 1.11815e+03, 1.15418e+03, 1.19255e+03, 1.23349e+03, 1.27725e+03, 1.32411e+03, 1.37442e+03, 1.42852e+03, 1.48684e+03, 1.54984e+03, 1.61805e+03, 1.69204e+03, 1.77245e+03, 1.85996e+03, 1.95526e+03, 2.05896e+03],
          [9.88999e+02, 1.01741e+03, 1.04748e+03, 1.07934e+03, 1.11317e+03, 1.14913e+03, 1.18745e+03, 1.22833e+03, 1.27205e+03, 1.31889e+03, 1.36918e+03, 1.42329e+03, 1.48165e+03, 1.54472e+03, 1.61305e+03, 1.68722e+03, 1.76791e+03, 1.85581e+03, 1.95166e+03, 2.05614e+03],
          [9.83326e+02, 1.01165e+03, 1.04164e+03, 1.07342e+03, 1.10716e+03, 1.14305e+03, 1.18130e+03, 1.22212e+03, 1.26579e+03, 1.31259e+03, 1.36286e+03, 1.41699e+03, 1.47538e+03, 1.53854e+03, 1.60701e+03, 1.68141e+03, 1.76243e+03, 1.85080e+03, 1.94732e+03, 2.05274e+03],
          [9.76806e+02, 1.00504e+03, 1.03492e+03, 1.06661e+03, 1.10027e+03, 1.13608e+03, 1.17425e+03, 1.21501e+03, 1.25862e+03, 1.30539e+03, 1.35565e+03, 1.40979e+03, 1.46825e+03, 1.53152e+03, 1.60018e+03, 1.67485e+03, 1.75627e+03, 1.84521e+03, 1.94253e+03, 2.04908e+03],
          [9.69524e+02, 9.97653e+02, 1.02744e+03, 1.05903e+03, 1.09260e+03, 1.12832e+03, 1.16641e+03, 1.20710e+03, 1.25067e+03, 1.29741e+03, 1.34768e+03, 1.40186e+03, 1.46040e+03, 1.52383e+03, 1.59271e+03, 1.66773e+03, 1.74964e+03, 1.83927e+03, 1.93755e+03, 2.04544e+03],
          [9.61539e+02, 9.89561e+02, 1.01924e+03, 1.05074e+03, 1.08421e+03, 1.11985e+03, 1.15787e+03, 1.19850e+03, 1.24203e+03, 1.28877e+03, 1.33906e+03, 1.39330e+03, 1.45197e+03, 1.51559e+03, 1.58478e+03, 1.66022e+03, 1.74272e+03, 1.83318e+03, 1.93261e+03, 2.04209e+03],
          [9.52893e+02, 9.80806e+02, 1.01038e+03, 1.04178e+03, 1.07516e+03, 1.11072e+03, 1.14868e+03, 1.18927e+03, 1.23278e+03, 1.27953e+03, 1.32987e+03, 1.38422e+03, 1.44306e+03, 1.50694e+03, 1.57649e+03, 1.65246e+03, 1.73569e+03, 1.82714e+03, 1.92793e+03, 2.03928e+03],
          [9.43613e+02, 9.71419e+02, 1.00090e+03, 1.03220e+03, 1.06550e+03, 1.10099e+03, 1.13890e+03, 1.17946e+03, 1.22297e+03, 1.26976e+03, 1.32019e+03, 1.37469e+03, 1.43375e+03, 1.49796e+03, 1.56799e+03, 1.64459e+03, 1.72869e+03, 1.82133e+03, 1.92372e+03, 2.03726e+03],
          [9.33716e+02, 9.61418e+02, 9.90799e+02, 1.02202e+03, 1.05525e+03, 1.09068e+03, 1.12856e+03, 1.16912e+03, 1.21266e+03, 1.25952e+03, 1.31008e+03, 1.36478e+03, 1.42415e+03, 1.48877e+03, 1.55937e+03, 1.63675e+03, 1.72189e+03, 1.81593e+03, 1.92020e+03, 2.03629e+03],
          [9.23208e+02, 9.50813e+02, 9.80108e+02, 1.01125e+03, 1.04442e+03, 1.07982e+03, 1.11769e+03, 1.15827e+03, 1.20188e+03, 1.24886e+03, 1.29960e+03, 1.35457e+03, 1.41431e+03, 1.47946e+03, 1.55074e+03, 1.62905e+03, 1.71542e+03, 1.81111e+03, 1.91758e+03, 2.03663e+03],
          [9.12089e+02, 9.39606e+02, 9.68824e+02, 9.99909e+02, 1.03304e+03, 1.06843e+03, 1.10631e+03, 1.14695e+03, 1.19066e+03, 1.23781e+03, 1.28880e+03, 1.34412e+03, 1.40433e+03, 1.47010e+03, 1.54222e+03, 1.62163e+03, 1.70946e+03, 1.80706e+03, 1.91609e+03, 2.03856e+03],
          [9.00348e+02, 9.27788e+02, 9.56945e+02, 9.87988e+02, 1.02110e+03, 1.05650e+03, 1.09443e+03, 1.13517e+03, 1.17904e+03, 1.22641e+03, 1.27772e+03, 1.33346e+03, 1.39425e+03, 1.46078e+03, 1.53389e+03, 1.61460e+03, 1.70413e+03, 1.80397e+03, 1.91596e+03, 2.04236e+03],
          [8.87967e+02, 9.15344e+02, 9.44457e+02, 9.75479e+02, 1.00860e+03, 1.04405e+03, 1.08206e+03, 1.12294e+03, 1.16702e+03, 1.21469e+03, 1.26639e+03, 1.32267e+03, 1.38415e+03, 1.45158e+03, 1.52587e+03, 1.60810e+03, 1.69961e+03, 1.80204e+03, 1.91742e+03, 2.04833e+03],
          [8.74919e+02, 9.02249e+02, 9.31338e+02, 9.62364e+02, 9.95525e+02, 1.03105e+03, 1.06920e+03, 1.11027e+03, 1.15462e+03, 1.20266e+03, 1.25485e+03, 1.31177e+03, 1.37408e+03, 1.44258e+03, 1.51824e+03, 1.60225e+03, 1.69605e+03, 1.80145e+03, 1.92072e+03, 2.05679e+03],
          [8.61164e+02, 8.88467e+02, 9.17556e+02, 9.48614e+02, 9.81848e+02, 1.01749e+03, 1.05582e+03, 1.09715e+03, 1.14184e+03, 1.19033e+03, 1.24312e+03, 1.30080e+03, 1.36409e+03, 1.43384e+03, 1.51111e+03, 1.59716e+03, 1.69360e+03, 1.80241e+03, 1.92613e+03, 2.06806e+03],
          [8.46654e+02, 8.73951e+02, 9.03066e+02, 9.34189e+02, 9.67533e+02, 1.00334e+03, 1.04191e+03, 1.08356e+03, 1.12868e+03, 1.17771e+03, 1.23121e+03, 1.28979e+03, 1.35422e+03, 1.42544e+03, 1.50455e+03, 1.59297e+03, 1.69242e+03, 1.80513e+03, 1.93391e+03, 2.08248e+03],
          [8.31323e+02, 8.58639e+02, 8.87810e+02, 9.19032e+02, 9.52530e+02, 9.88561e+02, 1.02742e+03, 1.06947e+03, 1.11509e+03, 1.16479e+03, 1.21911e+03, 1.27875e+03, 1.34452e+03, 1.41741e+03, 1.49866e+03, 1.58977e+03, 1.69267e+03, 1.80980e+03, 1.94431e+03, 2.10040e+03]]) # kg/m3

        self.specific_heat.source       = self.specific_heat.SOURCE_EQUATION
        self.specific_heat.data         = np.array([
          [4.22124e+03, 4.01348e+03, 3.79973e+03, 3.58258e+03, 3.36481e+03, 3.14935e+03, 2.93915e+03, 2.73714e+03, 2.54602e+03, 2.36805e+03, 2.20483e+03, 2.05694e+03, 1.92364e+03, 1.80253e+03, 1.68940e+03, 1.57844e+03, 1.46287e+03, 1.33622e+03, 1.19249e+03, 1.01868e+03],
          [4.19305e+03, 4.01236e+03, 3.82482e+03, 3.63285e+03, 3.43907e+03, 3.24618e+03, 3.05692e+03, 2.87394e+03, 2.69965e+03, 2.53601e+03, 2.38427e+03, 2.24469e+03, 2.11622e+03, 1.99625e+03, 1.88059e+03, 1.76382e+03, 1.64032e+03, 1.50614e+03, 1.36033e+03, 1.19951e+03],
          [4.18223e+03, 4.01012e+03, 3.83116e+03, 3.64774e+03, 3.46240e+03, 3.27780e+03, 3.09660e+03, 2.92137e+03, 2.75441e+03, 2.59756e+03, 2.45197e+03, 2.31777e+03, 2.19378e+03, 2.07731e+03, 1.96416e+03, 1.84905e+03, 1.72680e+03, 1.59442e+03, 1.45295e+03, 1.30289e+03],
          [4.17919e+03, 4.01004e+03, 3.83421e+03, 3.65405e+03, 3.47211e+03, 3.29103e+03, 3.11343e+03, 2.94185e+03, 2.77856e+03, 2.62537e+03, 2.48335e+03, 2.35259e+03, 2.23187e+03, 2.11846e+03, 2.00814e+03, 1.89570e+03, 1.77615e+03, 1.64696e+03, 1.51008e+03, 1.36785e+03],
          [4.18036e+03, 4.01219e+03, 3.83748e+03, 3.65862e+03, 3.47814e+03, 3.29866e+03, 3.12281e+03, 2.95311e+03, 2.79183e+03, 2.64074e+03, 2.50091e+03, 2.37239e+03, 2.25394e+03, 2.14282e+03, 2.03482e+03, 1.92474e+03, 1.80770e+03, 1.68140e+03, 1.54829e+03, 1.41166e+03],
          [4.18443e+03, 4.01642e+03, 3.84202e+03, 3.66361e+03, 3.48371e+03, 3.30496e+03, 3.12997e+03, 2.96127e+03, 2.80111e+03, 2.65126e+03, 2.51279e+03, 2.38573e+03, 2.26883e+03, 2.15936e+03, 2.05308e+03, 1.94483e+03, 1.82980e+03, 1.70580e+03, 1.57557e+03, 1.44298e+03],
          [4.19092e+03, 4.02272e+03, 3.84824e+03, 3.66985e+03, 3.49009e+03, 3.31159e+03, 3.13697e+03, 2.96876e+03, 2.80920e+03, 2.66006e+03, 2.52241e+03, 2.39628e+03, 2.28041e+03, 2.17206e+03, 2.06701e+03, 1.96011e+03, 1.84657e+03, 1.72431e+03, 1.59622e+03, 1.46654e+03],
          [4.19976e+03, 4.03117e+03, 3.85638e+03, 3.67778e+03, 3.49789e+03, 3.31936e+03, 3.14480e+03, 2.97674e+03, 2.81743e+03, 2.66864e+03, 2.53143e+03, 2.40583e+03, 2.29060e+03, 2.18297e+03, 2.07874e+03, 1.97276e+03, 1.86028e+03, 1.73927e+03, 1.61274e+03, 1.48515e+03],
          [4.21109e+03, 4.04197e+03, 3.86672e+03, 3.68773e+03, 3.50753e+03, 3.32875e+03, 3.15403e+03, 2.98587e+03, 2.82655e+03, 2.67784e+03, 2.54077e+03, 2.41541e+03, 2.30049e+03, 2.19325e+03, 2.08950e+03, 1.98410e+03, 1.87231e+03, 1.75214e+03, 1.62668e+03, 1.50055e+03],
          [4.22519e+03, 4.05543e+03, 3.87960e+03, 3.70007e+03, 3.51939e+03, 3.34020e+03, 3.16512e+03, 2.99667e+03, 2.83712e+03, 2.68824e+03, 2.55108e+03, 2.42569e+03, 2.31081e+03, 2.20369e+03, 2.10013e+03, 1.99500e+03, 1.88357e+03, 1.76389e+03, 1.63910e+03, 1.51393e+03],
          [4.24253e+03, 4.07200e+03, 3.89544e+03, 3.71524e+03, 3.53393e+03, 3.35415e+03, 3.17853e+03, 3.00960e+03, 2.84962e+03, 2.70036e+03, 2.56288e+03, 2.43723e+03, 2.32214e+03, 2.21487e+03, 2.11123e+03, 2.00609e+03, 1.89473e+03, 1.77522e+03, 1.65075e+03, 1.52613e+03],
          [4.26367e+03, 4.09224e+03, 3.91480e+03, 3.73376e+03, 3.55165e+03, 3.37111e+03, 3.19477e+03, 3.02516e+03, 2.86454e+03, 2.71470e+03, 2.57667e+03, 2.45052e+03, 2.33499e+03, 2.22733e+03, 2.12335e+03, 2.01793e+03, 1.90636e+03, 1.78672e+03, 1.66225e+03, 1.53780e+03],
          [4.28930e+03, 4.11679e+03, 3.93831e+03, 3.75624e+03, 3.57314e+03, 3.39165e+03, 3.21438e+03, 3.04389e+03, 2.88242e+03, 2.73176e+03, 2.59296e+03, 2.46608e+03, 2.34985e+03, 2.24154e+03, 2.13696e+03, 2.03099e+03, 1.91893e+03, 1.79887e+03, 1.67407e+03, 1.54945e+03],
          [4.32019e+03, 4.14640e+03, 3.96667e+03, 3.78337e+03, 3.59907e+03, 3.41640e+03, 3.23799e+03, 3.06637e+03, 2.90382e+03, 2.75210e+03, 2.61228e+03, 2.48440e+03, 2.36722e+03, 2.25800e+03, 2.15254e+03, 2.04574e+03, 1.93290e+03, 1.81212e+03, 1.68668e+03, 1.56154e+03],
          [4.35716e+03, 4.18187e+03, 4.00064e+03, 3.81588e+03, 3.63013e+03, 3.44603e+03, 3.26622e+03, 3.09323e+03, 2.92932e+03, 2.77628e+03, 2.63516e+03, 2.50602e+03, 2.38760e+03, 2.27717e+03, 2.17055e+03, 2.06261e+03, 1.94868e+03, 1.82687e+03, 1.70046e+03, 1.57445e+03],
          [4.40106e+03, 4.22399e+03, 4.04101e+03, 3.85450e+03, 3.66703e+03, 3.48123e+03, 3.29973e+03, 3.12507e+03, 2.95952e+03, 2.80486e+03, 2.66215e+03, 2.53143e+03, 2.41148e+03, 2.29953e+03, 2.19142e+03, 2.08203e+03, 1.96668e+03, 1.84350e+03, 1.71578e+03, 1.58854e+03],
          [4.45271e+03, 4.27356e+03, 4.08852e+03, 3.89997e+03, 3.71046e+03, 3.52265e+03, 3.33915e+03, 3.16251e+03, 2.99500e+03, 2.83839e+03, 2.69376e+03, 2.56114e+03, 2.43931e+03, 2.32551e+03, 2.21557e+03, 2.10438e+03, 1.98727e+03, 1.86236e+03, 1.73297e+03, 1.60412e+03],
          [4.51285e+03, 4.33130e+03, 4.14387e+03, 3.95293e+03, 3.76106e+03, 3.57089e+03, 3.38505e+03, 3.20609e+03, 3.03627e+03, 2.87737e+03, 2.73046e+03, 2.59559e+03, 2.47152e+03, 2.35551e+03, 2.24337e+03, 2.13002e+03, 2.01077e+03, 1.88376e+03, 1.75230e+03, 1.62145e+03],
          [4.58210e+03, 4.39779e+03, 4.20760e+03, 4.01393e+03, 3.81933e+03, 3.62644e+03, 3.43790e+03, 3.25624e+03, 3.08374e+03, 2.92218e+03, 2.77263e+03, 2.63513e+03, 2.50844e+03, 2.38984e+03, 2.27513e+03, 2.15922e+03, 2.03745e+03, 1.90793e+03, 1.77402e+03, 1.64077e+03],
          [4.66086e+03, 4.47342e+03, 4.28010e+03, 4.08332e+03, 3.88561e+03, 3.68963e+03, 3.49800e+03, 3.31327e+03, 3.13772e+03, 2.97311e+03, 2.82052e+03, 2.68000e+03, 2.55031e+03, 2.42872e+03, 2.31104e+03, 2.19218e+03, 2.06748e+03, 1.93506e+03, 1.79828e+03, 1.66220e+03]]) # J/kg-K

        self.saturation_pressure.source = self.saturation_pressure.SOURCE_EQUATION
        self.saturation_pressure.data   = np.array([
          [6.04584e+02, 5.94264e+02, 5.79332e+02, 5.60479e+02, 5.38753e+02, 5.15022e+02, 4.89421e+02, 4.60881e+02, 4.26952e+02, 3.84269e+02, 3.30070e+02, 2.64740e+02, 1.93977e+02, 1.27898e+02, 7.60339e+01, 4.19348e+01, 2.26792e+01, 1.28192e+01, 7.83769e+00, 4.77725e+00],
          [1.38411e+03, 1.36170e+03, 1.32911e+03, 1.28753e+03, 1.23881e+03, 1.18446e+03, 1.12454e+03, 1.05681e+03, 9.76423e+02, 8.77015e+02, 7.53714e+02, 6.07985e+02, 4.51609e+02, 3.04940e+02, 1.87552e+02, 1.07704e+02, 6.05269e+01, 3.51047e+01, 2.16143e+01, 1.31246e+01],
          [2.94021e+03, 2.89497e+03, 2.82889e+03, 2.74377e+03, 2.64255e+03, 2.52756e+03, 2.39848e+03, 2.25089e+03, 2.07591e+03, 1.86235e+03, 1.60235e+03, 1.29998e+03, 9.78035e+02, 6.74876e+02, 4.27985e+02, 2.54855e+02, 1.48276e+02, 8.80876e+01, 5.46759e+01, 3.31666e+01],
          [5.84814e+03, 5.76251e+03, 5.63692e+03, 5.47368e+03, 5.27702e+03, 5.04999e+03, 4.79122e+03, 4.49247e+03, 4.13846e+03, 3.71079e+03, 3.19788e+03, 2.60930e+03, 1.98670e+03, 1.39831e+03, 9.11654e+02, 5.60912e+02, 3.36772e+02, 2.04605e+02, 1.28123e+02, 7.78118e+01],
          [1.09762e+04, 1.08230e+04, 1.05975e+04, 1.03020e+04, 9.94173e+03, 9.51993e+03, 9.03272e+03, 8.46561e+03, 7.79359e+03, 6.98827e+03, 6.03416e+03, 4.95138e+03, 3.81232e+03, 2.73236e+03, 1.82672e+03, 1.15766e+03, 7.15248e+02, 4.43752e+02, 2.80484e+02, 1.70841e+02],
          [1.95691e+04, 1.93083e+04, 1.89231e+04, 1.84147e+04, 1.77881e+04, 1.70452e+04, 1.61772e+04, 1.51594e+04, 1.39530e+04, 1.25165e+04, 1.08316e+04, 8.93712e+03, 6.95356e+03, 5.06743e+03, 3.46608e+03, 2.25634e+03, 1.43097e+03, 9.05387e+02, 5.77832e+02, 3.53464e+02],
          [3.33314e+04, 3.29068e+04, 3.22776e+04, 3.14412e+04, 3.04004e+04, 2.91525e+04, 2.76793e+04, 2.59409e+04, 2.38792e+04, 2.14367e+04, 1.85953e+04, 1.54256e+04, 1.21202e+04, 8.96897e+03, 6.26381e+03, 4.17839e+03, 2.71408e+03, 1.74908e+03, 1.12734e+03, 6.93298e+02],
          [5.45080e+04, 5.38432e+04, 5.28550e+04, 5.15333e+04, 4.98736e+04, 4.78635e+04, 4.54686e+04, 4.26264e+04, 3.92529e+04, 3.52726e+04, 3.06739e+04, 2.55782e+04, 2.02826e+04, 1.52226e+04, 1.08356e+04, 7.39090e+03, 4.90726e+03, 3.21743e+03, 2.09442e+03, 1.29600e+03],
          [8.59536e+04, 8.49486e+04, 8.34502e+04, 8.14345e+04, 7.88826e+04, 7.57632e+04, 7.20160e+04, 6.75457e+04, 6.22353e+04, 5.59897e+04, 4.88152e+04, 4.09108e+04, 3.27212e+04, 2.48801e+04, 1.80215e+04, 1.25453e+04, 8.49928e+03, 5.66336e+03, 3.72327e+03, 2.31960e+03],
          [1.31191e+05, 1.29718e+05, 1.27516e+05, 1.24539e+05, 1.20740e+05, 1.16058e+05, 1.10391e+05, 1.03599e+05, 9.55218e+04, 8.60475e+04, 7.52165e+04, 6.33423e+04, 5.10726e+04, 3.93043e+04, 2.89289e+04, 2.05175e+04, 1.41610e+04, 9.58030e+03, 6.36038e+03, 3.99129e+03],
          [1.94453e+05, 1.92354e+05, 1.89209e+05, 1.84933e+05, 1.79440e+05, 1.72618e+05, 1.64305e+05, 1.54298e+05, 1.42386e+05, 1.28442e+05, 1.12566e+05, 9.52359e+04, 7.73710e+04, 6.02104e+04, 4.49733e+04, 3.24479e+04, 2.27824e+04, 1.56342e+04, 1.04801e+04, 6.62637e+03],
          [2.80711e+05, 2.77793e+05, 2.73411e+05, 2.67426e+05, 2.59688e+05, 2.50009e+05, 2.38143e+05, 2.23801e+05, 2.06710e+05, 1.86737e+05, 1.64077e+05, 1.39433e+05, 1.14083e+05, 8.97015e+04, 6.79156e+04, 4.97785e+04, 3.55086e+04, 2.46961e+04, 1.67116e+04, 1.06487e+04],
          [3.95686e+05, 3.91721e+05, 3.85753e+05, 3.77565e+05, 3.66916e+05, 3.53509e+05, 3.36979e+05, 3.16927e+05, 2.93005e+05, 2.65087e+05, 2.33508e+05, 1.99276e+05, 1.64133e+05, 1.30298e+05, 9.98937e+04, 7.42865e+04, 5.37734e+04, 3.78732e+04, 2.58654e+04, 1.66118e+04],
          [5.45851e+05, 5.40570e+05, 5.32605e+05, 5.21633e+05, 5.07283e+05, 4.89107e+05, 4.66583e+05, 4.39165e+05, 4.06418e+05, 3.68245e+05, 3.25177e+05, 2.78627e+05, 2.30925e+05, 1.84961e+05, 1.43448e+05, 1.08113e+05, 7.93290e+04, 5.65378e+04, 3.89594e+04, 2.52200e+04],
          [7.38419e+05, 7.31512e+05, 7.21076e+05, 7.06644e+05, 6.87669e+05, 6.63504e+05, 6.33413e+05, 5.96668e+05, 5.52736e+05, 5.01567e+05, 4.43967e+05, 3.81873e+05, 3.18351e+05, 2.57103e+05, 2.01539e+05, 1.53784e+05, 1.14271e+05, 8.23533e+04, 5.72426e+04, 3.73489e+04],
          [9.81327e+05, 9.72441e+05, 9.58991e+05, 9.40323e+05, 9.15661e+05, 8.84091e+05, 8.44605e+05, 7.96247e+05, 7.38367e+05, 6.71002e+05, 5.95321e+05, 5.13927e+05, 4.30794e+05, 3.50600e+05, 2.77560e+05, 2.14227e+05, 1.61058e+05, 1.17295e+05, 8.22158e+04, 5.40640e+04],
          [1.28321e+06, 1.27195e+06, 1.25487e+06, 1.23109e+06, 1.19953e+06, 1.15894e+06, 1.10795e+06, 1.04535e+06, 9.70335e+05, 8.83083e+05, 7.85230e+05, 6.80217e+05, 5.73126e+05, 4.69790e+05, 3.75345e+05, 2.92782e+05, 2.22524e+05, 1.63665e+05, 1.15649e+05, 7.66377e+04],
          [1.65340e+06, 1.63931e+06, 1.61792e+06, 1.58804e+06, 1.54821e+06, 1.49676e+06, 1.43190e+06, 1.35204e+06, 1.25626e+06, 1.14491e+06, 1.02023e+06, 8.86685e+05, 7.50701e+05, 6.19470e+05, 4.99161e+05, 3.93203e+05, 3.01887e+05, 2.24108e+05, 1.59595e+05, 1.06563e+05],
          [2.10186e+06, 2.08446e+06, 2.05799e+06, 2.02091e+06, 1.97129e+06, 1.90692e+06, 1.82548e+06, 1.72498e+06, 1.60433e+06, 1.46413e+06, 1.30736e+06, 1.13976e+06, 9.69347e+05, 8.04887e+05, 6.53712e+05, 5.19660e+05, 4.02756e+05, 3.01613e+05, 2.16400e+05, 1.45564e+05],
          [2.63922e+06, 2.61797e+06, 2.58559e+06, 2.54009e+06, 2.47897e+06, 2.39938e+06, 2.29837e+06, 2.17343e+06, 2.02332e+06, 1.84893e+06, 1.65420e+06, 1.44637e+06, 1.23534e+06, 1.03173e+06, 8.44126e+05, 6.76730e+05, 5.29121e+05, 3.99519e+05, 2.88708e+05, 1.95607e+05]]) # Pa

        self.Tmax = np.max(self.temperature.data)
        self.Tmin = np.min(self.temperature.data)
        self.xmax = np.max(self.concentration.data)
        self.xmin = np.min(self.concentration.data)
        self.xid      = self.ifrac_mass
        self.TminPsat = self.Tmin