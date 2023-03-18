from input_parser import TPInput
from landscape import Landscape
from backtracking import solve
import os
import time
import argparse

# parser to parse the input file
parser = argparse.ArgumentParser(description="Tile placement problem")
parser.add_argument("--input_file", "-i", type=str, help="Input file to be parsed", default="inputs/tilesproblem_1326658928646700.txt")
args = parser.parse_args()



def place_tiles(input_file: str) -> None:
    tile_input = TPInput(input_file)
    landscape = Landscape(tile_input)
    print(landscape)
    print(landscape.targets)
    
    start_time = time.time()
    solve(landscape, 0, 0)
    print(landscape)
    print(landscape.count_colors(landscape.bushes))
    print(landscape.print_output())
    
    print("CSP performed in %.3f seconds" % (time.time() - start_time)

if __name__ == "__main__":
    place_tiles(args.input_file)

