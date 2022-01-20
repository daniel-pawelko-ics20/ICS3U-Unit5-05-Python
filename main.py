#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Jan 2022
# Address


def address(
    name: str, aptnum: int, strnum: int, strname: str, city: str, prov: str, post: str
):
    # return formated address
    # process
    if aptnum:
        return f"{name}\n{aptnum}-{strnum} {strname}\n{city} {prov} {post}"
    else:
        return f"{name}\n{strnum} {strname}\n{city} {prov} {post}"


def main():
    # main function for address

    # details
    print("This program formats your address to a mailing address.")

    try:
        # input
        name = input("Enter your full name: ").upper()
        live_app = input("Do you live in an apartment? (y/n): ").lower()
        if live_app == "y":
            aptnum = input("Enter your apartment number: ")
            aptnum = int(aptnum)
        else:
            aptnum = None
        strnum = input("Enter your street number: ")
        strnum = int(strnum)
        strname = input(
            "Enter your street name AND type (Main St, Express Pkwy...): "
        ).upper()
        city = input("Enter your city: ").upper()
        prov = input(
            "Enter your province (as an abbreviation, ex: ON, BC...): "
        ).upper()
        post = input("Enter your postal code(123 456): ").upper()

        # output/calling function
        print(address(name, aptnum, strnum, strname, city, prov, post))
    except ValueError:
        print("Input must be an integer")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
