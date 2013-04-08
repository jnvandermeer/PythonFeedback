These are some python scripts to do RtfMRI feedback.

It is just a very simple base system, including:

1 directory watcher
1 data tracker
1 'Percentage' calculator to go from data to [0-100]
1 TCP/IP communicator (it can only send integers right now)
1 'Thermo' Feedback

It should work with the output files from TurboBrainVoyager... but may be extensible to others

I should really clean it up, but wanted to put it into git as soon as I could (also for my understanding of repos)

Also I should investigate Threading of processes...

Also I should see how this works together with Pyff (for EEG feedback)

