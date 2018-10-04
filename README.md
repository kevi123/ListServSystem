# ListServSystem
This program runs in Python 3.5
Will not run correctly in python 2.7 ie strings input

think of organizations as following tree

                      org1
                  /           \
          org2                    org3
          / \                       /\
      user1 user2              user3    org5
                                        / \
                                    user4   user6



Function so the following

mkorg --> This creates an Organization. These organizations will be able to hold users and other organization.
create --> This creates a user which will belong to the current organizations
cd --> this lets us change between organizations, users and organizations will be created in the current organization you are in.
delOrg --> this lets us delete an organizations
delUser --> this lets us delete users from any organization at any level
notify --> this will send a message to every user in the current organization
