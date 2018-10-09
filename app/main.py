import sys

class PackageManager():

    def __init__(self):
        # tuple of (depnedency graph node, reverse dependency node)
        self.packages_dict = {}
        self.installed_dict = {}

    def main(self):

        while True:
            input_line = input(">>:")
            command_args = self.pars_command(input_line)
            command = command_args[0]

            if command == "END":
                break
            elif command == "DEPEND":
                if len(command_args) > 2:
                    self.depend(command_args[1], command_args[2:])
                else:
                    print (" BAD COMMAND")

            elif command == "LIST":
                self.list()

            elif command == "INSTALL":
                if len(command_args) > 1:
                    self.install(command_args[1])
                else:
                    print (" BAD COMMAND")

            elif command == "REMOVE":
                if len(command_args) > 1:
                    self.remove(command_args[1])
                else:
                    print (" BAD COMMAND")

            else:
                print (" BAD COMMAND")


    def pars_command(self, input_line):
        command = input_line.split(' ')
        return command

    def depend(self, pkg_name, dep_list):

        if pkg_name in self.packages_dict:
            all_dep_list = self.packages_dict[pkg_name][0]
            all_dep_list.extend(dep_list)
            self.packages_dict[pkg_name][0] = all_dep_list
        else:
            self.packages_dict[pkg_name] = [dep_list, []]

        for pk in dep_list:
            if pk in self.packages_dict:
                all_depd_list = self.packages_dict[pk][1]
                all_depd_list.append(pkg_name)
                self.packages_dict[pkg_name][1] = all_depd_list

            else:
                self.packages_dict[pk] = [[], [pkg_name]]


    def list(self):
        for pk in self.installed_dict:
            print(" {}".format(pk))

    def install(self, pkg_name):
        if pkg_name in self.installed_dict:
            self.installed_dict[pkg_name] = True
        else:
            self.installed_dict[pkg_name] = True
            print(" Installing {}.".format(pkg_name))
            if pkg_name in self.packages_dict:
                for pk in self.packages_dict[pkg_name][0]:
                    if pk not in self.installed_dict:
                        self.installed_dict[pk] = False
                        print(" Installing {}.".format(pk))

    def remove(self, pkg_name):
        if not pkg_name in self.installed_dict:
            print(" {} is not installed.".format(pkg_name))
            return

        if pkg_name in self.packages_dict:
            for pk in self.packages_dict[pkg_name][1]:
                if pk in self.installed_dict:
                    print(" {} is still needed.".format(pkg_name))
                    return

            del self.installed_dict[pkg_name]
            print(" Removing {}.".format(pkg_name))
            for pk in self.packages_dict[pkg_name][0]:
                if self.installed_dict[pk] == False:
                    can_remove = True
                    for dep_pk in self.packages_dict[pk][1]:
                        if dep_pk != pkg_name and dep_pk in self.installed_dict:
                            can_remove = False
                            break
                    if can_remove:

                        del self.installed_dict[pk]
                        print(" Removing {}.".format(pk))



PK_manger = PackageManager()
PK_manger.main()



