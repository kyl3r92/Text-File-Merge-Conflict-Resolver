# Text-File-Merge-Conflict-Resolver
When git produced files containing '<<<<<<< HEAD' that won't be detected as conflicting, use this.

Requires Python 3.5+
uses glob to iterate files, searching for 'merge markers' and deleting everything unwanted. 

TODO: Make filepath configurable, open dialog?
TODO: Only overwrite files, when you changed something
TODO: allow to use the 1st instead of the 2nd part (above/below the '=======')
TODO: use "startswith" instead of "==" to compare the lines with merge markers.
