3d-force-graph 1.80.1 (MIT)

Local fix: removed the synthetic document pointerup with pointerType touch and default pointerId 0 emitted at node drag end. With OrbitControls / Three.js r186 this event can clear pointer bookkeeping for the actual mouse pointer and throw reading pointer position x. The real browser pointerup continues to bubble to OrbitControls after navigation is enabled again, so drag completion retains the actual pointer identity.

Source: node_modules/3d-force-graph/dist/3d-force-graph.js, dragend callback. Reapply or confirm an upstream fix when replacing the vendored distribution.
