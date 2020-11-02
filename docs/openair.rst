OpenAir specifications
======================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

`OpenAir format <http://www.winpilot.com/usersguide/userairspace.asp>`_ is an airspace and terrain description language. It is an easy to use and publicly available standard for displaying map information.
User can add or modify the data himself, therefore having a full control over what is being displayed on the screen.

More details `OpenAir specification page <http://www.winpilot.com/usersguide/userairspace.asp>`_

AIRSPACE related record types
-----------------------------

AC class:
    class = Airspace Class, see below:

    - **R** restricted
    - **Q** danger
    - **P** prohibited
    - **A** Class A
    - **B** Class B
    - **C** Class C
    - **D** Class D
    - **GP**    glider prohibited
    - **CTR**   CTR
    - **W** Wave Window

AN string:
    Airspace Name

AH string:
    Upper bound, composed by the altitude (meters or feet) followed by the relative area:

    - **AMSL** Above mean sea level
    - **AGL** Above ground level

AL string:
    Lower bound, ?

    - **SFC** ?

AT coordinate:
    Coordinate of where to place a name label on the map (optional)


TERRAIN related record types (WinPilot version 1.130 and newer)
---------------------------------------------------------------

TO string:
    Declares Terrain Open Polygon (optional)

TC string:
    Declares Terrain Closed Polygon (optional)

SP style, width, red, green, blue:
    Selects Pen to be used in drawing

SB red, green, blue:
    Selects Brush to be used in drawing

Record types common to both TERRAIN and AIRSPACE
------------------------------------------------

...



