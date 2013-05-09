#
# update-header - Updates the header comment in source files
# Copyright (C) 2013  Lorenzo Villani
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
#


def update_header(input_stream, new_header, output_stream, comment_string="#"):
    """
    Replaces or inserts a new header in a file.


    @param input_stream: The input file with the old (or missing) header.
    @type input_stream: file

    @param new_header: Input stream of the new header.
    @type new_header: file

    @param output_stream: Output stream for the new file with the header
        replaced.
    @type output_stream: file

    @param comment_string: The string used to start a comment which spans until
        the end of the line.
    @type comment_string: str
    """
    class State:
        Start, FoundHeaderStart, Done = range(3)

    state = State.Start

    for line in input_stream:
        if state == State.Start:
            # At the beginning of the file.
            if line.startswith("#!"):
                # Ignore the shebang and copy this line as-is. No state change.
                output_stream.write(line)
            elif line.startswith(comment_string):
                # Start -> FoundHeaderStart.
                state = State.FoundHeaderStart
            else:
                # Inject header then state transition: Start -> Done.
                inject_header(new_header, output_stream, comment_string)
                output_stream.write(line)

                state = State.Done
        elif state == State.FoundHeaderStart:
            # We have found the beginning of the header comment, now we have to
            # look for the first non comment line, then inject our header,
            # then transition from FoundHeaderStart -> Done.
            if not line.startswith(comment_string):
                inject_header(new_header, output_stream, comment_string)
                output_stream.write(line)

            state = State.Done
        elif state == State.Done:
            # Copy input to output verbatim
            output_stream.write(line)
    else:
        if state == State.Start:
            # Input is empty, inject the header and be done with it
            inject_header(new_header, output_stream, comment_string)

            state = State.Done

    output_stream.flush()


def inject_header(header_stream, output_stream, comment_string):
    """
    Writes the header onto the output stream.


    @param header_stream: Input stream for the header. A seek to the beginning
        of the file is performed with every call.
    @type header_stream: file

    @param output_stream: The stream where the header will be written.
    @type output_stream: file

    @param comment_string: The string used to start a comment which spans until
        the end of the line.
    @type comment_string: str
    """
    header_stream.seek(0)

    for line in header_stream:
        if line.strip() == "":
            output_stream.write(comment_string + "\n")
        else:
            output_stream.write(comment_string + " " + line.rstrip(' '))
