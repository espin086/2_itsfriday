
import WazeRouteCalculator

# # TODO: put the code below into a Waze commute calculator into it's own function
# commutes = []

# for address in sample_df["clean_address"]:
#     from_address = "10757 Longworth Ave Santa Fe Springs CA 90670"
#     region = 'US'
#     try:
#         to_address = address
#         route = WazeRouteCalculator.WazeRouteCalculator(
#             from_address, to_address, region)
#         commutes.append(route.calc_route_info(real_time=False))
#     except:
#         commutes.append((0, 0))