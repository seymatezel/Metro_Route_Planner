#  Ankara,Turkey Metro Route Optimizer

This project was developed as part of the **Global AI Hub & Akbank: Introduction to Python and AI Bootcamp**. The application models the Ankara Metro Network (Red, Blue, and Orange lines) as a graph data structure to help passengers find either the path with the fewest line transfers or the absolute fastest journey time.


## Project Objectives

The optimization engine implements two graph search algorithms to solve routing queries:

* **Fewest Transfers (BFS Algorithm):** Uses Breadth-First Search (BFS) to traverse adjacent stations level by level. It prioritizes the route that requires the absolute minimum number of train/line changes.
* **Fastest Route (A* Algorithm):** Uses the A* pathfinding approach combined with a priority queue. It evaluates the exact track segment travel times and dynamic transfer delays to return the quickest path in minutes.


## Future Roadmap & Enhancements
To scale this project into a production-ready transit application, the following updates are planned:

**Budget-Optimized Routing:** Adding a feature to calculate paths based on financial costs, such as ticket pricing, multi-passenger discounts, or distance-based fares.

**User Interface (UI) Integration:** Porting the core Python algorithm into a mobile application or web dashboard to create an interactive experience similar to Moovit or Google Maps.

**Multi-Stop Waypoints:** Extending the graph engine to support flexible itineraries, allowing users to add multiple intermediate stops to their journey.

**Scalable Real-World Datasets:** Optimizing the performance of the core graph classes to handle highly complex, large-scale metropolitan transit maps with dynamic real-time data updates.

**Live Station Density Mapping:** Implementing a real-time system to track station crowd levels and recommend alternative routes during rush hours to bypass heavily congested platforms.

## Sample Execution & Test Outputs

When the routing simulator runs, it dynamically evaluates the network and prints the following results to the console:

```text
=== Test Scenarios ===

1. From AŞTİ to OSB:
   - The route with the fewest transfers: AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB
   - The fastest route (25 minutes): AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB

2. From Batıkent to Keçiören:
   - The route with the fewest transfers: Batikent -> Demetevler -> Gar -> Keçiören
   - The fastest route (21 minutes): Batikent -> Demetevler -> Gar -> Keçiören

3. From Keçiören to AŞTİ:
   - The route with the fewest transfers: Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ
   - The fastest route (19 minutes): Keçiören -> Gar -> Gar -> Sıhhiye -> Kızılay -> AŞTİ

4. From Kızılay to Demetevler:
   - The route with the fewest transfers: Kızılay -> Ulus -> Demetevler
   - The fastest route (10 minutes): Kızılay -> Ulus -> Demetevler
