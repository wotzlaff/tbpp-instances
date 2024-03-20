# Benchmark Instances for the Temporal Bin Packing Problem (with Fire-Ups) and the Busy Time Minimization Problem

## Parts
### Part (A)
The instances were introduced in [[1]](#1).
A part of (small instances) are available at [here](https://github.com/sibirbil/TemporalBinPacking).

### Part (B)
The instances are generated from a subset of instances of the Temporal Knapsack Problem (TKP) and used in [[2]](#2).
The TKP instances can be found [here](http://or.dei.unibo.it/library).

### Part (C)
The instances were introduced in [[3]](#3) for a temporal bin packing problem in which the time-averaged number of active bins is minimized.

### Part (D)
The set of instances is derived from real-world VM traces originally introduced in [[4]](#4) and published [here](https://github.com/Azure/AzurePublicDataset).
In order to generate suitable instances, we only consider one capacity constraint given by the maximum CPU usage (over all possible machines) per job (VM).
Moreover, we exclude all jobs running in the whole time interval of 14 days or having a resource demand smaller than 0.25 or at least 0.75.
The subset selection is handled in [azure_from_database.py](azure_from_database.py) which uses the SQLite database published through the repository mentioned above.
Details of the sampling method can be found in [azure_sample.py](azure_sample.py).

## Format
An instance is represented by a list of items (jobs) and a bin (server) capacity.
The first row of each file summarizes the number of items and the capacity.
Each subsequent row represents one item (item index, starting time, ending time, item size).

## References

<a id="1">[1]</a>
Aydın, N., Muter, İ., & Birbil, Ş. İ. (2020). Multi-objective temporal bin packing problem: An application in cloud computing. Computers & Operations Research, 121, 104959. <https://doi.org/10.1016/j.cor.2020.104959>

<a id="2">[2]</a>
Dell'Amico, M., Furini, F., & Iori, M. (2020). A branch-and-price algorithm for the temporal bin packing problem. Computers & Operations Research, 114, 104825. <https://doi.org/10.1016/j.cor.2019.104825>

<a id="3">[3]</a>
Muir, C., Marshall, L., & Toriello, A. (2023). Temporal Bin Packing with Half-Capacity Jobs. INFORMS Journal on Optimization 6(1):46-62. <https://doi.org/10.1287/ijoo.2023.0002>

<a id="4">[4]</a>
Ori Hadary, Luke Marshall, Ishai Menache, Abhisek Pan, David Dion, Esaias Greeff, Star Dorminey, Shailesh Joshi, Yang Chen, Mark Russinovich and Thomas Moscibroda. "[Protean: VM Allocation Service at Scale](https://www.microsoft.com/en-us/research/publication/protean-vm-allocation-service-at-scale/)", in Proceedings of the 14th USENIX Symposium on Operating Systems Design and Implementation (OSDI 2020). USENIX Association, November 2020.
