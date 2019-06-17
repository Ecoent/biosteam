# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:47:26 2018

@author: yoelr
"""

from .._unit import Unit
from .._exceptions import DesignError
from ._mixer import Mixer
from .decorators import cost
from .metaclasses import static
import numpy as np
import biosteam as bst

class Tank(Unit):
    """Abstract Tank class."""
    _units = {'Total volume': 'm^3'}

    @property
    def tau(self):
        """Residence time (hr)."""
        return self._tau
    @tau.setter
    def tau(self, tau):
        self._tau = tau

class StorageTank(Tank, metaclass=static):
    r"""Create a storage tank with volume based on residence time [1].

    .. math::

        V &= \\tau Q \\\\
        C_{fob}^{2007} &= 250000 + 94.2 V (2*10^3 < V < 50*10^3 m^3) \\\\

    **References**

        [1] Apostolakou, A. A., Kookos, I. K., Marazioti, C., & Angelopoulos, K. C. (2009). Techno-economic analysis of a biodiesel production process from vegetable oils. Fuel Processing Technology, 90(7–8), 1023–1031. https://doi.org/10.1016/j.fuproc.2009.04.017

    """
    line = 'Storage tank'
    
    #: [float] residence time (hr)
    _tau = 4*7*24

    def _design(self):
        Design = self._results['Design']
        V = self._tau*self._volnet_out
        Design['N'] = N = np.ceil(V/50e3)
        Design['Total volume'] = V/N
        return Design

    def _cost(self):
        Design = self._results['Design']
        N, V = Design.values()
        if V < 2e3:
            self._results['Cost']['Tank'] = N * (65000 + 158.7*(V/N)) * bst.CEPCI/525.4
        elif V < 50e3:
            self._results['Cost']['Tank'] = N * (250000 + 94.2*(V/N)) * bst.CEPCI/525.4
        else:    
            raise DesignError(f"Volume is out of bounds for costing")

@cost('Total volume', cost=12080, CE=525.4, exp=0.525, kW=0.591, limit=30)
class MixTank(Tank):
    """Create a mixing tank with volume based on residence time.

    .. math::

       V &= \\frac{\\tau* Q}{0.8}

       C_{fob}^{2007} &= 12080 * V^{0.525} (0.1 < V < 30 m^3)

    References

         [1] I.K. Kookos, Preliminary Chemical Process Synthesis and Design, Tziolas Publishing, Thessalonika, Greece, 2008 (book in Greek).

    """
    line = 'Mix tank'
    _tau = 1
    _N_ins = 2
    _run = Mixer._run
    _minimum_volume = 0.1
    
    #: Fraction of working volume
    _V_wf = 0.8
    
    @property
    def working_volume_fraction(self):
        """Fraction of working volume."""
        return self._V_wf

    @working_volume_fraction.setter
    def working_volume_fraction(self, V_wf):
        if not 0 < V_wf <= 1:
            raise ValueError('working_volume_fraction must be between 0 to 1')
        self._V_wf = V_wf
    
    def _design(self):
        V = self._tau * self.outs[0].volnet / self._V_wf
        if V < self._minimum_volume: self._lb_warning('Volume', V, self._minimum_volume)
        Design = self._results['Design']
        Design['Total volume'] = V

