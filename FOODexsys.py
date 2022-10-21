import os
import sys
import json
import operator

restaurantList = {}


def main():
    global restaurantList
    while (True):
        print("""
----------------------------------------------
 _______   ______       ______      _______
|   ____| /  __  \     /  __  \    |       \\
|  |__   |  |  |  |   |  |  |  |   |  .--.  |
|   __|  |  |  |  |   |  |  |  |   |  |  |  |
|  |   __|  `--'  | __|  `--'  | __|  '--'  | __
|__|  (__)\______/ (__)\______/ (__)_______/ (__)

---------- Figure Out Our Dinner -------------

Please enter a number to answer each question!
  ---   r : Restart   ---   q : Quit   ---
""")

        restaurantList = {}
        with open('json/restaurants.json') as restaurantsFile:
            restaurants = json.load(restaurantsFile)

        with open('json/amountOfTime.json') as restaurantsFile:
            amountOfTimeJson = json.load(restaurantsFile)

        with open('json/priceRange.json') as priceFile:
            priceRangeJson = json.load(priceFile)

        with open('json/diningExperience.json') as diningExpFile:
            diningExpJson = json.load(diningExpFile)

        with open('json/typeOfCuisine.json') as cuisineTypeFile:
            cuisineTypeJson = json.load(cuisineTypeFile)

        with open('json/alcohol.json') as alcoholFile:
            alcoholJson = json.load(alcoholFile)
        wantsAlcohol = False

        with open('json/bar.json') as barFile:
            barJson = json.load(barFile)

        with open('json/healthy.json') as healthyFile:
            healthyJson = json.load(healthyFile)

        with open('json/dateOfMeal.json') as dateOfMealFile:
            dateOfMealJson = json.load(dateOfMealFile)

        restaurantList = dict.fromkeys(restaurants)
        quit = False
        restart = False

        while True:
            amountOfTime = input("How much time do you have for this meal?\n"
                                 "1. Less than 30 minutes\n"
                                 "2. Between 30 and 60 minutes\n"
                                 "3. More than 60 minutes\n")

            if "1" in amountOfTime:
                for item in amountOfTimeJson["AmountOfTime"]:
                    if item["time"] == "Less than 30 minutes":
                        restaurantList[item["restaurant"]] = item["cf"]
                break
            elif "2" in amountOfTime:
                for item in amountOfTimeJson["AmountOfTime"]:
                    if item["time"] == "30 - 60 minutes":
                        restaurantList[item["restaurant"]] = item["cf"]
                break
            elif "3" in amountOfTime:
                for item in amountOfTimeJson["AmountOfTime"]:
                    if item["time"] == "More than 60 minutes":
                        restaurantList[item["restaurant"]] = item["cf"]
                break
            else:
                if amountOfTime in ["q", "quit", "Q"]:
                    quit = True
                    break
                elif amountOfTime in ["r", "restart", "R"]:
                    restart = True
                    break
                print("Invalid choice. Try again.\n")

        if quit:
            print("\nGood luck choosing your meal!")
            break
        if restart:
            print("\n")
            continue


        while True:
            priceRange = input("\nHow much would you like to spend on the meal?\n"
                               "1. $\n"
                               "2. $$\n"
                               "3. $$$\n"
                               "4. Doesn't Matter\n")
            if "1" in priceRange:
                for item in priceRangeJson["PriceRange"]:
                    if item["priceRange"] == "$":
                        if restaurantList[item["restaurant"]] is None:
                            restaurantList[item["restaurant"]] = item["cf"]
                        else:
                            restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]],
                                                                            item["cf"])
                break
            elif "2" in priceRange:
                for item in priceRangeJson["PriceRange"]:
                    if item["priceRange"] == "$$":
                        if restaurantList[item["restaurant"]] is None:
                            restaurantList[item["restaurant"]] = item["cf"]
                        else:
                            restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]],
                                                                            item["cf"])
                break
            elif "3" in priceRange:
                for item in priceRangeJson["PriceRange"]:
                    if item["priceRange"] == "$$$":
                        if restaurantList[item["restaurant"]] is None:
                            restaurantList[item["restaurant"]] = item["cf"]
                        else:
                            restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]],
                                                                            item["cf"])
                break
            elif "4" in priceRange:
                break
            else:
                if priceRange in ["q", "quit", "Q"]:
                    quit = True
                    break
                elif priceRange in ["r", "restart", "R"]:
                    restart = True
                    break
                print("Invalid choice. Try again.\n")

        if quit:
            print("\nGood luck choosing your meal!")
            break
        if restart:
            print("\n")
            continue

        driveThruOrDelivery = False

        while True:
            diningExp = input("\nWhat kind of dining experience would you like?\n"
                              "1. Drive-Thru/ Take-Out\n"
                              "2. Sit-Down\n"
                              "3. Delivery\n"
                              "4. Doesn't Matter\n")
            if "1" in diningExp:
                driveThruOrDelivery = True
                for item in diningExpJson["DiningExperience"]:
                    if item["diningExperience"] == "Drive-Thru/ Take-Out":
                        if restaurantList[item["restaurant"]] is None:
                            restaurantList[item["restaurant"]] = item["cf"]
                        else:
                            restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]],
                                                                            item["cf"])
                break
            elif "2" in diningExp:
                break
            elif "3" in diningExp:
                driveThruOrDelivery = True
                for item in diningExpJson["DiningExperience"]:
                    if item["diningExperience"] == "Delivery":
                        if restaurantList[item["restaurant"]] is None:
                            restaurantList[item["restaurant"]] = item["cf"]
                        else:
                            restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]],
                                                                            item["cf"])
                break
            elif "4" in diningExp:
                break
            else:
                if diningExp in ["q", "quit", "Q"]:
                    quit = True
                    break
                elif diningExp in ["r", "restart", "R"]:
                    restart = True
                    break
                print("Invalid choice. Try again.\n")

        if quit:
            print("\nGood luck choosing your meal!")
            break
        if restart:
            print("\n")
            continue

        while True:
            cuisineType = input("\nWhat type of cuisine would you like to eat?\n"
                                "1. Italian\n"
                                "2. Pizza\n"
                                "3. Seafood\n"
                                "4. American\n"
                                "5. Mexican\n"
                                "6. Asian\n"
                                "7. I don't know\n")
            if "1" in cuisineType:
                for item in cuisineTypeJson["TypeOfCuisine"]:
                    if item["typeOfCuisine"] == "Italian":
                        if restaurantList[item["restaurant"]] is None:
                            restaurantList[item["restaurant"]] = item["cf"]
                        else:
                            restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]],
                                                                            item["cf"])
                break
            elif "2" in cuisineType:
                for item in cuisineTypeJson["TypeOfCuisine"]:
                    if item["typeOfCuisine"] == "Pizza":
                        if restaurantList[item["restaurant"]] is None:
                            restaurantList[item["restaurant"]] = item["cf"]
                        else:
                            restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]],
                                                                            item["cf"])
                break
            elif "3" in cuisineType:
                for item in cuisineTypeJson["TypeOfCuisine"]:
                    if item["typeOfCuisine"] == "Seafood":
                        if restaurantList[item["restaurant"]] is None:
                            restaurantList[item["restaurant"]] = item["cf"]
                        else:
                            restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]],
                                                                            item["cf"])
                break
            elif "4" in cuisineType:
                for item in cuisineTypeJson["TypeOfCuisine"]:
                    if item["typeOfCuisine"] == "American":
                        if restaurantList[item["restaurant"]] is None:
                            restaurantList[item["restaurant"]] = item["cf"]
                        else:
                            restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]],
                                                                            item["cf"])
                break
            elif "5" in cuisineType:
                for item in cuisineTypeJson["TypeOfCuisine"]:
                    if item["typeOfCuisine"] == "Mexican":
                        if restaurantList[item["restaurant"]] is None:
                            restaurantList[item["restaurant"]] = item["cf"]
                        else:
                            restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]],
                                                                            item["cf"])
                break
            elif "6" in cuisineType:
                for item in cuisineTypeJson["TypeOfCuisine"]:
                    if item["typeOfCuisine"] == "Asian":
                        if restaurantList[item["restaurant"]] is None:
                            restaurantList[item["restaurant"]] = item["cf"]
                        else:
                            restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]],
                                                                            item["cf"])
                break
            elif "7" in cuisineType:
                break
            else:
                if cuisineType in ["q", "quit", "Q"]:
                    quit = True
                    break
                elif cuisineType in ["r", "restart", "R"]:
                    restart = True
                    break
                print("Invalid choice. Try again.\n")

        if quit:
            print("\nGood luck choosing your meal!")
            break
        if restart:
            print("\n")
            continue

        while not driveThruOrDelivery:
            alcohol = input("\nIs alcohol an important option with your meal?\n"
                            "1. Yes\n"
                            "2. No\n")
            if "1" in alcohol:
                wantsAlcohol = True
                for item in alcoholJson["Alcohol"]:
                    if restaurantList[item["restaurant"]] is None:
                        restaurantList[item["restaurant"]] = item["cf"]
                    else:
                        restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]], item["cf"])
                break
            elif "2" in alcohol:
                wantsAlcohol = False
                break
            else:
                if wantsAlcohol in ["q", "quit", "Q"]:
                    quit = True
                    break
                elif wantsAlcohol in ["r", "restart", "R"]:
                    restart = True
                    break
                print("Invalid choice. Try again.\n")

        if quit:
            print("\nGood luck choosing your meal!")
            break
        if restart:
            print("\n")
            continue

        while wantsAlcohol:
            bar = input("\nIs the presence of a bar in the restaurant an important factor?\n"
                        "1. Yes\n"
                        "2. No\n")
            if "1" in bar:
                for item in barJson["Bar"]:
                    if restaurantList[item["restaurant"]] is None:
                        restaurantList[item["restaurant"]] = item["cf"]
                    else:
                        restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]], item["cf"])
                break
            elif "2" in bar:
                break
            else:
                if bar in ["q", "quit", "Q"]:
                    quit = True
                    break
                elif bar in ["r", "restart", "R"]:
                    restart = True
                    break
                print("Invalid choice. Try again.\n")

        if quit:
            print("\nGood luck choosing your meal!")
            break
        if restart:
            print("\n")
            continue

        while True:
            healthy = input("\nIs a healthy option important for your meal?\n"
                            "1. Yes\n"
                            "2. No\n")
            if "1" in healthy:
                for item in healthyJson["Healthy"]:
                    if restaurantList[item["restaurant"]] is None:
                        restaurantList[item["restaurant"]] = item["cf"]
                    else:
                        restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]], item["cf"])
                break
            elif "2" in healthy:
                break
            else:
                if healthy in ["q", "quit", "Q"]:
                    quit = True
                    break
                elif healthy in ["r", "restart", "R"]:
                    restart = True
                    break
                print("Invalid choice. Try again.\n")

        if quit:
            print("\nGood luck choosing your meal!")
            break
        if restart:
            print("\n")
            continue

        mealDate = ""
        isTuesday = False
        while True:
            dateOfMeal = input("\nWhat day do you plan on eating?\n"
                               "1. Sunday\n"
                               "2. Monday\n"
                               "3. Tuesday\n"
                               "4. Wednesday\n"
                               "5. Thursday\n"
                               "6. Friday\n"
                               "7. Saturday\n")
            if "1" in dateOfMeal:
                mealDate = "sunday"
                break
            elif "2" in dateOfMeal:
                mealDate = "weekday"
                break
            elif "3" in dateOfMeal:
                isTuesday = True
                mealDate = "weekday"
                break
            elif "4" in dateOfMeal:
                mealDate = "weekday"
                break
            elif "5" in dateOfMeal:
                mealDate = "weekday"
                break
            elif "6" in dateOfMeal:
                mealDate = "weekend"
                break
            elif "7" in dateOfMeal:
                mealDate = "weekend"
                break
            else:
                if dateOfMeal in ["q", "quit", "Q"]:
                    quit = True
                    break
                elif dateOfMeal in ["r", "restart", "R"]:
                    restart = True
                    break
                print("Invalid choice. Try again.\n")

        if quit:
            print("\nGood luck choosing your meal!")
            break
        if restart:
            print("\n")
            continue

        while True:
            timeOfMeal = input("\nWhat meal are you planning?\n"
                               "1. Breakfast\n"
                               "2. Lunch\n"
                               "3. Dinner\n"
                               "4. Late Evening Meal\n")
            if "1" in timeOfMeal:
                meal = "breakfast"
                for item in dateOfMealJson["DateOfMeal"]:
                    if item["timeOfDay"] == "breakfast" and item["dayOfWeek"] == mealDate:
                        if restaurantList[item["restaurant"]] is None:
                            restaurantList[item["restaurant"]] = item["cf"]
                        else:
                            restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]],
                                                                            item["cf"])
                break
            elif "2" in timeOfMeal:
                meal = "lunch"
                for item in dateOfMealJson["DateOfMeal"]:
                    if item["timeOfDay"] == "lunch" and item["dayOfWeek"] == mealDate:
                        if restaurantList[item["restaurant"]] is None:
                            restaurantList[item["restaurant"]] = item["cf"]
                        else:
                            restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]],
                                                                            item["cf"])
                break
            elif "3" in timeOfMeal:
                meal = "dinner"
                for item in dateOfMealJson["DateOfMeal"]:
                    if item["timeOfDay"] == "dinner" and item["dayOfWeek"] == mealDate:
                        if restaurantList[item["restaurant"]] is None:
                            restaurantList[item["restaurant"]] = item["cf"]
                        else:
                            restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]],
                                                                            item["cf"])
                break
            elif "4" in timeOfMeal:
                meal = "late evening meal"
                for item in dateOfMealJson["DateOfMeal"]:
                    if item["timeOfDay"] == "late" and item["dayOfWeek"] == mealDate:
                        if restaurantList[item["restaurant"]] is None:
                            restaurantList[item["restaurant"]] = item["cf"]
                        else:
                            restaurantList[item["restaurant"]] = cfCombined(restaurantList[item["restaurant"]],
                                                                            item["cf"])
                break
            else:
                if timeOfMeal in ["q", "quit", "Q"]:
                    quit = True
                    break
                elif timeOfMeal in ["r", "restart", "R"]:
                    restart = True
                    break
                print("Invalid choice. Try again.\n")

        if quit:
            print("\nGood luck choosing your meal!")
            break
        if restart:
            print("\n")
            continue

        while isTuesday:
            tuesday = input("\nIs the planned meal on the first or last Tuesday of the month?\n"
                            "1. Yes\n"
                            "2. No\n")
            if "1" in tuesday:
                restaurantList["Dairy Queen"] = 1
                for key in restaurantList.keys():
                    if not 'dairy queen' in key.lower():
                        restaurantList[key] = -1
                break
            elif "2" in tuesday:
                break
            else:
                if tuesday in ["q", "quit", "Q"]:
                    quit = True
                    break
                elif tuesday in ["r", "restart", "R"]:
                    restart = True
                    break
                else:
                    print("Invalid choice. Try again.\n")

        if quit:
            print("\nGood luck choosing your meal!")
            break
        if restart:
            print("\n")
            continue

        # pprint("hello world")
        descending = sorted(restaurantList.items(), key=operator.itemgetter(1))
        descending.reverse()

        print("\nRESULTS:\n"
              "Based on your answers, you should choose " + descending[0][0] + "!\n")
        for restaurant, cf in descending:
            if cf > 0:
                print(restaurant + " : %.5f" % cf)

        answer = input("\nWould you like to try again?\n"
                       "1. Yes\n"
                       "2. No\n")
        if "1" in answer:
            print("\n")
            continue
        else:
            print("\nHope you have a great " + meal + "!")
            break

    return


def cfCombined(cf1, cf2):
    if cf1 > 0 and cf2 > 0:
        return cfCombinedPositive(cf1, cf2)
    elif cf1 < 0 and cf2 < 0:
        return cfCombinedNegative(cf1, cf2)
    else:
        return cfCombinedOppo(cf1, cf2)


def cfCombinedPositive(cf1, cf2):
    return (cf1 + cf2) - (cf1 * cf2)


def cfCombinedNegative(cf1, cf2):
    return (cf1 + cf2) + (cf1 * cf2)


def cfCombinedOppo(cf1, cf2):
    return (cf1 + cf2) / (1 - min(abs(cf1), abs(cf2)))


def certaintyAND(e1, e2):
    return max(e1.cf, e2.cf)


def certaintyOR(e1, e2):
    return min(e1.cf, e2.cf)


main()
