"""
Calculates the miles and average COMMUTE times between two addresses
"""


import WazeRouteCalculator


def calc_route(TO_ADDRESS, FROM_ADDRESS, region='US', real_time=False):
    """
    Calculates commute time between two locations
    """
    commutes = []
    region = region
    try:
        route = WazeRouteCalculator.WazeRouteCalculator(
            FROM_ADDRESS, TO_ADDRESS, region)
        commutes.append(route.calc_route_info(real_time=real_time))
    except:
        commutes.append((0, 0))
    return commutes


if __name__ == "__main__":
    TO_ADDRESS = str(input("To Address:  "))
    FROM_ADDRESS = str(input("From Address: "))
    COMMUTE = calc_route(TO_ADDRESS=TO_ADDRESS,
                         FROM_ADDRESS=FROM_ADDRESS)
    print("""
----------------------------------------------------------------
Commute Report
--------------------------------
""")
    print("Distance is {0} miles.".format(round(COMMUTE[0][0])))
    print("Drive time is {0} minutes or {1} hours.".format(
        round(COMMUTE[0][1]), round(COMMUTE[0][1])/60))
    print("-"*60)
