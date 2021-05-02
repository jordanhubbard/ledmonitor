# ledmonitor

Simple project to monitor the various hops on my network which indicate different levels of connectivity (first radio link down, second radio link down, router down, etc) using a tri-state LED hooked to a Raspberry pi-zeroW.  Due to the topology of the network, almost all of the intermediate states are masked and this
is really a green/red status kind of thing, but I wrote it as if all of the states (and color codes) actually mattered since, why not?

Just for fun - not intended to be really useful.  It makes me happy to see the LED light up, but this is more of a prototype project which I will ultimately
replace with something far more useful (like a much better PI with a much better display) but this can, at least, be seen all the way across the room!
