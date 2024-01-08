# Observing the Fission Fragments with Monte Carlo Algorithm 

## INTRODUCTION

In this study, the fission fragments produced in the fuel region by fission are investigated. 
The fuel region is spherical with a radius of  R_f = 0.16 mm and with an outer radius of 
R_shell = 0.18 mm.

The white region is the fuel region which is the centre of the sphere. The blue-shaded region
is the shell region. In every fission, two fission fragments are produced in opposite directions
at random points in the fuel region as shown in Figure 1.

![image](https://github.com/enesmertulu/Observing-Fission-Fragments-with-Monte-Carlo-Algorithm/assets/95104931/aee48578-24a2-4b7e-af5d-2d645a93b926)

Figure 1 – The Sphere Region and the Fission Event with Fission Products

The distance taken by the fission fragments is denoted with S. While S ≥ 0 probability density
function is given as:

P(S)= 0.7/l exp⁡(-S/l) + 0.3δ(S-d)

where l = 0.1 mm and d = 0.05 mm

In this study, the main purpose is to virtualise the distribution of fission fragments for 10^4,
10^6 and 10^8 fissions by using Monte Carlo Algorithm.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

Apache License
Version 2.0, January 2004

Copyright (c) 2024 Enes Mert Ulu

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
