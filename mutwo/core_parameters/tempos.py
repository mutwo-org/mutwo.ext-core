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

"""Submodule for the parameter tempo.
"""

import typing

try:
    import quicktions as fractions
except ImportError:
    import fractions

import ranges

from mutwo import core_constants
from mutwo import core_parameters

__all__ = ("DirectTempoPoint", "WesternTempoPoint")


class DirectTempoPoint(core_parameters.abc.TempoPoint):
    """Simple `TempoPoint` that is directly initialised by its tempo.

    :param tempo: Specify a tempo in `beats per minute <https://en.wikipedia.org/wiki/Tempo#Measurement>`_.

    **Example:**

    >>> from mutwo import core_events
    >>> from mutwo import core_parameters
    >>> tempo_envelope = core_events.TempoEnvelope([
    ...     [0, core_parameters.DirectTempoPoint(60)]
    ... ])
    """

    def __init__(self, tempo: core_constants.Real | str):
        self.tempo = tempo

    @property
    def tempo(self) -> float:
        return self._tempo

    @tempo.setter
    def tempo(self, tempo: core_constants.Real | str):
        self._tempo = float(tempo)


class WesternTempoPoint(core_parameters.abc.TempoPoint):
    """A tempo point useful for western notation.

    :param tempo_range: Specify a tempo range in
        `beats per minute <https://en.wikipedia.org/wiki/Tempo#Measurement>`_.
        In western notation tempo is often indicated as a range from the
        minimal accepted tempo to the fastest accepted tempo. Therefore
        a :class:`WesternTempoPoint` is initialized by a range. In internal
        calculations the minimal (slowest) tempo is used. The tempo in
        the tempo range is relative as the absolute tempo depends on
        the ``reference``.
    :param reference: The reference with which the tempo is multiplied.
        In terms of Western notation a reference = 1 equals a 1/4 beat, a
        reference of 2 equals a 1/2 beat, etc. Default to 1.
    :type reference: float
    :param textual_indication: Sometimes it is desired to specify an extra
        text indication how fast or slow the music should be (for instance
        "Adagio" in Western music). Default to `None`.
    :type textual_indication: typing.Optional[str]

    **Example:**

    >>> from mutwo import core_events
    >>> from mutwo import core_parameters
    >>> tempo_envelope = core_events.TempoEnvelope([
    ...     [0, core_parameters.WesternTempoPoint(60, reference=2)]
    ... ])
    """

    def __init__(
        self,
        tempo_range: ranges.Range | core_constants.Real | str,
        reference: typing.Optional[core_constants.Real | str] = None,
        textual_indication: typing.Optional[str] = None,
    ):
        self.tempo_range = tempo_range
        self.reference = reference or core_parameters.configurations.DEFAULT_REFERENCE
        self.textual_indication = textual_indication

    @property
    def tempo(self) -> float:
        return self._tempo_range.start * self.reference

    @property
    def tempo_range(self) -> ranges.Range:
        """A range from the slowest to the fastest accepted tempo.

        In internal calculations the minimal (slowest) tempo is used.
        The tempo in the tempo range is relative as the absolute tempo
        depends on the ``reference``.
        """
        return self._tempo_range

    @tempo_range.setter
    def tempo_range(self, tempo_range: ranges.Range | core_constants.Real | str):
        match tempo_range:
            case ranges.Range():
                r = tempo_range
            case _:
                v = float(tempo_range)
                r = ranges.Range(v, v)
        self._tempo_range = r

    @property
    def reference(self) -> fractions.Fraction:
        """The reference with which the tempo is multiplied.

        In terms of Western notation a reference = 1 equals a 1/4 beat, a
        reference of 2 equals a 1/2 beat, etc. Default to 1.
        """
        return self._reference

    @reference.setter
    def reference(self, reference: core_constants.Real | str):
        self._reference = fractions.Fraction(reference)
