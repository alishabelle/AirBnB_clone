#!/usr/bin/python3
""" building console """

import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """ class that interprets commands """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """ command to quit program """
        return True

    def do_EOF(self, args):
        """ command to exit program """
        return True

    def emptyline(self):
        """ does not perform any action """
        pass

    def do_create(self, args):
        """ creates new instances """
        ListofArgs = args.split()
        if len(ListofArgs) == 0:
            print('** class name missing **')
        elif ListofArgs[0] != 'BaseModel':
            print("** class doesn\'t exist **")
        else:
            instance = BaseModel()
            instance.save()
            print(instance.id)

    def do_show(self, args):
        """ prints string rep of instance """
        ListofArgs = args.split()
        if len(ListofArgs) == 0:
            print('** class name missing **')
        elif ListofArgs[0] != 'BaseModel':
            print("** class doesn\'t exist **")
        elif len(ListofArgs) < 2:
            print('** instance id missing **')
        else:
            all_objs = storage.all()
            if len(all_objs) == 0:
                print('** no instance found **')
            else:
                a_key = 'BaseModel.' + ListofArgs[1]
                keys = list(all_objs.keys())
                if a_key in keys:
                    wouldbekwargs = all_objs[a_key]
                    instance = BaseModel(None, **wouldbekwargs)
                    print(instance)
                else:
                    print('** no instance found **')

    def do_destroy(self, args):
        """ deletes an instance based on the class name """
        ListofArgs = args.split()
        if len(ListofArgs) == 0:
            print('** class name missing **')
        elif ListofArgs[0] != 'BaseModel':
            print("** class doesn\'t exist **")
        elif len(ListofArgs) < 2:
            print('** instance id missing **')
        else:
            all_objs = storage.all()
            if len(all_objs) == 0:
                print('** no instance found **')
            else:
                a_key = 'BaseModel.' + ListofArgs[1]
                keys = list(all_objs.keys())
                if a_key in keys:
                    del all_objs[a_key]
                    all_objs = json.dumps(all_objs)
                    with open('file.json', 'w') as my_file:
                        my_file.write(all_objs)
                else:
                    print('** no instance found **')

    def do_all(self, args):
        """ prints string rep of all class instances """
        ListofArgs = args.split()
        listerine = []
        x = 0
        if len(ListofArgs) == 0:
            all_objs = storage.all()
            for key, val in all_objs.items():
                wouldbekwargs = all_objs[key]
                instance = BaseModel(None, **wouldbekwargs)
                listerine.append(instance.__str__())
            print(listerine)
        elif ListofArgs[0] == 'BaseModel':
            all_objs = storage.all()
            for key, val in all_objs.items():
                if 'BaseModel' in key:
                    x = 1
                    wouldbekwargs = all_objs[key]
                    instance = BaseModel(None, **wouldbekwargs)
                    listerine.append(instance.__str__())
            if x == 1:
                print(listerine)
            else:
                print("** class doesn\'t exist **")
        else:
            print("** class doesn\'t exist **")

    def do_update(self, args):
        """ updates instances based on class """
        ListofArgs = args.split()
        if len(ListofArgs) == 0:
            print("** class name missing **")
        elif ListofArgs[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(ListofArgs) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            a_key = ListofArgs[0] + "." + ListofArgs[1]
            if a_key not in all_objs.keys():
                print("** no instance found **")
            elif len(ListofArgs) == 2:
                print("** attribute name missing **")
            elif len(ListofArgs) == 3:
                print("** value missing **")
            else:
                x = 0
                int_success = 0
                float_success = -1
                string_success = -1
                numdots = 0
                check = 0
                if ListofArgs[2] != 'created_at' or ListofArgs[2] != 'updated_at' or 'id':
                    value = ListofArgs[3]
                    if ListofArgs[3][:1] == '"' or ListofArgs[3][-1:] == '"':
                        string_success = 0
                    elif ListofArgs[3][:1] == "'" or ListofArgs[3][-1:] == "'":
                        string_success = 0
                    if string_success == -1:
                        if value[0] == '-':
                            x = 1
                            value = value[1:]
                        for char in value:
                            if char == '.':
                                numdots += 1
                        for char in value:
                            if char == '.':
                                continue
                            if ord(char) not in range(ord('0'), ord('9')):
                                int_success = -1
                                break
                        if int_success == 0 and numdots == 1:
                            value = float(value)
                            if x == 1:
                                value = value * (-1)
                        elif int_success == 0 and numdots == 0:
                            value = int(value)
                            if x == 1:
                                value = value * (-1)
                        else:
                            if int_success == -1 and x == 1:
                                value = '-' + value
                    if value[:1] == '"' and value[-1:] == '"':
                        value = value[1:-1]
                    if value[:1] == "'" and value[-1:] == "'":
                        value = value[1:-1]
                    all_objs[a_key].update({'{}'.format(ListofArgs[2]): value})
                    all_objs = json.dumps(all_objs)
                    with open('file.json', 'w') as my_file:
                        my_file.write(all_objs)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
