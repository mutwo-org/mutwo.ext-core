# This file is part of mutwo, ecosystem for time-based arts.
#
# Copyright (C) 2020-2023
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Time-based Event abstractions.

Event objects can be understood as the core objects
of the :mod:`mutwo` framework. They all own a :attr:`~mutwo.core_events.abc.Event.duration`
(of type :class:`~mutwo.core_parameters.abc.Duration`), a :attr:`~mutwo.core_events.abc.Event.tempo_envelope`
(of type :class:`~mutwo.core_events.TempoEnvelope`) and a :attr:`~mutwo.core_events.abc.Event.tag`
(of type ``str`` or ``None``).

The most often used classes are:

    - :class:`mutwo.core_events.Chronon`: the leaf or the node of a tree
    - :class:`mutwo.core_events.Consecution`: a sequence of other events
    - :class:`mutwo.core_events.Concurrence`: a simultaneous set of other events

Further more complex Event classes with more relevant attributes
can be generated through inheriting from basic classes.
"""

from . import configurations
from . import abc

from .basic import *
from .tempos import *
from .envelopes import *

from . import basic, envelopes

from mutwo import core_utilities

__all__ = core_utilities.get_all(basic, envelopes)

# Force flat structure
del basic, core_utilities, envelopes
