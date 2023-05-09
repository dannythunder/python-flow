#!/usr/bin/env python3

from flow import Flow

#########################################################################
#   This method is used for mocking data when developing outside Flow   #
#########################################################################
def populateMockedData():

    # Setup mock data and run script
    data = {}
    data["id"] = "123"

    # Add mocked data object to Flow.data property
    Flow.data = data

#############################################################################################
#   This method fetches a list of tickets and retreive the data of the first ticket found   #
#############################################################################################
def main():
    
    # change httpList tp rpcList when pasting to Flow
    tickets = Flow.httpList("ticket/ticket")
    #print(tickets)

    if tickets['success'] == False:
        exit("Nothing found")

    # change httpOpen tp rpcOpen when pasting to Flow
    ticket = Flow.httpOpen("ticket/ticket", objectId=tickets['data'][0]['id'])
    print(ticket)

# Uncomment to populate mocked data
#populateMockedData()

# Run script
main()